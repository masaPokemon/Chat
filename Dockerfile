FROM python:3.9-slim

WORKDIR /app

# 必要なパッケージをインストール
RUN pip install pyngrok email

# SMTP サーバーのコードをコピー
COPY 

CMD ["python", "smtp_server.py"]
