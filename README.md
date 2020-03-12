<div style="width:40px;height:30px;float:left;">
    <p align="left"><a href="https://github.com/mi2rl/DONT/blob/master/README_ENG.md"><img src='./imgs/america.png' width="40" height="30"></a></p>
</div>
<div style="width:40px;height:30px;float:left;">
    <p align="left"><a href="https://github.com/mi2rl/DONT/blob/master/README.md"><img src='./imgs/korea.png' width="40" height="30"></a></p>
</div>

<br>

<p align="center"><img src='./imgs/MI2RL_logo.png' width="440" height="150"></p>
<br>

# 얼굴을 만지지 마세요 (DO Not Touch your face, DONT)

* 이 프로그램은 세계적으로 대유행인 코로나-19(SARS-CoV-2)를 극복하기 위해 서울아산병원의 MI2RL 연구실에서 개발하였습니다.  
* 사전학습된 신경망이 weights 폴더에 업로드 되어있습니다. 
* 비디오 데모  : https://youtu.be/Yn7jqsNAmNk

<br>

## 뉴스 (20.03.11) : ver.0.2 가 배포되었습니다. 

* 행동 인식 성능이 향상되었습니다. 

* 약간의 버그를 수정하였습니다. 

* 해야할일 (TO DO):

  * 사용의 편의성을 위하여 실행파일(.exe, .deb) 을 배포할 예정입니다. 

  * 영어버전의 GUI를 개발할 예정입니다. 

  * '설정' 메뉴를 추가할 예정입니다.
  
  * 관련 논문을 작성할 예정입니다. 
  
    

<br>

## 설치방법

```bash
# Github 에서 Clone 해줍니다.
$ git clone https://github.com/mi2rl/DONT.git

# 가상환경을 만들어줍니다. 
$ conda create -n [your virtual environment name] python3

# 가상환경을 활성화 시킵니다.
$ conda activate fta_gpu

# 코드 실행에 필요한 파일들을 설치합니다. 
$ pip install torch==1.2.0+cu92 torchvision==0.4.0+cu92 -f https://download.pytorch.org/whl/torch_stable.html

$ pip install -r requirements.txt
```

  <br>


## 설명서

* GUI 프로그램은 아래 명령으로 실행시킬 수 있습니다. 

  ```bash
  $ python main.py
  ```



* GUI 화면

  <p align="center"><img src='./imgs/GUI.png' width="500" height="139"></p><br>  
* '시작'/'중지' 버튼을 눌러 행동 인식 기능을 키고/끄고 할 수 있습니다. 
  
  * 행동 인식 결과는 '알림: ' 에 표시됩니다. 
  
* '설정' 버튼을 눌러 기능을 설정할 수 있습니다. (이 부분은 추후에 업데이트 될 예정입니다)
* '카메라' 버튼을 누르면, 웹캠의 영상을 확인할 수 있습니다. 

<br>


## 세부사항

* **타당성/합리성(Rationale)**
    * A Study Quantifying the Hand-to-Face Contact Rate and Its Potential Application to Predicting Respiratory Tract Infection (https://www.tandfonline.com/doi/full/10.1080/15459620802003896)
    * Controlling the novel A (H1N1) influenza virus: don't touch your face! (https://www.journalofhospitalinfection.com/article/S0195-6701(09)00255-2/abstract)
    * Hand Hygiene Practices in a Neonatal Intensive Care Unit: A Multimodal Intervention and Impact on Nosocomial Infection (https://pediatrics.aappublications.org/content/114/5/e565.short)  
      


* **데이터**
  * [MI2RL](https://mi2rl.co)의 연구자 및 교수의 영상을 촬영하여 약 190,000장의 학습 데이터를 만들었습니다. 
    * 다양한 환경 구성을 위하여 서로 다른 10개의 장소에서 촬영하였습니다.  
    * 행동 종류 : 11 가지
      * 전체 행동 종류 : 물 마시기, 전화 받기, 마스크 벗기, 턱 괴기, 눈 비비기, 안경 만지기, 머리 만지기, 키보드 만지기, 코 만지기, 마스크 쓰기
      * 얼굴을 만지는 행동 : 전화 받기, 턱 괴기, 눈 비비기, 머리 만지기, 코 만지기
  
* **Action Classification Network**
  * I3D Network (https://github.com/deepmind/kinetics-i3d)   
    * 학습과정
        * 3D CNN에서 사용되는 스택당 이미지 갯수 : 16
        * 데이터 증강 (Data augmentation)
          * 클립 사이의 프레임 간격 : 4
          * 색상 왜곡
          * 임의 회전
        
    * 추론과정
      * 3D CNN에서 사용되는 스택당 이미지 갯수 : 24
  
* **하드웨어 환경**

    * 테스트 환경
      
      * GPU : Geforce GTX 960 4GB
        * CPU : Intel(R) Core i7-6700 CPU 3.40GHz 
        * OS : Linux Ubuntu 18.04
        * 추론 속도 및 자원 사용
        
          * 0.07~0.085 sec on GPU
          * 1.4~1.5 sec on CPU
          * CPU usage  ≈ 35%  
          * GPU memory usage ≈  1.1GB
            
      
    * 최소사양


      * GPU : Geforce GTX 960 4GB
      * CPU : Intel(R) Core i7-6700 CPU 3.40GHz 
      * OS : Linux / Windows  


<br>

## 실험결과

**Confusion matrix : 이진 분류 (얼굴 만지기/안만지기)**
<br>

<p align="center"><img src='./imgs/result_confusion_binary.png' width="400" height="400"></p><br>
## 추가 데이터를 부탁 드립니다. 

* 행동 인식 신경망의 정확도를 높이기 위하여, 조금 더 다양한 환경의 데이터가 필요합니다. 
  당신의 데이터는 보호될 예정이며, namkugkim@gmail.com 으로 보내주시면 감사드리겠습니다. 

