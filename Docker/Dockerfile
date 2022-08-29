FROM python:3.8-buster
LABEL maintainer="support@cosr.eu.org"

WORKDIR /work
RUN apt-get install git gcc && \
    git clone https://github.com/Oreomeow/warpplus.git --depth=1 /work && \
    pip install python-telegram-bot && \
    chmod +x warpplus.py

ENTRYPOINT ["python", "warpplus.py"]
