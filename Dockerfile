# Python 3.11이 포함된 공식 FastAPI 이미지 사용
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

# 작업 디렉토리 설정
WORKDIR /app

# requirements.txt 파일을 복사하고 종속성 설치
COPY requirements.txt .
RUN pip install -r requirements.txt

# 프로젝트 코드 전체를 컨테이너로 복사
COPY . .

# 기본 FastAPI 포트 개방
EXPOSE 8000

# 앱 실행 명령어
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
