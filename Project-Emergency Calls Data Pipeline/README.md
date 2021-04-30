## Team2_CSYE7245_Spring2021

## Big Data Systems and Int Analytics


## Team Information

| NAME              |     NUID        |
|------------------ |-----------------|
|   [Tanvi Gurav](https://www.linkedin.com/in/tanvigurav/)     |   001306848     |
|   [Keerti Ojha](https://www.linkedin.com/in/keertiojha/)     |   001050173     |
| [Priyanka Malpekar](https://www.linkedin.com/in/priyankamalpekar6/) |   001302741     |

## CLAT Link

Link: https://codelabs-preview.appspot.com/?file_id=1hLC_-yuAXatvpq8ndS7YYJFFCvrEfW4-yeMCmZMKRWg#0

## Demo Video Recording

https://www.youtube.com/watch?v=HyeLsyKRRGE

## AWS Deployment Link:

- The Streamlit Web Application hosted on AWS EC2 instance can be acccessed at: http://52.86.246.227:8501
- Login Credentials to try out website:
```
Username: admin
Password: admin
```


## Table of Contents
* [About](#about)
* [Architecture](#architecture)
* [Dataset](#dataset)
* [FolderStructure](#folderstructure)
* [Requirements](#requirements)
* [Setup](#setup)
* [Steps to regenerate](#stepstoregenerate)
* [Serverless-Lambda-Function](#serverless-lambda-function)
* [Streamlit](#streamlit)
* [BlackBoxTesting](#blackboxtesting)
* [Locust](#locust)
* [References](#references)

## About

The main aim of our project is to handle Emergency audio calls and build a fully functional data pipeline to notify it to the correct entities using various AWS services and demonstrating insights in a reference web application.

![a](https://user-images.githubusercontent.com/59846364/116672228-ee55da80-a96f-11eb-82d7-a94e27b4fc28.png)


## Architecture

![FinalProject](https://user-images.githubusercontent.com/59594174/116677087-c9646600-a975-11eb-8e9b-79960448b48c.png)


## Dataset

In our scenario, we are fetching real time call data that is being received and recorded through AWS Connect Service which are in the format .wav files. This audio call recording data will be stored in AWS S3 bucket as soon as the call between the customer and agent is closed.

## FolderStructure

The overall folder structure of the project is summarized as below:
```
Project-Emergency Calls Data Pipeline/
├── BlackBoxTesting-Pytest/
│   └── test_api_gateway.py
├── lambda functions/
│   ├── getAddress.py
│   ├── getDataFromS3.py
│   ├── movetohistoricalbucket.py
│   ├── sns_notification.py
│   ├── transcribejob.py
│   └── transcribestatusjob.py
├── Locust/
│   └── project-locust.py
├── PowerBi/
│   ├── EmergencyCalls.pdf
│   └── EmergencyCallsDataAnalysis.pdf
├── README.md
└── Streamlit/
    ├── config.py
    ├── data.db
    ├── download_audio.py
    ├── location.py
    ├── requirements.txt
    ├── services.py
    ├── streamlit.py
    ├── support.png
    ├── test.py
    └── welcome.gif
```

## Requirements

- Python Version 3.7+
- Amazon Web Services account to deploy and run. Signup for an AWS Account [here](https://portal.aws.amazon.com/billing/signup#/start).
- Google Cloud Platform account to leverage various services from Google Maps API. Sign up for $300 credit [here](https://cloud.google.com/free)
- Refer `requirements.txt` file to install all dependencies.
- Generate API key and secret access keys from GCP and AWS respectively.

## Setup

For detailed setup refer [here](https://codelabs-preview.appspot.com/?file_id=1aMilpp1VwJ5FC-V7HDH0ZoM2R0hW_5DXFbrj0BSnQKQ#1)







## Serverless Lambda Functions

:file_folder: **Reference Folder:** `/lambda functions`

The following are the serverless lambda functions configured in this project
* `getAddress.py` : Fetches the victim address from Dynamodb before sending out notification to corresponding entity
* `getDataFromS3.py`: Fetches transcribed data (audio-to-text) from the S3 Bucket
* `movetohistoricalbucket.py`: Moves audio call recordings from S3 for live calls to S3 for historical calls
* `sns_notification.py`: Triggers SNS email and text notifications to the help relief entity and victim respectively.
* `transcribejob.py`: Triggers a transcribe job which converts audio calls to transcripts
* `transcribestatusjob.py`: Fetches the status of the triggered transcribe job to check if it is 'Completed' or 'In Progress'

## Streamlit

:file_folder: **Reference Folder:** Streamlit/

* Run the streamlit app using command `streamlit run streamlit.py`
* You can access the locally app from your browser on `https://localhost:8501`

![s1](https://user-images.githubusercontent.com/59594174/116677378-23652b80-a976-11eb-85d6-191f8b3aa2d8.png)


![s2](https://user-images.githubusercontent.com/59594174/116677391-2829df80-a976-11eb-95e2-18d4598eeafe.png)


![s3](https://user-images.githubusercontent.com/59594174/116677409-2c55fd00-a976-11eb-98f6-31973db7df45.png)

## Black Box Unit Testing Using Pytest

:file_folder: **Reference File:** `/BlackBoxTesting-Pytest/test_api_gateway.py`

**Command to execute:** `python -m pytest -v`

In our scenario, we take into consideration different use cases for performing **unit testing on our serverless lambda endpoints** by passing valid and invalid inputs to test if it withstands and works under both circumstances. Following is the result of the **12 unit tests** that we performed which takes approximately **3.42 seconds** to complete:

![git](https://user-images.githubusercontent.com/59846364/116640531-d0b94e80-a938-11eb-8e70-a765c4b3ac83.PNG)

## Locust

:file_folder: **Reference File:** `/Locust/project-locust.py`

Load testing on AWS Api Gateway endpoints: `locust -f project-locust.py`

This will start the locust console on http://127.0.0.1:8089 in the browser

![locust](https://user-images.githubusercontent.com/59594174/116653775-d83b2080-a955-11eb-989f-16e25421cab1.png)

## Dashboards

#### Dashboard 1:

https://app.powerbi.com/view?r=eyJrIjoiODgzZDQ5YzQtNTNmMS00OWE4LWIwMWMtZGM3MTM0NGI1MWEzIiwidCI6ImE4ZWVjMjgxLWFhYTMtNGRhZS1hYzliLTlhMzk4YjkyMTVlNyIsImMiOjN9


![pasted image 0](https://user-images.githubusercontent.com/59594174/116649651-c6557f80-a94d-11eb-8806-e3ba4f20bcf6.png)

#### Dashboard 2: 

https://app.powerbi.com/view?r=eyJrIjoiZDExNGU2NGYtZmU2MC00M2U3LWI4ODUtYmI4NmNiZGIxMWU5IiwidCI6ImE4ZWVjMjgxLWFhYTMtNGRhZS1hYzliLTlhMzk4YjkyMTVlNyIsImMiOjN9&pageName=ReportSection


![pasted image 0 (2)](https://user-images.githubusercontent.com/59594174/116651053-5d233b80-a950-11eb-9904-efcb49eda74b.png)


## References:

* https://blog.jcharistech.com/2020/05/30/how-to-add-a-login-section-to-streamlit-blog-app/
* https://docs.aws.amazon.com/connect/latest/adminguide/data-streaming.html
* https://docs.aws.amazon.com/connect/latest/adminguide/set-up-recordings.html
* https://github.com/jrieke/streamlit-analytics
* https://developers.google.com/maps/documentation/geocoding/overview?hl=en_US#ReverseGeocoding
* https://developers.google.com/maps/documentation/embed/embedding-map
* https://www.geeksforgeeks.org/python-fetch-nearest-hospital-locations-using-googlemaps-api/
* https://public.opendatasoft.com/explore/dataset/us-zip-code-latitude-and-longitude/
* https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html
* https://www.mrnice.dev/posts/testing-aws-lambda-and-api-gateway/
* https://towardsdatascience.com/how-to-deploy-a-streamlit-app-using-an-amazon-free-ec2-instance-416a41f69dc3
