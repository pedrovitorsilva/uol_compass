FROM amazonlinux:latest
RUN yum update -y && \
    yum install -y \
    python3-pip \
    zip \
    && yum -y clean all
RUN python3.9 -m pip install --upgrade pip --ignore-installed pip
