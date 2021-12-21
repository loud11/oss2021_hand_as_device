# HAND MOTION RECOGNITION



First of all, a Python module called mediapipe was used entirely to make the hand recognized.



Since the computer system used in the development should have been executed in an environment of 

i3-4160 cpu and 8 gigabytes of RAM without gpu, practical and fast hand recognition was needed.



## Reference of Idea

thanks to these [link](https://gist.github.com/TheJLifeX/74958cc59db477a91837244ff598ef4a), [link2](https://google.github.io/mediapipe/solutions/hands.html) I just learned Mediapipe module, which is the core of this project.  I decided to implement it after confirming that there is a solution that can satisfy this project and the development environment.



## Media pipe Detail

Using the mediapipe module, your PC recognizes your hand through the web cam as follows.



[](https://github.com/loud11/oss2021_hand_as_device/blob/main/resource/hand/hand_onmarked.png)



Using the 21 dots marked on hand,  can easily extract feature vectors of poses taken with hand,

extract feature vectors by capturing motions such as holding hands, blooming, signing pieces, or raising thumbs.



But what movements are taking with a hand were made to extract and learn feature vectors using tensorflow to classify what movements they are taking.



There are a total of 7 hand motions used in this project, but about 5 are actually used in the program.
That's what happened when I made an extra to map keys corresponding to hand motion.



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



## model used in this section



![](https://github.com/loud11/oss2021_hand_as_device/blob/main/resource/hand/model.png)

The picture above is part of the source code of the hand_gesture_learn.py file.



This model was just used based on what was on the link to this site [link](https://optisol.com.au/insight/alphabet-hand-gestures-recognition-using-mediapipe/).



The input value of the model is in the form of receiving 42 inputs. Because when you recognize your hand in media pipe, you write x,y on 21 points, so you store it like that.



we could expect an amazing effect by just dropping out on the floor about two times.



### model evaluation



![](https://github.com/loud11/oss2021_hand_as_device/blob/main/resource/hand/hand_model_loc.png)



![](https://github.com/loud11/oss2021_hand_as_device/blob/main/resource/hand/hand_model_loc_loss.png)



It is predicted that it will still show high accuracy in making the user aware of his or her own hand, although there are some parts that are too overfitting.



![](https://github.com/loud11/oss2021_hand_as_device/blob/main/resource/hand/final.png)



The figure above is a coating matrix that was initially learned based on the data I made, and I am a little confused between clenching my fist and clenching my index finger.