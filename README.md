# EML-NET-Saliency
This repo contains the code and the pre-computed saliency maps used in our paper: "EML-NET: An Expandable Multi-Layer NETwork for saliency prediction".

## Training
Our training code is based on the [SALICON](http://salicon.net/challenge-2017/) dataset, we assume you already download and unzip the images and annotations under your workspace.
```
workspace
└───Images
│     │   *.jpg
|     |
└───fixations
|       |  *.mat
|       |
└───maps
     │   *.png
```

Our training code "train_resnet.py" taks two mandatory arguements, 1. "data_folder"(the path of your workspace). 2 "output_folder"(the folder you want to save the trained model). One more optional arguement you might want to set is "--model_path", pre-trained on ImageNet or PLACE365 for classification, it will train from scratch if not specified.

TODO: the nasnet training code will be merged into this training file and the dataloder will be discarded.

## Predict
You can make a prediction on any images you want by running "eval.py". This file takes two compulsory arguements: 1. "model_path"(where you saved the pre-trained saliency mdoel). 2. "img_path"(the path of the input image).
