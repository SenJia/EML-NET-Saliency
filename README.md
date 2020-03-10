# EML-NET-Saliency
This repo contains the code and the pre-computed saliency maps used in our paper: "EML-NET: An Expandable Multi-Layer NETwork for saliency prediction". It has shown that visual saliency relies on objectness within an image, but this may also limit the performance when there is no (known) objects. Our work attempts to broaden the horizon of a saliency model by introducing more types prior knowledge in an efficient way, deeper model architectures, e.g., NasNet can be applied in an "almost" end-to-end fashion. You can also try our modified combined loss funciton as a plug-in to see how it works in your saliency system. 

<img src="https://github.com/SenJia/EML-NET-Saliency/blob/master/examples/EMLNET.jpg" width="80%">

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
