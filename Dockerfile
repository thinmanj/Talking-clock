FROM python:2.7

RUN apt-get update && apt-get install -y libespeak-dev

ADD requirements.txt /
RUN pip install -r /requirements.txt

ADD alarm_clock.py /

ENTRYPOINT [ "python", "./alarm_clock.py" ]
