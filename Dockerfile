ARG PYTHON_VERSION=3.8.1
ARG ALPINE_VERSION=3.11

FROM alpine:${ALPINE_VERSION} as builder
ENV PYTHONUNBUFFERED 1
RUN apk add --no-cache \
            --upgrade \
            --repository http://dl-cdn.alpinelinux.org/alpine/edge/main \
        alpine-sdk \
        postgresql-dev \
        python3 \
        python3-dev \
        py-pip

WORKDIR /wheels
COPY ./requirements.txt /wheels/requirements.txt
RUN pip3 install -U pip \
    && pip3 install wheel \
    && pip3 wheel -r ./requirements.txt

FROM python:${PYTHON_VERSION}-alpine${ALPINE_VERSION}
ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache \
            --upgrade \
            --repository http://dl-cdn.alpinelinux.org/alpine/edge/main \
        libstdc++ \
        libpq \
        postgresql-client \
    && rm -rf /var/cache/apk/*

COPY --from=builder /wheels /wheels
RUN pip3 install -U pip \
    && pip3 install --no-cache-dir \
                    -r /wheels/requirements.txt \
                    -f /wheels \
    && rm -rf /wheels

WORKDIR /app
COPY ./ ./