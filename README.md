# CSLEE 최종 프로젝트
ANTI-TBML(서류기반 자금세탁 방지 프로젝트)

![슬라이드2](https://user-images.githubusercontent.com/83098550/143228533-6c930707-807d-4131-95e2-753b24bf7bac.JPG)

무역 서류 내의 글자를 인식, 탐지하여 제재 목록과 비교하여 자금세탁 위험 여부 파악

# 목차
1. 프로젝트 개요
2. Anti-TBML 소개
3. 기술 & 화면 소개
4. 향후 기대효과

# 1) 프로젝트 개요
## anti-TBML 이란?
![슬라이드5](https://user-images.githubusercontent.com/83098550/143228542-ad0d874d-ffff-47f8-b21c-740c4c6654d4.JPG)

## 추진 배경 및 필요성
![슬라이드6](https://user-images.githubusercontent.com/83098550/143228546-9453d4c6-2e97-4594-a5f2-ffb7714d30f9.JPG)

## 프로젝트 목표
![슬라이드7](https://user-images.githubusercontent.com/83098550/143228549-de7defce-92bd-4376-8620-e6548588ba7c.JPG)

# 2) 프로젝트 소개
## 개발 일정
![슬라이드8](https://user-images.githubusercontent.com/83098550/143228550-c0b4e7d4-aef7-413f-898f-00fef7edd88b.JPG)

## 개발 환경
![슬라이드9](https://user-images.githubusercontent.com/83098550/143228552-eaff48b4-656b-490c-ba98-2f97a457d62f.JPG)

## 시스템 구성도
![슬라이드10](https://user-images.githubusercontent.com/83098550/143228553-12d04edc-4f3b-4643-9136-9fffd9c5cda2.JPG)

## 최종 결과물
![슬라이드11](https://user-images.githubusercontent.com/83098550/143228554-d0b7c710-9d4f-45e3-9ea6-2bcf219a7395.JPG)
![슬라이드12](https://user-images.githubusercontent.com/83098550/143228555-bc966605-de2f-4214-b9d5-207c768da5ec.JPG)

# 3) 기술 & 화면 소개
## 데이터 라벨링
![슬라이드13](https://user-images.githubusercontent.com/83098550/143228557-c0c8957e-ea59-48e7-8eff-c3cff13a3ae1.JPG)

## 데이터 augmentation
![슬라이드14](https://user-images.githubusercontent.com/83098550/143228559-4ba1c467-c132-4606-ba00-c80da85b7b1b.JPG)

## AI 모델링
![슬라이드15](https://user-images.githubusercontent.com/83098550/143228560-1a5739d3-3131-4081-b0f5-4862a14f905d.JPG)

1. Detection – Faster RCNN
![슬라이드16](https://user-images.githubusercontent.com/83098550/143228563-2bc921c3-17af-4e4d-b633-f5404b7649b6.JPG)

2. Recognition - CRNN
![슬라이드17](https://user-images.githubusercontent.com/83098550/143228572-b9221bca-b91b-4f59-99d8-cf1e68a115a1.JPG)

## NLP
단어 -> 문장화
![슬라이드18](https://user-images.githubusercontent.com/83098550/143228574-f6edd784-7a50-48c6-8e92-233ddadcf0bd.JPG)
![슬라이드19](https://user-images.githubusercontent.com/83098550/143228575-e776994e-ef2f-4683-b5af-35263334d866.JPG)
![슬라이드20](https://user-images.githubusercontent.com/83098550/143228577-530e47c3-5bd7-40e2-8a7e-607e2d42a625.JPG)

## 데이터 베이스
![슬라이드21](https://user-images.githubusercontent.com/83098550/143223751-7e0e8508-5690-4de0-ae03-6b0173ae347c.JPG)

## 서비스 시연
[![service](https://img.youtube.com/vi/uvQJeMt1odk/0.jpg)](https://www.youtube.com/watch?v=uvQJeMt1odk)

# 4) 프로젝트 향후 계획
## 배운점
### TEXT recognition
![슬라이드23](https://user-images.githubusercontent.com/83098550/143228578-dfca8319-de86-4d35-b867-2c5b28e91681.JPG)

### NLP
![슬라이드24](https://user-images.githubusercontent.com/83098550/143228580-22d4d3ca-19cd-45ac-94e3-905dc487ec59.JPG)

## 향후계획
1. Sanction list의 텍스트를 augmentation 하고 학습시킨 후 
   text recognition의 정확도를 높인다.
2. 여러 줄의 문장도 하나의 문장으로 인식되도록 최적화 시킨다
3. 사용자 친화적으로 시스템을 개선한다.

### 팀소개
![슬라이드26](https://user-images.githubusercontent.com/83098550/143223755-e49f3225-c0e8-45fd-b9c0-7590b78764e9.JPG)
