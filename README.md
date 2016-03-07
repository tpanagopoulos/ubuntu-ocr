# ubuntu-ocr
An OCR server, based on Ubuntu and Tesseract OCR. The REST service is implemented on Python / Flask.

## Build
docker build -t "ubuntu-ocr" .

## Execution
docker run -ti -p 5000:5000 --name ocr ubuntu-ocr
