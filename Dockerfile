FROM centos:7


RUN yum clean all \
    && yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
    && yum install -y rpm-build rpmdevtools \
    && yum install -y which gpg gcc gcc-c++ make \
    && yum install -y https://centos7.iuscommunity.org/ius-release.rpm \
    && yum install -y python36u \
    && yum install -y python36u-libs \
    && yum install -y python36u-devel \
    && yum install -y python36u-pip \
    && pip3 install virtualenv

COPY . /hsimp3
Workdir /hsimp3

RUN virtualenv /usr/local/venv/hsimp3 \
    && source /usr/local/venv/hsimp3/bin/activate \
    && pip3 install -r requirements-test.txt \
    && pylint ./hsimp3/*.py \
    && pycodestyle ./hsimp3/*.py


CMD ["python3", "-m unittest discover tests"]
