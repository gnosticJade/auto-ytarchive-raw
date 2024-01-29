FROM python:3.8

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV NAME=auto-ytarchive-raw-docker
ENV HOSHINOVA_HOST=127.0.0.1
ENV HOSHINOVA_PORT=1104
ENV HOSHINOVA_DOWNLOAD=/tmp
ENV HOSHINOVA_MEMBER_DOWNLOAD=/tmp/member
ENV HOSHINOVA_PREMIERE_DOWNLOAD=/tmp/premiere
ENV COOKIE_PATH=/app/cookie

CMD ["python", "./index.py"]