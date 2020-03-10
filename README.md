
<center><img src='./imgs/logo.png' width="440" height="150"></center><br>

  


# DO Not Touch your face (DONT)

DONT(R) was developed to overcome 2019 pandemic of SARS-CoV-2 in the world by MI2RL@Asan Medical Center, South Korea  



## NEWS: Ver.0.2 Release !

* Boost up accuracy of action recognition  
* Fixed minor bugs  
  

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



## Quick Guide

* GUI program can be run using

  ```bash
  $ python main.py
  ```



* GUI Window  

  <center><img src='./imgs/GUI.png' width="500" height="139"></center><br>
  * Run/pause the classifier by '시작'/'중지' button
    * Action classifier's result will be shown 
  * Change configuration by '설정' button (To be updated)
  * View web-cam image by '카메라' button  
   
  


## Further details

* Rationale
    * A Study Quantifying the Hand-to-Face Contact Rate and Its Potential Application to Predicting Respiratory Tract Infection (https://www.tandfonline.com/doi/full/10.1080/15459620802003896)
    * Controlling the novel A (H1N1) influenza virus: don't touch your face! (https://www.journalofhospitalinfection.com/article/S0195-6701(09)00255-2/abstract)
    * Hand Hygiene Practices in a Neonatal Intensive Care Unit: A Multimodal Intervention and Impact on Nosocomial Infection (https://pediatrics.aappublications.org/content/114/5/e565.short)   
      


* Datasets
    * To make training data, [MI2RL](https://www.mi2rl.co/) researchers and professors obtain a total of 190,000 images
    * Recording at approximately 10 different locations   
      
    
* Network
    * I3D Network (https://github.com/deepmind/kinetics-i3d)   
      

* Our pretrained weight in weights folder.

  