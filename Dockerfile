FROM python:3.12.2-slim-bookworm

ENV POETRY_VERSION=1.7.1

RUN apt-get update -q  \
    && apt-get upgrade -qy  \
    && apt-get install -y strace  \
    && apt-get clean  \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


RUN mkdir /app

COPY pyproject.toml .
COPY poetry.lock .

RUN python -m pip install --no-cache-dir poetry==$POETRY_VERSION  \
    && poetry config virtualenvs.create false  \
    && cd /app/  \
    && poetry install

COPY . /app
RUN cd /app

CMD ["strace", "-fc", "python"]