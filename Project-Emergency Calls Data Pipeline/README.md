## Team2_CSYE7245_Spring2021

## Big Data Systems and Int Analytics


## Team Information

| NAME              |     NUID        |
|------------------ |-----------------|
|   [Tanvi Gurav](https://www.linkedin.com/in/tanvigurav/)     |   001306848     |
|   [Keerti Ojha](https://www.linkedin.com/in/keertiojha/)     |   001050173     |
| [Priyanka Malpekar](https://www.linkedin.com/in/priyankamalpekar6/) |   001302741     |


## Table of Contents
* About
* Architecture
* Dataset
* Folder Structure
* Requirements
* Setup
* Steps to regenerate
* Serverless Lambda Function
* Streamlit
* Black Box Testing - PyTest
* Load Testing - Locust
* References

## About

The main aim of our project is to handle Emergency audio calls and build a fully functional data pipeline to notify it to the correct entities using various AWS services and demonstrating insights in a reference web application.

## CLAT Link

Link: https://codelabs-preview.appspot.com/?file_id=1hLC_-yuAXatvpq8ndS7YYJFFCvrEfW4-yeMCmZMKRWg#0

## AWS Deployment Link:

Link: http://52.86.246.227:8501

Login Credentials to try our website:
Username: admin
Password: admin


## Dashboard Links:

1. https://app.powerbi.com/view?r=eyJrIjoiODgzZDQ5YzQtNTNmMS00OWE4LWIwMWMtZGM3MTM0NGI1MWEzIiwidCI6ImE4ZWVjMjgxLWFhYTMtNGRhZS1hYzliLTlhMzk4YjkyMTVlNyIsImMiOjN9

2. https://app.powerbi.com/view?r=eyJrIjoiZDExNGU2NGYtZmU2MC00M2U3LWI4ODUtYmI4NmNiZGIxMWU5IiwidCI6ImE4ZWVjMjgxLWFhYTMtNGRhZS1hYzliLTlhMzk4YjkyMTVlNyIsImMiOjN9&pageName=ReportSection

## Architecture


## Requirements

- Most labs require an Amazon Web Services account to deploy and run. Signup for an AWS Account [here](https://portal.aws.amazon.com/billing/signup#/start).
- Python 3.7+
- Refer to the `requirements.txt` file or `README.md` inside the respective directories to install all dependencies.


## Serverless Lambda Functions

:file_folder: **Reference Folder:** `/lambda functions`


## Streamlit

Reference Folder: Streamlit/

* Run the streamlit app using command streamlit run streamlit.py
* You can access the app from your browser on https://localhost:8501

## Black Box Unit Testing Using Pytest

:file_folder: **Reference File:** `/BlackBoxTesting-Pytest/test_api_gateway.py`

**Command to execute:** `python -m pytest -v`

In our scenario, we take into consideration different use cases for performing **unit testing on our serverless lambda endpoints** by passing valid and invalid inputs to test if it withstands and works under both circumstances. Following is the result of the **12 unit tests** that we performed which takes approximately **3.42 seconds** to complete:

![git](https://user-images.githubusercontent.com/59846364/116640531-d0b94e80-a938-11eb-8e70-a765c4b3ac83.PNG)

## Locust

Load testing on FastApi endpoints: locust -f project-locust.py

Load testing on AWS Api Gateway endpoints: locust -f project-locust.py

This will start the locust console on http://127.0.0.1:8089 in the browser

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
