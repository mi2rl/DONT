<div style="width:40px;height:30px;float:right;">
    <p align="right"><a href="https://github.com/mi2rl/DONT/blob/master/README_ENG.md"><img src='./imgs/america.png' width="40" height="30"></a></p>
</div>
<div style="width:40px;height:30px;float:right;">
    <p align="right"><a href="https://github.com/mi2rl/DONT/blob/master/README.md"><img src='./imgs/korea.png' width="40" height="30"></a></p>
</div>

<br>

<p align="center"><img src='./imgs/MI2RL_logo.png' width="440" height="150"></p>
<br>

# 얼굴을 만지지 마세요 (DO Not Touch your face, DONT)

* 실행파일 다운로드 링크 : 
* 이 프로그램은 세계적으로 대유행인 코로나-19(SARS-CoV-2)를 극복하기 위해 서울아산병원의 MI2RL 연구실에서 개발하였습니다.  
* 사전학습된 신경망이 weights 폴더에 업로드 되어있습니다. 
* 비디오 데모  : https://youtu.be/Yn7jqsNAmNk



### 한계점

* 이 프로젝트는 2020.03.05 부터 시작되어, 약 1주일 동안 진행되었습니다. **높은 성능의 프로그램을 만드는 것 보다 빠른 배포를 통한 공동의 노력을 촉구하는 것이 코로나-19 확산 방지를 위하여 더 바람직**할 것으로 판단하여, 아직 부족함에도 불구하고 프로그램 배포를 진행하게 되었습니다. 
* 높은 성능을 위해서는 많은 데이터 확보가 필요합니다. [이곳](#추가-데이터를-부탁드립니다) 을 참조하시어, 데이터를 기부해 주신다면 감사드리겠습니다. 



<br>

## 뉴스 (20.03.12) : ver.0.2.1 

* 윈도우용 실행파일이 배포되었습니다. 

* 약간의 버그가 수정되었습니다. (쓰레드 종료 이슈)

* 해야할일 (TO DO):

  * GUI에서 한글/영어를 지원할 예정입니다. 

  * 관련 논문을 작성할 예정입니다. 

    

<br>

## 설치방법

```bash
# Github 에서 Clone 해줍니다.
$ git clone https://github.com/mi2rl/DONT.git

# 가상환경을 만들어줍니다. 
$ conda create -n [your virtual environment name] python3

# 가상환경을 활성화 시킵니다.
$ conda activate [your virtual environment name]

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
## * 추가 데이터를 부탁드립니다 *

행동 인식 신경망의 정확도를 높이기 위하여, 조금 더 다양한 환경과 많은 사람의 데이터가 필요합니다. 
당신의 데이터 강력하게 보호 될 예정입니다. 데이터는 dev.sungman@gmail.com 또는 minjeekim00@gmail.com 으로 보내주시면 감사드리겠습니다. 



### 동영상 촬영 가이드라인

* 동영상 촬영 순서는 다음과 같습니다. 
  * 마스크 쓰기 -> (마스크를 착용한 상태에서) -> 코 만지기 -> 턱 괴기 -> 눈 비비기 -> 머리 쓸기 -> 물 마시기 -> 핸드폰 만지기 -> 전화 받기 -> 키보드 사용하기 -> (마스크를 벗은 상태에서) -> 코 만지기 -> 턱 괴기 -> 눈 비비기 -> 머리 쓸기 -> 물 마시기 -> 핸드폰 만지기 -> 전화 받기 -> 키보드 사용하기 
  * 영상의 길이는 90초 정도가 적당합니다. 
  * 예시 : [얼굴 촬영 가이드라인](https://youtu.be/NU5FlHp6Qgg )

<br>

