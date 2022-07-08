from flask import Flask, request, render_template

import boto3
import json

textractclient = boto3.client("textract", aws_access_key_id="AKIASHQ25MX5V5RK7QL4",
                                aws_secret_access_key="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",
                                region_name="us-west-2")

app = Flask(__name__)


@app.route('/', methods=["GET"])
def main():
    return render_template("index.html", jsonData=json.dumps({}))

@app.route("/extract", methods=["POST"])
def extractImage():
    file = request.files.get("filename")
    binaryFile = file.read()
    response = textractclient.detect_document_text(
    Document={
        'Bytes': binaryFile
    }
    )
    extractedText = ""

    for block in response["Blocks"]:
        if block["BlockType"] == "LINE":
            extractedText = extractedText +  block["Text"] + "<br>"
    
    responseJson = {
        "text": extractedText
    }

    return render_template("index.html", jsonData=json.dumps(responseJson))



app.run("0.0.0.0", port=5000, debug=True)