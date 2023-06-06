FROM jenkins/jenkins:2.401.1
USER root
RUN apt-get update && apt-get install -y --no-install-recommends python3 python3-pip python3-setuptools && pip install requests pytest && apt install wget && echo y | apt install cmake
