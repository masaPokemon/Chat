FROM python:3.9-slim

WORKDIR /app

# 必要なパッケージをインストール
RUN pip install pyngrok email

CMD ["python", "smtp_server.py"]
