# 아이들의 위한 재난 안전 AI Speaker : 폼페이

### 경희대학교 소프트웨어 해커톤 KHUTHON

<p align=center><img width="500"src = "../../../Pompeii/blob/main/images/main.png"></p>

<br>

## 폼페이 주요 기능

### 재난 안전 퀴즈

_하이, 폼페이. 퀴즈 내 줘!_<br>
폼페이와 함께하는 재나 안전 퀴즈를 통해 어린이들이 재미있게 재난행동요령을 습득할 수 있습니다. <br>
폼페이의 재난행동요령 데이터는 [국민재난안전포털](https://www.safekorea.go.kr/idsiSFK/neo/main/main.html)에 기반합니다.

### 재난 관련 뉴스 및 정보 제공

폼페이는 재난관련 최신 뉴스를 제공합니다.

### 유저 인터페이스

웹을 통해 폼페이와의 대화를 실시간으로 확인할 수 있습니다. <br>

<p align=center><img width="900" src = "../../../Pompeii/blob/main/images/interface.gif"></p>

<img  width =100% />

## 폼페이 아키텍쳐 및 핵심 기술
<p align=center><img width="600" src = "../../../Pompeii/blob/main/images/architecture.png"></p>

### Sentence Embedding

- 사용자 답변과 모범 답안의 유사도 분석을 통해 퀴즈 정답 여부를 확인합니다. 
- https://github.com/BM-K/KoSentenceBERT_SKT

### Google Speech API

- Speech To Text
- Text To Speech

## 시연 영상

### 1. 폼페이 퀴즈 시연 영상

https://youtu.be/2uDQohrjnSs

### 2. 폼페이 뉴스 시연 영상

https://youtu.be/LzjoqNt_1J0
