# EML-NET-Saliency
This repo contains the code and the pre-computed saliency maps used in our paper: "EML-NET: An Expandable Multi-Layer NETwork for saliency prediction".

## Training
Our training code is based on the [SALICON](http://salicon.net/challenge-2017/) dataset, we assume you already download and unzip the images and annotations under your workspace.
```
salicon
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

```
python train_resnet.py ~/salicon imagenet_resnet --model_path backbone/resnet50.pth.tar
```
A suffix of "_eml" will be added to the output path, e.g., imagenet_resnet_eml in this case. If you specify the loss flag, --mse, the added suffix will be "_mse". You can simply compare our proposed loss function against the standard mean squared error.


TODO: the nasnet training code will be merged into this training file and the dataloder will be discarded.

## Make a prediction
You can make a prediction on any images you want by running "eval.py". This file takes two compulsory arguements: 1. "model_path"(where you saved the pre-trained saliency mdoel). 2. "img_path"(the path of the input image).
```
python eval.py pretrained_sal/imagenet_sal.pth.tar examples/115.jpg
```
Download the pre-trained model first and save it somewhere, e.g., pretrained_sal.

TODO: upload the pre-trained model.
