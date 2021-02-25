#### Team Information

| NAME              |     NUID        |
|------------------ |-----------------|
| Priyanka Malpekar |   001302741     |
|   Tanvi Gurav     |   001443824     |
|   Keerti Ozha     |   001050173     |


### Lab 1 - Getting started with AWS + Lambda

#### CLAAT Link
https://codelabs-preview.appspot.com/?file_id=1S2tP87Y0Bd7wZ-3jqAKWdCUl9__4dgl7RFbByM7HNS4#0


### Getting Started with AWS

### About

This lab demonstrated the implementation of AWS CLI and other services like IAM, Amazon S3, comprehend and lambda.

Amazon Web Services (AWS) provides computing resources and services that you can use to build applications within minutes at pay-as-you-go pricing. You can run nearly anything on AWS that you would run on physical hardware: websites, applications, databases, mobile apps, email campaigns, distributed data analysis, media storage, and private networks. The services they provide are designed to work together so that we can build complete solutions. There are currently dozens of services, with more being added each year. AWS is readily distinguished from other vendors because it is flexible, cost-effective, scalable, elastic and secure.


#### Requirements

1. Creating an AWS account

2. Configuring AWS CLI

3. Configuring AWS on our system

4. Getting started with IAM ( Identity Access Management )

5. Creating a virtual environment

6. Installing all the required packages in this virtual env - first-lambda

```
pip3 install Faker
pip3 install boto3
```

#### Test Results

#### Creating Amazon S3 Bucket

Amazon S3 - a simple storage service is a scalable, high-speed, web-based cloud storage service. 

--> Ensure below mentioned rules while creating any S3 bucket:
Block all public access
Disable bucket versioning
Disable encryption


#### Contents

- `s3_upload.py` - Python script to generate some fake data using Faker and uploadthe same to your S3 Bucket 
- `s3_download.py` - Downloading the file from S3 to your local environemnt 
- `comprehend_demo.py` - Using AWS Comprehend to implement sentiment analysis


- Lambda Functions - Deploying Lambda functions using Python Lambda. Documentation and boilerplate code is available on [this repository](https://github.com/holladileep/lambda-serverless-py) 
