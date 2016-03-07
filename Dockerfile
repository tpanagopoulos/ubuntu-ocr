FROM ubuntu:14.04

MAINTAINER Thodoris Panagopoulos <thodoris.panagopoulos@gmail.com> version: 0.1

# Install dependencies
RUN \
  apt-get update && \
  apt-get install -y software-properties-common python-software-properties unzip

RUN \
  apt-get install -y python python-pip python-flask python-dev build-essential \
  gcc libjpeg-dev zlib-bin zlib1g-dev ghostscript xpdf imagemagick

# Install pip dependencies
RUN pip install Pillow
RUN pip install reportlab
RUN pip install watchdog
RUN pip install pypdf2
RUN pip install pypdfocr

RUN \
  apt-get install -y \
  tesseract-ocr tesseract-ocr-eng tesseract-ocr-ell

RUN mkdir -p /opt/rest-wrapper
WORKDIR /opt/rest-wrapper

# Add wrapper script
ADD rest-wrapper.py /opt/rest-wrapper

# Define working directory.
WORKDIR /tmp

# Create tmp dirs
RUN mkdir -p /tmp/data/uploads
RUN mkdir -p /tmp/data/extracted
RUN mkdir -p /tmp/data/ocr

EXPOSE 5000:5000

CMD ["/usr/bin/python","/opt/rest-wrapper/rest-wrapper.py"]
