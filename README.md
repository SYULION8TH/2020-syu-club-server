# 2020-syu-club-server

# 동아리 연합회 백엔드 설명

동아리 박람회를 대체하기 위해 동아리 연합회를 진행할 예정입니다. 

인원: 박기홍, 정하늘, 이지수, 박미란, 위보람

## 세팅 방법

1. git clone을 합니다.
`git clone https://github.com/SYULION8TH/2020-syu-club-server.git`

2. 이후 멋사 구글 드라이브에서 env.py 와 mysql.cnf를 다운 받습니다.
https://drive.google.com/drive/folders/1SVlbKT-klrC5g_k3ljm5sYO2dVz33sVd?usp=sharing

3. 2020-syu-club-server/secure 이와 같이 2020-syu-club-server폴더 안에 secure폴더를 생성 후 위 두 파일을 넣습니다. 

4. 2020-syu-club-server폴더가 있는 위치에서 가상환경(`python -m venv venv`)을 생성해 줍니다.

5. 가상환경 실행 후 requirements.txt가 있는 위치에서 `pip install -r requirements.txt`명령어를 입력합니다.

6. `python manage.py runserver` 이후 `127.0.0.1:8000/admin`으로 들어가서 제대로 되는지 확인합니다.
> - id : dev
> - password : 12345

7. 개발 시작합시다.

## 소셜 로그인 기능 test 하고 싶으신 분!
1. 서버를 킨 후 localhost:8000/accounts/kakao/login or /accounts/google/login (반드시 localhost여야함!)
2. 각 로그인 페이지에서 가입을 진행한다.
3. localhost:8000/admin 에서 유저 정보가 등록되어 있는지 확인한다. (user or socialaccount)

동아리 앱 폴더:

### 동아리 - 하늘

- 동아리 목록 / 상세
- 활동 포스팅 좋아요 개수에 따른 동아리 목록
- 관심 동아리 목록
- 관심 동아리 설정
- 관심 동아리 삭제

### QnA - 이지수

- QnA 목록
- QnA 상세
- QnA 댓글 / 비밀댓글(?) / QnA 대댓글

### 게시물 - 박미란

- 게시물 목록 
- 게시물 상세
- 게시물 좋아요 기능 N:M
- 조회수 측정 - 위보람
- 인기 게시물(?)
- 게시물 댓글 / 게시물 대댓글대댓글

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
