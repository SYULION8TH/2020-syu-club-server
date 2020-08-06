# 2020-syu-club-server

# 동아리 연합회 백엔드 설명

동아리 박람회를 대체하기 위해 동아리 연합회를 진행할 예정입니다. 

인원: 박기홍, 정하늘, 이지수, 박미란, 위보람

동아리 앱 폴더:

### 동아리 - 하늘

- 동아리 목록 / 상세
- 활동 포스팅 좋아요 개수에 따른 동아리 목록
- 관심 동아리 목록
- 관심 동아리 설정
- 관심 동아리 삭제
- 동아리 별 회원 목록

### QnA - 박미란

- QnA 목록
- QnA 상세
- QnA 댓글 / 비밀댓글(?) / QnA 대댓글

### 게시물 - 이지수

- 게시물 목록
- 게시물 상세
- 인기 게시물
- 게시물 댓글 / 게시물 대댓글

### account

- 소셜로그인


## URL 설계

+ 자원의 컬렉션 이름으로는 복수형을 쓴다.
ex) /Post/1 -> /posts/1
+ http의 Method가 들어가서는 안된다.
+ 동사표현을 쓰면 안된다.
ex) /posts/show/1 -> GET /posts/1 
+ 경로 중 변하는 값은 유일한 값으로 바꾼다.
ex) id가 12인 게시물을 지우는 행위 DELETE /posts/12

+ '/'는 계층관계를 나타내는데 사용한다.
+ URI 마지막 문자로 슬래시(/ )를 포함하지 않는다.
+ 대문자는 쓰지 않고 소문자만 쓴다.   
+ 하이픈(- )은 URI 가독성을 높이는데 사용
불가피하게 긴 URI경로를 사용하게 된다면 하이픈을 사용해 가독성을 높인다.
+ 밑줄(_ )은 URI에 사용하지 않는다.
밑줄은 보기 어렵거나 밑줄 때문에 문자가 가려지기도 하므로 가독성을 위해 밑줄은 사용하지 않는다.
+ 리소스 간에 연관 관계가 있는 경우
ex) 리소스명/{리소스ID}/관계가 있는 다른 리소스 명
--> posts/1/comments

QnA 예시)

|설명|Method|경로|
|----|-------|----|
|한 동아리의 QnA목록을 나타낸다.|GET|/clubs/:id/qna|
|한 동아리의 QnA상세를 나타낸다.|GET|/clubs/:id/qna/:id|
|한 동아리의 QnA를 수정한다.|PUT|/clubs/:id/qna/:id|
|한 동아리의 QnA를 삭제한다.|DELETE|/clubs/:id/qna/:id|
