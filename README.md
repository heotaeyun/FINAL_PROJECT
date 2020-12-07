# Final PJT



> 요약 : 본 프로젝트는 SSAFY 교육을 통해 배운 프로그램언어, 웹 프레임워크를 활용하여 `영화 정보 기반 추천 서비스`를 구성하는 프로젝트이다.
>
> 이에 따라, `HTML`, `CSS`, `JavaScript`, `Vue.js`, `Django`, `REST API`, `DataBase` 등을 활용하여 실제 서비스를 설계하고 구현하였다.

## 1. 진행 기간

- 2020.11.19 ~ 2020.11.27



## 2.  팀원 정보 및 업무 분담 내역

- 팀원 : 허태윤, 한승엽
- 업무 분담
  - 허태윤 : `Front-end`, `HTML/CSS`
  - 한승엽 : `Back-end`, `DataBse`



## 3. 목표 서비스 구현 및 실제 구현 정도

- 실제 영화 추천 서비스와 유사하게 구현하고자 노력하였으나 안되는 부분이 발생함.
- 구현 한 부분
  - 회원 가입 / 회원탈퇴
  - 로그인 / 로그아웃
  - 장르별 영화 소개
  - 유투브 API 연결을 통한 예고편 보여주기
- 구현 못 한 부분
  - 서버 배포
  - 이메일 인증 후 회원가입
  - `Lazy Loading`

## 4. ERD

![image-20201126160238448](C:\Users\taeyun\AppData\Roaming\Typora\typora-user-images\image-20201126160238448.png)



## 5. 필수 기능

### 5-1. 관리자 뷰

- Django에서 제공하는 기본 관리자 폼을 커스터마이징 하여 구현하였다.

  ```django
  accounts/admin.py
  
  from django.contrib import admin
  from django.contrib import admin
  from django.contrib.auth.admin import UserAdmin
  
  from .models import User
  
  admin.site.register(User, UserAdmin)
  ```

  ```
  community/admin.py
  
  from django.contrib import admin
  from .models import Review, Comment
  
  admin.site.register(Review)
  admin.site.register(Comment)
  ```

  

### 5-2. 영화 정보

- 데이터베이스는 `TMDB`에서 제공하는 `API`를 요청해서 현재 상영되는 영화 85개를 데이터베이스에 저장함.



### 5-3. 추천 알고리즘

- `USER`는 장르 18개 중 2개를 선택하여 추천 영화를 선택 받을 수 있다.
- 예를들어, 액션 & 범죄 장르를 선택할 경우 액션 & 범죄가 동시에 포함되는 영화를 선택하신 항목과 가창 일치합니다 페이지에 보여주고, 액션에 해당 하는 영화를 그 다음 content로, 범죄에 해당 하는 영화를 마지막 content로 보여준다.
- 해당 기능에서 아쉬운 점 : 체크박스 선택 시 2개의 영화를 선택하여야 하는데 한 번 선택하고 수정이 안되는 부분을 구현하지 못하였다. 간단한 줄 알았던 기능이었지만 많은 시도와 노력에도 불구하고 구현하지 못했음.



### 5-4. 커뮤니티

- 상단 `nav bar`에 있는 마이페이지를 누르면 영화 후기 게시판으로 이동한다.
- 리뷰 작성하기를 누르면 글 제목, 영화제목, 평가 점수, 본문 내용 등을 작성 할 수 있는 폼이 있고 작성이 완료 되면 영화 후기 게시판에 전체 글이 보여진다(작성자, 작성시각, 좋아요 포함)
- 또한, 리뷰에 해당하는 댓글을 쓸 수 있으며 본인 이 작성한 글, 댓글을 수정 / 삭제 할 수 있다.





## 6. 기타(느낀점, 힘들었던 점)

- 약 4개월 간의 배웠던 교육 내용을 토대로 한 웹 서비스 개발 프로젝트를 진행하였다.

- 일주일 간의 짧으면 짧은 시간 동안, 최대한 노력하여 많은 것을 구현하고자 하였지만, 많이 부족한 부분도 있어서 개발 역량을 더 높여야 겠다고 생각이 든다.

- 힘들 었던 점은 아래와 같다.

  - `DB` 설계를 하는 것 만으로도 1일을 소요하였다. 해당 `API`에 담겨진 내용을 넣는것은 쉽게 할 수 있었지만 원하는 정보만 빼와서 그 값을 테이블에 넣는것은 매우 어려웠다.

  - 영화 리스트의 각 카드 선택 시 `MODAL`창을 띄워 각 영화 상세 내용을 보여주고 싶었다. 이 부분에서 첫번째 영화의 내용이 각 카드에 중복되어 보여지는 상황이 발생하였다. `data-target` 과 `id`의 값이 일치해야 한다는 것을 알았지만 이 때 의 값이 숫자가 먼저 오면 안되는 부분을 알지 못하였다.

    이것을 알아보고 구현하느라 1일을 소요하였다......

  - 또한, 유부트 API를 받아서 재생을 하고, 재생을 멈추지 않고 `MODAL`창을 꺼도 계속 재생되고 있는 문제가 발생하였다. 이 부분은 `iframe`의 `src`를 비워주는 함수를 실행하며 해결 할 수 있었다.

  - `CSS`부분은 타고난 미적감각이 없어서 매우 힘들었다.....