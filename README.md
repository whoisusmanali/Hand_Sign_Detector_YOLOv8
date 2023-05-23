# Hand Sign Detector by using YOLOv8
In this project I used my own dataset by clicking my own pictures and annotate these images by using MakeSense.com and use YOLOv8 for training and test on Vs Code.

## Demo
https://user-images.githubusercontent.com/104086680/232927683-a62eb7d3-c488-4be2-aa81-3393a0419d3c.mp4



## Libraries/Dependencies used in this project:
1. Collecting Images:<br>
    1.1. cv2<br>
    1.2. uuid<br>
    1.3. time<br>
    1.4. os<br>
2. Image Annotation:<br>
    2.1. Make Sense websit<br>
3. Training:<br>
    3.1. ultralytics<br>
    3.2. YOLO v8<br>
4. Testing using webcam:<br>
    4.1. cv2<br>
    4.2. ultralytics<br>
    4.3. numpy<br>
    4.4. math<br>





## Steps Involved:
#### 1. Data collection:<br>
    In this section I use my own dataset by clicking my own pictures with different signs from different posses. In this process I use Python Programming language use to     collect the data.
#### 2. Image Annotation:<br>
    Image annotion is also done by myself by using MakeSense.com (Make Sense) website and store label in separate files and images into separate files.<br>
    
### Screenshot while Data Annotation:
![Capture](https://user-images.githubusercontent.com/104086680/230760760-fe4b2eff-a3de-45d5-a4dd-aef0539ca951.PNG)

![Capture1](https://user-images.githubusercontent.com/104086680/230760766-bdb40240-3035-45dd-af6e-dce061c66999.PNG)
 
    
#### 3. Data spliting:<br>
    The total data which includes labels and images got divided into 3 different folders train, test and valid which is further divided into images and lebels folders.
    The split percentage is 70% , 20% and 10% respectively.
#### 4. Model training:<br>
    The model got training on Google Colab on YOLO v8 from ultralytics and good pretty much good results.<br>
    
### Sreenshots of Results:

![results (1)](https://user-images.githubusercontent.com/104086680/230760776-67096f8e-f342-40a0-ba18-8e4c940198b8.png)

![confusion_matrix (2)](https://user-images.githubusercontent.com/104086680/230760779-264b4e2a-8a3e-43c1-ac96-32e888fe2794.png)   

## Batch one working:

![train_batch0](https://user-images.githubusercontent.com/104086680/230761268-7ba4b0b7-5017-4f8e-989f-b46e7dbd0901.jpg)

#### 5. Testing:<br>
    The testing of the model is completly done on PyCharms with Using different libraries and run on completely by using my own webcam. And try to detect the objects.
### Screenshots of labels and Confidence Level:
![Labels and Confidence score prediction](https://user-images.githubusercontent.com/104086680/230761258-7394b3c9-25ec-4469-a26f-3e74d482bf0d.jpg)


   
