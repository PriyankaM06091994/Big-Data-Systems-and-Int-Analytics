## Team2_CSYE7245_Spring2021

## Big Data Systems and Int Analytics


## Team Information

| NAME              |     NUID        |
|------------------ |-----------------|
|   Tanvi Gurav     |   001306848     |
|   Keerti Ojha     |   001050173     |
| Priyanka Malpekar |   001302741     |


## Table of Contents
* About
* Architecture
* Dataset
* Requirements
* Setup
* Steps to regenerate
* Serverless Lambda Function
* Streamlit
* Black Box Testing - PyTest
* Load Testing - Locust
* References


## Architecture



## Serverless Lambda Functions

:file_folder: **Reference Folder:** `/lambda functions`


## Streamlit

## Black Box Unit Testing Using Pytest

:file_folder: **Reference File:** `/BlackBoxTesting-Pytest/test_api_gateway.py`

**Command to execute:** `python -m pytest -v`

In our scenario, we take into consideration different use cases for performing **unit testing on our serverless lambda endpoints** by passing valid and invalid inputs to test if it withstands and works under both circumstances. Following is the result of the **12 unit tests** that we performed which takes approximately **3.42 seconds** to complete:

![git](https://user-images.githubusercontent.com/59846364/116640531-d0b94e80-a938-11eb-8e70-a765c4b3ac83.PNG)



## References:

https://blog.jcharistech.com/2020/05/30/how-to-add-a-login-section-to-streamlit-blog-app/
https://docs.aws.amazon.com/connect/latest/adminguide/data-streaming.html
https://docs.aws.amazon.com/connect/latest/adminguide/set-up-recordings.html
https://github.com/jrieke/streamlit-analytics
https://developers.google.com/maps/documentation/geocoding/overview?hl=en_US#ReverseGeocoding
https://developers.google.com/maps/documentation/embed/embedding-map
https://www.geeksforgeeks.org/python-fetch-nearest-hospital-locations-using-googlemaps-api/
https://public.opendatasoft.com/explore/dataset/us-zip-code-latitude-and-longitude/
https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html
https://www.mrnice.dev/posts/testing-aws-lambda-and-api-gateway/
