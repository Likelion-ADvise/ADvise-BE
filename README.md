
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
#1. 광고 게시물 작성
  * 광고를 진행하고자 하는 업체가 웹에 자신의 게시물을 올릴 수 있다.
    ![image](https://github.com/Likelion-ADvise/ADvise-BE/assets/149250433/7fde9b5f-db42-471a-ae8d-93b5f22cd414)
    post 요청을 통해 title, content, minimum_price(최저 가격) 을 입력받아 정해진 양식에 맞게 입력시 광고 게시물을 업로드할 수 있도록 한다.
    만약 양식이 다름 등의 이유로 실패할 시 400 에러를 띄우도록 한다.





#2. 모든 광고 게시물 조회
  * 메인화면에 띄울 기능으로, 생성된 모든 광고 게시물을 불러온다.
    ![image](https://github.com/Likelion-ADvise/ADvise-BE/assets/149250433/7c81bca6-4268-44fa-8f5e-7010c031fe59)
    get 요청을 통해 메인에 띄워질 게시물의 정보들을 불러와 원하는 입력값들만 모든 광고 게시물에서 가져올 수 있도록 한다.





#3. 특정 광고 게시물 조회
  * 사용자가 메인화면에서 특정 광고를 클릭할 시, 해당 광고 게시물을 불러온다.
    ![image](https://github.com/Likelion-ADvise/ADvise-BE/assets/149250433/c8e3e230-e39b-4352-92af-419a37ee0cec)
    get 요청을 통해 조회하려고 하는 광고 게시물의 pk 가 일치하는지 확인 후, 해당하는 게시물의 정보를 가져올 수 있도록 한다.
    만약 pk가 존재하지 않음 등의 이유로 실패할 시 404 에러를 띄우도록 한다.




   
#4. 광고 검색
  * 원하는 키워드를 가지고 검색할 시, 해당 키워드가 제목에 존재하는 모든 게시물들의 정보를 가져올 수 있도록 한다.
    ![image](https://github.com/Likelion-ADvise/ADvise-BE/assets/149250433/6fedf3fe-9859-4f29-a23e-f2d05c8906e6)
    get 요청을 통해 사용자가 원하는 검색어를 쿼리로 받아 title__icontains 변수를 이용해 오직 제목에 검색어가 존재하는 게시물들의 정보를 가져올 수 있도록 한다.
    불러오는 게시물들을 정보를 특정해 원하는 입력값들만 검색창에 띄워질 수 있도록 한다.





#5. 댓글 작성
  * 업체가 업로드한 광고 게시물에 희망하는 인플루언서가 정해진 입력값을 입력 후 댓글을 단다.
    ![image](https://github.com/Likelion-ADvise/ADvise-BE/assets/149250433/760120b0-ccbb-4630-bd43-54250de55d9e)
    post 요청을 통해 사용자가 댓글을 작성하고자 원하는 게시물의 ad_id 값을 확인 후 해당 ad_id가 존재할 시 사용자가 정해진 입력값에 맞춰 정보를 전송하면 댓글을 게시할 수 있도록 한다.
    만약 ad_id가 존재하지 않음 등의 이유로 실패할 시 404 에러를 띄우도록 한다.





#6. 모든 댓글 조회
  * 업체가 업로드한 광고 게시물에 작성된 모든 댓글들을 불러온다.
    ![image](https://github.com/Likelion-ADvise/ADvise-BE/assets/149250433/61503c56-12fa-4677-ab1c-74594a234a96)
    get 요청을 통해 불러오고자 하는 광고 게시물의 id 값을 확인후 해당 id 에 있는 모든 댓글 data를 불러올 수 있도록 한다.
    만약 광고 게시물의 id 값이 존재하지 않음 등의 이유로 실패할 시 404 에러를 띄우도록 한다. 






#7. 특정 댓글 삭제
  * 광고 게시물에 작성한 인플루언서의 댓글을 삭제한다.
    ![image](https://github.com/Likelion-ADvise/ADvise-BE/assets/149250433/a26ec9ed-490d-4b91-9abc-e71b5c25408a)
    delete 요청을 통해 삭제하고자 하는 광고게시물의 id 과 해당 댓글의 id를 확인 후 일치하는 댓글의 data를 불러온다.
    이후 일치한 댓글의 data와 delete 요청에서 전송한 data 값이 일치할 시 해당 댓글의 삭제가 가능하다.
    만약 delete 요청에서 전송한 data의 pwd 값과 댓글의 pwd 가 일치하지 않을 시 403 에러를 띄우고, 삭제가 완료될 시 200 코드와 'id: {pk} 제안 삭제 완료' 를 띄운다.






## ✒️ API
| 기능                        | method  | REST API                                                                 | 입력 data                 | 반환 data |
|-----------------------------|---------|--------------------------------------------------------------------------|---------------------------|-----------------------|
| 전체 게시물 조회             | get     | https://advise.kro.kr/dutch/                                             |          | 성공:200,ok 실패 : 500 |
| 게시물 작성                  | post    | https://advise.kro.kr/dutch/ads/                                         | {“title”:varchar(100),“content”:text,“minimum_price”:int,“image”:image}| 성공:200 ok, 실패 : 400 |
| 특정 광고 조회               | get     | https://advise.kro.kr/dutch/ads/<int:pk>/                                |         | 성공 : 200, ok 실패 : 404 |
| 검색어 게시물 조회           | get     | https://advise.kro.kr/dutch/ads/search?q=검색어/                         |          | 성공 : 200, ok 실패 : 500 |
| 댓글 작성                   | post    | https://advise.kro.kr/dutch/ads/<intad_id>/proposals/                     |{“identifier”:varchar(100),“pwd”:varchar(100),“title”:varchar(100),“url”:url,“info”:text,“price”:int} | 성공 : 200, ok 실패 : 400 |
| 모든 댓글 조회              | get     | https://advise.kro.kr/dutch/ads/<intad_id>/proposals/all/                 |         | 성공 : 200, 실패 : 404|
| 댓글 삭제                   | delete  | https://advise.kro.kr/dutch/ads/<intad_id>/proposals/<intpk>/delete/      |{“id”:<int:ad_id>,“identifier”:varchar(100),“pwd”:varchar(100),“title”:varchar(100),“url”:url,“info”:text,“price”:int}| 성공 : 200, ok 실패 : 400, 403 (일치 오류) |







## ERD CLOUD
![image](https://github.com/Likelion-ADvise/ADvise-BE/assets/131441769/d1386430-c0b6-4c6c-8b8c-c211da8c323f)

