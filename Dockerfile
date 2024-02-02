FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .

# 安装 gcc，以便诸如 MarkupSafe 和 SQLAlchemy 之类的 Python 包可以编译加速
# RUN apk add --no-cache gcc musl-dev linux-headers

RUN pip install -r requirements.txt

# CMD ["flask", "run", "--host=0.0.0.0"]