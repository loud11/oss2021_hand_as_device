# OSS 2021
This repository is for OPEN SOURCE SOFTWARE COURSE 2021



# PROJECT SUMMARY



The project in this repository wanted to recognize the user's hand through a laptop's webcam so that it could be entered instead of a mouse or keyboard with hand gestures.



If you wanna see project details,

Please refer to the project details section of this read me file.



# HOW TO START?

This project was built using the virtual environment of Anaconda, 

so Anaconda must be installed in the system.



```
type this at cmd prompt or terminal

prompt\: conda env create --file environment.yaml
prompt\: conda activate oss2021
(oss2021)prompt\: python main.py
```



python main.py may take while. so wait it for 1~2 minutes.



## DEMO



![](https://github.com/loud11/oss2021_hand_as_device/blob/main/resource/short_demo_hand_act.gif)

The demo video above is an image that recognizes the user's hand movement, moves the mouse cursor, and clicks.



![](https://github.com/loud11/oss2021_hand_as_device/blob/main/resource/short_demo_handwriting.gif)

The demo video above is a gif video that recognizes the user's hand movement and recognizes hand-drawn letters in the air, so that letters are entered instead of keyboard input.



Please click the [link](https://github.com/loud11/oss2021_hand_as_device/blob/main/resource/PROJECTDETAIL03.md) to find out more about the key mapping demonstrated in the demo.



# Project Detail

And the module that can recognize hand used the link([**mediapipe**](https://pypi.org/project/mediapipe/)) entirely.



The project is largely divided into two parts.



It is divided into two parts: 



1. (HAND MOTION RECOGNITION)

extracting hand motion feature vectors using **mediape** and 

then making hand motion recognition using vectors, 

Click the ([link](https://github.com/loud11/oss2021_hand_as_device/blob/main/resource/PROJECTDETAIL01.md)) to see how you handled this part of the project.



2. (Extended MNIST RECOGNITION)

emnist training to recognize handwriting in the air.

Click the ([link](https://github.com/loud11/oss2021_hand_as_device/blob/main/resource/PROJECTDETAIL02.md)) to see how you handled this part of the project.

