# Extended MNIST RECOGNITION



EMNIST is an extended version of MNIST and can be seen as an extended dataset used to make handwriting recognized in the field of machine learning.



## how to get Data?



Python has a module([emnist_python](https://pypi.org/project/emnist/)) that facilitates access to emnist data.

In this repository project, the module was used in "emnist_model_learn.py" and learned by tensorflow.



![](https://github.com/loud11/OSS2021/blob/main/resource/emnist/emnist_breakdown.png)

The above picture shows how the python module emnist stores emnist data.

Here, we used the dataset in the section "by merge". From 0 to 9, from a to z, there are more than 62 classes that must be classified from A to Z. If you want to use datasets that remove overlapping parts due to the nature of the alphabet, use a by-merge section with a lot of data, you can reduce it to 47 classes.

Considering the above mentioned points, "by merge" datasets were used.



## model used in this section



![](https://github.com/loud11/OSS2021/blob/main/resource/emnist/emnist_model.png)

The picture above is part of the source code of the "emnist_model_learn.py" file.



The system used to develop was not high-performance, so we couldn't evaluate the model by drawing a roc curve while increasing the epoch. But just 1 epoch of result is flows.



![](https://github.com/loud11/OSS2021/blob/main/resource/emnist/emnist_bymerge_result.png)

