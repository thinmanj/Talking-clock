# Talking-clock
small demo script with dockers

after cloning the repo just build the docker

$ docker build -t irish_clock .

then just call it, for example:

$ docker run --device /dev/snd irish_clock 00:00

$ docker run --device /dev/snd irish_clock 01:30

$ docker run --device /dev/snd irish_clock 12:05

Doctest are runned like:

$ docker run --device /dev/snd irish_clock -t -v
