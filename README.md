# Keras-RetinaNet Custom Object Detection

## Installation process of keras-Retinanet
* Download the Keras-Retinanet source from https://github.com/fizyr/keras-retinanet
* Install Tensorflow > 2.3.0. In my case I have Tensorflow 2.3.1
* Execute ```pip3 install . –user```.
* To compile Cython code run ```python setup.py build_ext –inplace```

## Test Keras-Retinanet using pre trained model
* Download pre-trained model of Keras-Retinanet from ```https://github.com/fizyr/keras-retinanet/releases``` and save it to snapshots folder.
* Go to examples folder and open ‘’’ resnet50_retinanet.py```  and confirm your downloaded model name in ```model_path = os.path.join('..', 'snapshots', 'resnet50_coco_best_v2.1.0.h5')```.
* After confirmation run ```python resnet50_retinanet.py```. If it runs successfully, congratulation you have successfully installed  Keras-Retinanet.
* If there is an compute_overlap error 
```
File “..\keras_retinanet\utils\anchors.py”, line 20, in <module> 
from ..utils.compute_overlap import compute_overlap
ImportError: DLL load failed while importing compute_overlap
```
Than open “keras_retinanet\utils\ anchors.py” in your editor and edit
``` 
from ..utils.compute_overlap import compute_overlap
``` 
to 
``` 
from compute_overlap import compute_overlap
```
This will solve the error of cumpute_overlap.

## Train our custom dataset using keras-Retinanet
* Step1 : Prepare Dataset
* Step2 : Labelling/Annotation
* Step3 : Train
* Step4 : Test

### Prepare Dataset
First, you need to define what object you want to detect. In this example i have used "racoon" images to train.[https://public.roboflow.com/object-detection/raccoon]. 
Copy all your images in
“dataset/JPEGImages” folder. 

### Labelling/Annotation
The next step is to Label/annotate the dataset according to respective class. In this case there is only one class : "raccoon".
I used labelImg from https://github.com/tzutalin/labelImg. It is a graphical image annotation tool written in Python and it uses Qt for its graphical interface.
**In labelImg confirm the save directory of “.xml” file to “dataset/Annotations” folder.**

![labelimg](https://user-images.githubusercontent.com/20577227/114542661-259b6a80-9c93-11eb-8e3c-f7d3c53fe7c8.JPG)

I have used PASCAL VOC format since it is supported by Keras-Retinanet.

Images are in **“dataset/JPEGImages”**

XML file are in **“dataset/Annotations”**

Divide the whole dataset into training and validation

Open/Run **“train_val_divide.py”** in and enter your desired percentage_val default is **“percentage_val = 10;”** . This will save **“train.txt”** and **“val.txt”** in directory **“ImageSets/Main/”**

Directory Structure of dataset
```
+---dataset
|   |   train_val_divide.py
|   |   
|   +---Annotations
|   |       raccoon-1.xml
|   |       raccoon-10.xml
|   |       raccoon-100.xml
|   |       …
|   +---ImageSets
|   |   \---Main
|   |           train.txt
|   |           val.txt
|   |           
|   \---JPEGImages
|           raccoon-1.jpg
|           raccoon-10.jpg
|           raccoon-100.jpg
|           …

```

**Define the classes to "keras_retinanet/preprocessing/pascal_voc.py"**
Default is 
```
voc_classes = {
    'aeroplane'   : 0,
    'bicycle'     : 1,
    'bird'        : 2,
    'boat'        : 3,
    'bottle'      : 4,
    'bus'         : 5,
    'car'         : 6,
    'cat'         : 7,
    'chair'       : 8,
    'cow'         : 9,
    'diningtable' : 10,
    'dog'         : 11,
    'horse'       : 12,
    'motorbike'   : 13,
    'person'      : 14,
    'pottedplant' : 15,
    'sheep'       : 16,
    'sofa'        : 17,
    'train'       : 18,
    'tvmonitor'   : 19
}
```

**Changed to** 
```
voc_classes = {
    'raccoon'   : 0
    
}
```
**Because i have only one class**

### Train
```
python keras_retinanet/bin/train.py --weights snapshots/resnet50_coco_best_v2.1.0.h5 --steps 1000 --epochs 10 --snapshot-path snapshots --tensorboard-dir tensorboard pascal dataset
```
--weights -> Initialize the model with weights from a file

--steps -> Number of steps per epoch

--Epochs -> Number of epochs to train

--snapshot-path -> Path to store snapshots of models during training

--tensorboard-dir -> Log directory for Tensorboard output

Pascal -> Directory of our dataset

### Test
To test our trained model, first we need to convert it from training format to test format.
```
python keras_retinanet/bin/convert_model.py snapshots/resnet50_pascal_01.h5 directory_to_save_test_model.h5
```
Now we can this Saved model for our object detection.
** You can use "examples/resnet50_retinanet.py" to test the trained model


**Ref {"https://github.com/fizyr/keras-retinanet"] 
