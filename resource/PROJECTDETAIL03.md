# Demo Details



In this section, 

you can understand how the input method used in the demo is configured 

and learn how to run the demo yourself.



## what can i do with this project?



To introduce the project again, 

the idea of this project is to replace the input of the mouse and keyboard, 

which are input devices of the PC, by making the movement of the hand recognized.



Naturally, by understanding the details of this section, 

you can run the program of this project and control the PC only with the movement of your hands.



## how to start?



**before you start, your computer should make your webcam available.**



open your terminal and follow instruction below

```
type this at cmd prompt or terminal

prompt\: conda env create --file environment.yaml
prompt\: conda activate oss2021
(oss2021)prompt\: python main.py
```

python main.py may take while. so wait it for 1~2 minutes.



and then You will see the screen that the webcam is recording.

If you want to exit, press the esc key to exit.



In this way, you learned how to run and exit the main program of this project. Congratulations!



Now you can use the window as a measure to see if your hand gestures are well recognized in the system.



## how to use?



This project recognizes your hand gestures 

and determines whether to move or click the mouse or enter the keyboard.



Let's check below to see what hand gestures this project recognizes.



The seven hand gestures recognized in this project are as follows.



![](https://github.com/loud11/oss2021_hand_as_device/blob/main/resource/hand/handopen.png)

hand open

![](https://github.com/loud11/oss2021_hand_as_device/blob/main/resource/hand/close.png)

hand close

![](https://github.com/loud11/oss2021_hand_as_device/blob/main/resource/hand/1finger.png)

1 finger unfold

![](https://github.com/loud11/oss2021_hand_as_device/blob/main/resource/hand/2finger.png)

2 finger unfold

![](https://github.com/loud11/oss2021_hand_as_device/blob/main/resource/hand/3finger.png)

3 finger unfold

![](https://github.com/loud11/oss2021_hand_as_device/blob/main/resource/hand/thumbsup.png)

thumbs up

![](https://github.com/loud11/oss2021_hand_as_device/blob/main/resource/hand/thumbsdown.png)

thumbs down



A total of 7 hand gestures can be recognized in this project, but only 5 are used to control mouse movement, click, and keyboard input.

I made about 7 for extra , but later you can modify the contents in main.py and customize them in the direction you want.



Anyway, let's see how four hand gestures are used to control PC input.

### 

### hand open(cursor move control)



When you light your hand on the webcam with your hand opened, 

your pc moves the mouse relative to the thumb of your open hand.



If you want to move the mouse, you have to move your hands with your hands folded.



### hand close(cursor move stop)

When you light your hand on the webcam with your hand closed, 

your pc will stop moving your cursor.



### 3 finger unfold

If you're pointing your hands at the webcam with three fingers unfolded, 

your PC will Launch a click event where the cursor was located.





### 2 finger unfold

If you're pointing your hands at the webcam with two fingers unfolded, 

your PC will use the position of the index fingers to draw a white line on the image of the webcam.



You can control the white line. 

If you make the white line draw a certain symbol or letter by moving two unfold fingers, 

the PC will refer to it as an input close to that figure.



### thumbs up



This is a hand signal to convert the white line drawn in Section 2 finger unfold above 

into the input of the system.



Keyboard input is entered as an input value for a symbol corresponding to the white line.

And the white line on the webcam disappears.
