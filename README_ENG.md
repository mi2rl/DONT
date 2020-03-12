<div style="width:40px;height:30px;float:right;">
    <p align="right"><a href="https://github.com/mi2rl/DONT/blob/master/README_ENG.md"><img src='./imgs/america.png' width="40" height="30"></a></p>
</div>
<div style="width:40px;height:30px;float:right;">
    <p align="right"><a href="https://github.com/mi2rl/DONT/blob/master/README.md"><img src='./imgs/korea.png' width="40" height="30"></a></p>
</div>

<p align="center"><img src='./imgs/MI2RL_logo.png' width="440" height="150"></p>
<br>

# DO Not Touch your face (DONT)

* Download link (execution file)  : https://drive.google.com/open?id=1owgC56KuQbNRNkF3gEJ7_52jhjeLmqFV
* DONT(R) was developed to overcome 2019 pandemic of SARS-CoV-2 in the world by MI2RL@Asan Medical Center, South Korea  
* Pretrained network is available (weights folder)  
* Video demo  : https://youtu.be/Yn7jqsNAmNk

<br>



## NEWS (20.03.12) : ver.0.2.1

* Release the execution file for window 

* Fixed minor bugs  (thread issue)

* TO DO:

  * Support Korean/English language in GUI

  * Writing paper

    

<br>

## Installation

```bash
# Clone this repository
$ git clone https://github.com/mi2rl/DONT.git

# Make virtual environment
$ conda create -n [your virtual environment name] python3

# Activate virtual environment
$ conda activate fta_gpu

# Install requirements
$ pip install torch==1.2.0+cu92 torchvision==0.4.0+cu92 -f https://download.pytorch.org/whl/torch_stable.html

$ pip install -r requirements.txt
```

  <br>


## Quick Guide

* GUI program can be run using

  ```bash
  $ python main.py
  ```



* GUI Window  

  <p align="center"><img src='./imgs/GUI.png' width="500" height="139"></p><br>  
* Run/pause the classifier by '시작'/'중지' button
  
  * Action classifier's result will be shown 
  
* Change configuration by '설정' button (To be updated)
* View web-cam image by '카메라' button   

<br>


## Further details

* **Rationale**
    * A Study Quantifying the Hand-to-Face Contact Rate and Its Potential Application to Predicting Respiratory Tract Infection (https://www.tandfonline.com/doi/full/10.1080/15459620802003896)
    * Controlling the novel A (H1N1) influenza virus: don't touch your face! (https://www.journalofhospitalinfection.com/article/S0195-6701(09)00255-2/abstract)
    * Hand Hygiene Practices in a Neonatal Intensive Care Unit: A Multimodal Intervention and Impact on Nosocomial Infection (https://pediatrics.aappublications.org/content/114/5/e565.short)  
      


* **Datasets**
  
    * To make training data, [MI2RL](https://www.mi2rl.co/) researchers and professors obtain a total of 190,000 images
    * Recording at approximately 10 different locations  
    * Action classes : 11 classes 
      * Overall classes : drinking, picking up phone, removing mask, resting chin on hand, rubbing eyes, touching glasses, touching hairs, touching keyboard, touching nose, touching phone, wearing mask
      * Touching classes : picking up phone, resting chin on hand, rubbing eyes, touching hairs, touching nose
        
    
* **Action Classification Network**
  * I3D Network (https://github.com/deepmind/kinetics-i3d)   
    * Training phase
        * The number of  frames in each stack for 3D CNN : 16
        * Data augmentation
          * Step in frames between each clip : 4
          * Color distortion
          * Rotation
        
    * Inference Phase
      * The number of  frames in each stack for 3D CNN : 24
        
  
* **H/W specification**

    * Test specification.
      
      * GPU : Geforce GTX 960 4GB
        * CPU : Intel(R) Core i7-6700 CPU 3.40GHz 
        * OS : Linux Ubuntu 18.04
        * Inference
        
          * 0.07~0.085 sec on GPU
          * 1.4~1.5 sec on CPU
          * CPU usage  ≈ 35%  
          * GPU memory usage ≈  1.1GB
            
      
    * Minimum specification


      * GPU : Geforce GTX 960 4GB
      * CPU : Intel(R) Core i7-6700 CPU 3.40GHz 
      * OS : Linux / Windows  


<br>

## Experiment Results

**Confusion matrix : binary-class**
<br>

<p align="center"><img src='./imgs/result_confusion_binary.png' width="400" height="400"></p><br>
## Limitations

* DONT began at 2020.03.05, and has been in the works for about a week. We decided that it would be more desirable to call for joint efforts through faster release than creating high-performance programs, so we decided to proceed with the disclosure despite the lack of progress.

<br>



## Contact for Data Donation 

* For more robust DONT, we need more data from different environments and persons. 
  If you want to donate your data, please send it to namkugkim@gmail.com. Your privacy will be protected, as strong as possible.



### Guideline for data donation

* Please take a video and send it to the e-mail address above.
* Recording process is as follows.
  * Wearing mask -> (With a mask) -> Touching nose -> Resting chin on hand -> Rubbing eyes -> Touching hairs -> Drinking water-> Touching phone -> Picking up phone -> Touching keyboard -> (Without a mask) -> Touching nose -> Resting chin on hand -> Rubbing eyes -> Touching hairs -> Drinking water-> Touching phone -> Picking up phone -> Touching keyboard
  * Moderate video recording time is about 90 seconds.
  * Example : [Gudieline for video recording](https://youtu.be/NU5FlHp6Qgg)

