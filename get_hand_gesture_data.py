import mediapipe as mp
import cv2
import csv
import numpy as np

ascii_number_start = ord('0')
ascii_number_end = ord('9')
keyboard_r = ord('r')
keyboard_h = ord('h')
record_flag = False
learning_label = 0

learning_data_file_name = "learning_data.csv"
fp = open(learning_data_file_name, 'a', newline="")
csv_handler = csv.writer(fp)
record_count = 0
mpDraw = mp.solutions.drawing_utils

def normalized_learn_data(given_landmarks):
    thumb_x, thumb_y = given_landmarks[0][0], given_landmarks[0][1]
    temp_marks = [[point[0] - thumb_x, point[1] - thumb_y] for point in given_landmarks]
    temp = np.array(temp_marks).ravel()
    max_mark = max(np.absolute(temp))
    return temp / max_mark


cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
while True:
    _, frame = cap.read()
    x, y, _ = frame.shape
    frame = cv2.flip(frame, 1)
    frame_in_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_in_rgb)

    if result.multi_hand_landmarks:
        hand_positions = []
        for hand_points in result.multi_hand_landmarks:
            for point in hand_points.landmark:
                hand_positions.append([int(point.x * x), int(point.y * y)])
            mpDraw.draw_landmarks(frame, hand_points, mpHands.HAND_CONNECTIONS)
        cv2.putText(frame, "HAND!", (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 2, cv2.LINE_AA)

        if record_flag:
            record_count += 1
            if record_count > 1000:
                record_flag = False
                print("record finished!")
                record_count = 0
                learning_label += 1
            print(record_count)
            csv_handler.writerow([learning_label, *normalized_learn_data(np.array(hand_positions))])

    cv2.imshow("Output", frame)

    key_pressed = cv2.waitKey(1)
    if key_pressed == 27:  # ESC:
        break
    if ascii_number_start <= key_pressed <= ascii_number_end:
        learning_label = key_pressed - ascii_number_start
        print("learning label = ", learning_label)
    if key_pressed == keyboard_r:
        record_flag = True
        print("learning label = ", learning_label)
    if key_pressed == keyboard_h:
        record_flag = False

cap.release()
fp.close()
