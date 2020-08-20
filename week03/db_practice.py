from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 설치 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

# MongoDB에 insert 하기

target_movie =db.movies.find.one({'titel': '월-E'})
target_star = target_movie['star']

movies = list(db.movies.find({'titel': '월-E'}))

for movie in movies :
    print(movie['titel'])
