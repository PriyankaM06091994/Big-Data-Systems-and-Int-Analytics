## Big Data Systems and Int Analytics
 
## Assignment 3-Part 1

#### Team Information

| NAME              |     NUID        |
|------------------ |-----------------|
|   Tanvi Gurav     |   001443824     |
|   Keerti Ojha     |   001050173     |
| Priyanka Malpekar |   001302741     |
 

**Submission Date**: 2nd April'21


### CLAAT Link

https://codelabs-preview.appspot.com/?file_id=1jTHf8qaN4N300bceYkY12fPi7ERu2TbfQh8D3kCbA0w#1

## About

**Moody's Analytics** provides financial intelligence and analytical tools to help business leaders make better, faster decisions. It provides a robust set of APIs that enable users to interact with their economic and credit solutions.

**How do they Work?**

* Moody Analytics provides various API's as per the requirements of the applications
* Create a developer account -> Register an App -> Provides API key to access the API's
* In order to access the API's an access code is required which authorizes the user.
* New Apps can be created and accessed by using the Promo Code
* API's are displayed in an interactive swagger UI which assist in understanding the various API methods

## Dataset

**Lending Club  Datasets**

We are using two csv’s for our implementation viz:

* Lending_club_info.csv
* Lending_club_loan_two.csv

Kaggle Link to Dataset: https://www.kaggle.com/hadiyad/lendingclub-data-sets

## Architecture

**Moody Architecture**

![moody-architecture](https://user-images.githubusercontent.com/59594174/113445641-437bec00-93c4-11eb-8f11-4c0550fe650a.png)

**Proposed Architecture**

![Architecture](https://user-images.githubusercontent.com/59594174/113439421-889a2100-93b8-11eb-8ddf-de5ca21af2c6.png)



## Data Ingestion

Analyzing the raw data before ingestion using **XSV** for getting an insight on different aspects like number of columns, count of rows in each csv and over stats of the files.

1. Uploading data to S3
2. Downlaoding Data
3. Ingesting data in Snowflake database

## Airflow

Pipeline includes automating:
* Uploading data to S3
* Downloading data from S3
* Ingesting data in Snowflake database

![Airflow](https://user-images.githubusercontent.com/59594174/113439427-8b951180-93b8-11eb-9c0d-0bc6a2153fe3.png)

## Designing Fast API

![FastAPI](https://user-images.githubusercontent.com/59594174/113440163-dcf1d080-93b9-11eb-951d-7fcdc1805125.png)

## API Key Authentication

![Auth1](https://user-images.githubusercontent.com/59594174/113440173-e1b68480-93b9-11eb-80bd-a4d45b9d19f4.png)


![Auth2](https://user-images.githubusercontent.com/59594174/113440182-e54a0b80-93b9-11eb-9057-5617bf7c20bc.png)


![Auth3](https://user-images.githubusercontent.com/59594174/113440186-e7ac6580-93b9-11eb-872b-eb1308e57c22.png)

## Pytest

![Pytest](https://user-images.githubusercontent.com/59594174/113440194-ed09b000-93b9-11eb-84d6-597b20ad4514.png)

## Locust

You can access the website by hitting ‘http://127.0.0.1:8089’

**Locust UI**

![Locust1](https://user-images.githubusercontent.com/59594174/113439437-92238900-93b8-11eb-9ae7-714f98426c0a.png)

**Testing our end-points in Locust**

![Locust2](https://user-images.githubusercontent.com/59594174/113439441-951e7980-93b8-11eb-90f4-aa7b0d152a47.png)


## Streamlit

![STreamlit1png](https://user-images.githubusercontent.com/59594174/113439447-98196a00-93b8-11eb-8d9a-86141e3261d7.png)


![Streamlit2](https://user-images.githubusercontent.com/59594174/113439455-9c458780-93b8-11eb-9f0d-7f3865bff771.png)


https://user-images.githubusercontent.com/59594174/113441837-fba59680-93bc-11eb-9e92-01a01b109cff.mp4





