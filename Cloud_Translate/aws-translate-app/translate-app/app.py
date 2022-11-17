from flask import render_template, Flask, request
import boto3
import json
account_id = "AKIAUTP2CT7AAYERIVHJ"
account_key = "Ao4B8MS7KUu0lVWHaAR7n4/VAZJVItwkAn1v4tXA"
def client():
    global account_id
    global account_key
    global account_token
    print(account_id, account_key)
    client = boto3.client("textract", aws_access_key_id=account_id,
                          aws_secret_access_key=account_key,
                          region_name='us-east-1')
    return client
app = Flask(__name__)

@ app.route("/", methods=["GET"])
def main():
    extractedText = ""
    responseJson = {

        "ban truong dep trai": extractedText
    }
    return render_template("index.html", jsonData=json.dumps(responseJson))

@ app.route("/extracttext", methods=["POST"])
def extractImage():
    file = request.files.get("filename")
    binaryFile = file.read()
    textractclient = client()
    response = textractclient.detect_document_text(
        Document={
            'Bytes': binaryFile
        }
    )
    extractedText = ""
    for block in response['Blocks']:
        if block["BlockType"] == "LINE":
            extractedText = extractedText+block["Text"]+" "
    responseJson = {

        "text": extractedText
    }
    print(responseJson)
    return render_template("index.html", jsonData=json.dumps(responseJson))

@ app.route("/translatedocument", methods=["POST"])
def extractDocument():
    file = request.files.get("filenameDocument")
    binaryFile = file.read()
    # textractclient = client()




    # response = textractclient.detect_document_text(
    #     Document={
    #         'String': binaryFile
    #     }
    # )
    extractedText = binaryFile
    # for block in response['Blocks']:
    #     if block["BlockType"] == "LINE":
    #         extractedText = extractedText+block["Text"]+" "





    responseJson = {

        "text": extractedText
    }
    print(responseJson)
    return render_template("index.html", jsonData=json.dumps(responseJson))



# @ app.route("/extractspeach", methods=["POST"])
# def get_job(job_name, transcribe_client):
#     """
#     Gets details about a transcription job.

#     :param job_name: The name of the job to retrieve.
#     :param transcribe_client: The Boto3 Transcribe client.
#     :return: The retrieved transcription job.
#     """
#     try:
#         response = transcribe_client.get_transcription_job(
#             TranscriptionJobName=job_name)
#         job = response['TranscriptionJob']
#         logger.info("Got job %s.", job['TranscriptionJobName'])
#     except ClientError:
#         logger.exception("Couldn't get job %s.", job_name)
#         raise
#     else:
#         return job



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)