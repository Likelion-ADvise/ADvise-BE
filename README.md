
# 멋쟁이 사자처럼 해커톤
멋쟁이 사자처럼 해커톤에서 사용한 서버코드입니다. Django를 사용하여 구현하였습니다.

## 👨‍🏫 프로젝트 소개
**ADvise**는 광고 역경매 서비스로, 업체들이 광고를 제시하면 인플루언서 / 광고사들이 역경매로 가격을 제시하여 합리적인 가격으로 광고를 할 수 있게 도와주는 서비스입니다.

## ⏲️ 개발 기간
* 2024.06.25(화) ~ 2024.07.06(금)
  * 아이디어 제시
  * 와이어프레임 작성
  * 프론트와 협업

## 🧑‍🤝‍🧑 개발자 소개
* 김민경
* 최우진

## ⚙️ 기술 스택
* Server: AWS EC2
* WS/WAS: Nginx
* 아이디어 회의: Notion
* [Notion 링크](https://www.notion.so/5c39c682496f45569c76f5d9950a82c8)

## 📌 주요 기능
* 광고 작성
  * 광고내용, 사진, 가격 등을 설정하여 광고를 제시할 수 있게 한다.
* 광고 검색
  * 광고 제목을 검색하면 제목과 일치하는 광고 게시글을 찾을 수 있다.
* 댓글 작성
  * 광고 게시글에 댓글을 통해서 자신의 포트폴리오와 가격을 제시한다.
* 댓글 조회
  * 조회를 통해서 해당 광고 게시글에 몇 명이 가격을 제시했는지 볼 수 있다.
* 댓글 삭제
  * 비밀번호를 입력하여 자신이 작성한 댓글을 삭제할 수 있다.

## ✒️ API
| 기능                  | method  | 주소                                                |
|-----------------------|---------|---------------------------------------------------------|
| 전체 게시물 조회     | get     | https://advise.kro.kr/dutch/                         |
| 게시물 작성           | post    | https://advise.kro.kr/dutch/ads/                         |
| 특정 광고 조회        | get     | https://advise.kro.kr/dutch/ads/<int:pk>/                |
| 검색어 게시물 조회   | get     | https://advise.kro.kr/dutch/ads/search?q=검색어/         |
| 댓글 작성            | post    | https://advise.kro.kr/dutch/ads/<intad_id>/proposals/   |
| 댓글 조회            | get     | https://advise.kro.kr/dutch/ads/<intad_id>/proposals/all/|
| 댓글 삭제            | delete  | https://advise.kro.kr/dutch/ads/<intad_id>/proposals/<intpk>/delete/ |

## ERD CLOUD
![image](https://github.com/Likelion-ADvise/ADvise-BE/assets/131441769/d1386430-c0b6-4c6c-8b8c-c211da8c323f)

