from tensorflow.keras.models import load_model
import pyautogui
import numpy as np
import cv2
import mediapipe as mp

record_flag = False
emnist_model_filename = 'finalized_emnist_model_merged'#_merged'  # 'finalized_mnist_model'
hand_rec_model_filename = 'hand_made_hand_guesture_model'
ascii_number_start = ord('0')
ascii_number_end = ord('9')
ascii_Big_start = ord('A')
ascii_Small_start = ord('a')
emnist_enum_by_class = [chr(i) for i in range(48, 58)]
emnist_enum_by_class += [chr(i) for i in range(ascii_Big_start, ascii_Big_start + 26)]
emnist_enum_by_class += [chr(i) for i in range(ascii_Small_start, ascii_Small_start + 26)]
white = (0xff)
black = (0x00)
GRAY_SCALE = "L"
mnist_width = 28
mnist_height = 28
mnist_size = mnist_width, mnist_height
screen_width, screen_height = pyautogui.size()
screen_move_x = lambda camera_x, thumb_x: screen_width * thumb_x // camera_x
screen_move_y = lambda camera_y, thumb_y: screen_height * thumb_y // camera_y

mp_Hands = mp.solutions.hands
hands_processor = mp_Hands.Hands(max_num_hands=1, min_detection_confidence=0.8)
camera = cv2.VideoCapture(0)
# camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
# camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
# camera.set(cv2.CAP_PROP_FPS, 60)

index_finger = []
record_thumb_flag = False
loaded_emnist_model = load_model(emnist_model_filename)
hand_model = load_model(hand_rec_model_filename)
hand_gesture_names = ['open', 'close', '1 finger', 'two finger', 'three finger', 'thumbs up', 'thumbs down']
action_names = ['move', 'stop', 'N/D', 'record', 'click', 'record entered', 'N/D']


def normalized_learn_data(given_landmarks):
    thumb_x, thumb_y = given_landmarks[0][0], given_landmarks[0][1]
    temp_marks = [[point[0] - thumb_x, point[1] - thumb_y] for point in given_landmarks]
    temp = np.array(temp_marks).ravel()
    max_mark = max(np.absolute(temp))
    return temp / max_mark


def points_to_mnist(pixels, x=480, y=640):
    target = np.full(mnist_size, black, dtype=int)
    for i in pixels:
        y_cell = i[1] * 28 // y
        x_cell = i[0] * 28 // x
        if y_cell >= 28 or x_cell >= 28:
            continue
        target[y_cell][x_cell] = white
    return target


def mnist_prediction(target):
    predicted = loaded_emnist_model.predict(target.reshape(1, 28, 28, 1))
    print("prediction : ", np.argmax(predicted), emnist_enum_by_class[np.argmax(predicted)])
    return emnist_enum_by_class[np.argmax(predicted)]


def loop_init():
    _, frame_data = camera.read()
    x, y, _ = frame_data.shape
    frame_data = cv2.flip(frame_data, 1)
    frame_rgb = cv2.cvtColor(frame_data, cv2.COLOR_BGR2RGB)
    return hands_processor.process(frame_rgb), x, y, frame_data


while True:
    cam_hand_result, x, y, frame = loop_init()
    predict_name = ''

    if cam_hand_result.multi_hand_landmarks:
        markers = []
        for hand_points in cam_hand_result.multi_hand_landmarks:
            for point in hand_points.landmark:
                markers.append([int(point.x * x), int(point.y * y)])
            hand_gesture_prediction = np.argmax(hand_model.predict(normalized_learn_data(markers).reshape(1, 42)))
            predict_name = action_names[hand_gesture_prediction]

            if record_thumb_flag:
                pyautogui.moveTo(screen_move_x(x, markers[0][0]),
                                 screen_move_y(y, markers[0][1]))
            # class_names = ['open', 'close', '1 finger', 'two finger', 'three finger', 'thumbs up', 'thumbs down']
            if hand_gesture_prediction == 0:  # cursor moves
                record_thumb_flag = True
            if hand_gesture_prediction == 1:  # cursor stop
                record_thumb_flag = False
            if hand_gesture_prediction == 4:  # cursor click event
                pyautogui.click()
            if hand_gesture_prediction == 3:  # record hand writing coord for key board action
                index_finger.append(markers[8])
            if hand_gesture_prediction == 5:  # key board key entered
                record_index_flag = False
                if index_finger:
                    pyautogui.write(mnist_prediction(points_to_mnist(index_finger, x, y)))
                index_finger = []

    for i in index_finger:  # draw hand writing
        cv2.circle(frame, (i[0], i[1]), radius=0, color=(0, 0, 255), thickness=3)

    cv2.putText(frame, predict_name, (30, 30), cv2.FONT_ITALIC, 1, (0, 0, 255), 2)

    cv2.imshow("CAM", frame)
    key_pressed = cv2.waitKey(1)
    if key_pressed == 27:  # ESC:
        break

camera.release()
cv2.destroyAllWindows()