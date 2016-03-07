from flask import Flask, request, send_file
import uuid
import subprocess

app = Flask(__name__)

UPLOAD_FOLDER = '/tmp/data/uploads/'
EXTRACTED_FOLDER = '/tmp/data/uploads/' #'/tmp/data/extracted/'
OCR_FOLDER = '/tmp/data/ocr/'

@app.route('/ocr', methods=['POST'])
def ocr():
    app.logger.info('Invoked ocr')
    filename = str(uuid.uuid4())
    app.logger.info('Filename is: ' + filename)
    uploadPath = UPLOAD_FOLDER + filename
    extractedPath = EXTRACTED_FOLDER + filename + "_ocr.pdf"
    ocrPath = OCR_FOLDER + filename + ".tar"
    # Store to filesystem
    f = request.files['file']
    app.logger.info('Fetched file from request ')
    f.save(uploadPath)
    app.logger.info('Stored file to : ' + uploadPath)
    # OCR
    subprocess.call(["pypdfocr", "-l", "eng", uploadPath]) #this must be replaced with actual OCR call
    app.logger.info('Processed file to : ' + extractedPath)
    # TAR
    subprocess.call(["tar", "cf", ocrPath, extractedPath])
    app.logger.info('Packaged file to : ' + ocrPath)
    # Return
    return send_file(ocrPath)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
