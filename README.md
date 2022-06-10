
## Intro
This is a short URL backend server made by FastAPI, python3, postgreSQL.
If the URL is not used longer than 1 month it will be deleted from the database.

## How to run
```
pip install -r requirements.txt

uvicorn main:app "--reload"
```

## How to test
```
pytest
```

## Swagger
http://localhost:8000/docs

## ReDoc
http://localhost:8000/redoc

## DB

used PostgreSQL v14

- create table

```postgresql
CREATE TABLE public.short_url_mt (
	id varchar NOT NULL,
	url varchar NOT NULL,
	last_used_dtm timestamptz NULL DEFAULT now(),
	create_dtm timestamptz NULL DEFAULT now()
);
```


<!-- ## Thoguht
1. db 하루에 한번씩 배치 돌면서 없애기. -> 마지막 조회일자 기준.
2. pk를 무엇으로? sequence 가능? sequence 가능하면 base62사용시 한바뀌 916,132,832. 그냥 써도 될듯. PK 중복체크 필수! -->

<!-- ## Q
1. 왜 굳이 random?
2. URL 최대길이? 2000자 정도
- https://qqqqqq.tistory.com/entry/%EC%B5%9C%EB%8C%80-URL-%EA%B8%B8%EC%9D%B4%EC%97%90-%EB%8C%80%ED%95%9C-%EC%9D%B4%EC%95%BC%EA%B8%B0
3. Redis? 성능을 위해 있으면 좋다.
4.   -->


## reference
1. https://medium.com/monday-9-pm/%EC%B4%88%EB%B3%B4-%EA%B0%9C%EB%B0%9C%EC%9E%90-url-shortener-%EC%84%9C%EB%B2%84-%EB%A7%8C%EB%93%A4%EA%B8%B0-1%ED%8E%B8-base62%EC%99%80-%EC%B6%A4%EC%9D%84-9acc226fb7eb
2. https://velog.io/@meme2367/%EB%8B%A4%EC%8B%9C-%EB%A7%8C%EB%93%A4%EC%96%B4%EB%B3%B4%EB%8A%94-Url-Shortener
3. https://lovecode.tistory.com/120
