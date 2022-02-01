FROM python:3.8-alpine

RUN apk update \
    && apk add --no-cache --virtual build-deps gcc libc-dev linux-headers \
    && apk add --no-cache jpeg-dev zlib-dev \
    && pip install --upgrade pip

COPY setup.py /app/setup.py

COPY README.md /app/README.md

COPY ./pycasso /app/pycasso

COPY ./app /app/app

WORKDIR /app

RUN python setup.py install

RUN apk del build-deps

ENTRYPOINT [ "python" ]

CMD [ "app/app.py" ]
