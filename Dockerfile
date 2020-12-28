FROM python:3.8-alpine
WORKDIR /thumbnail_project
ADD . /thumbnail_project
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev\
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install -r requirements.txt \
    && apk del build-deps
CMD ["python","main.py"]