## Big Data Systems and Int Analytics

## Assignment1

#### Team Information

| NAME              |     NUID        |
|------------------ |-----------------|
|   Tanvi Gurav     |   001443824     |
|   Keerti Ojha     |   001050173     |
| Priyanka Malpekar |   001302741     |


#### Data Pipeline in AWS

#### CLAAT Link

## About

**Implementing a data pipeline of SEVIR and Storm Events using Amazon Web Services S3 bucket for storage,
Amazon Glue for ETL and Amazon Quicksight for Visualization and Dashboard creation.**

![AWS](https://user-images.githubusercontent.com/59594174/109194191-32a5de00-7767-11eb-916e-827815f25b96.png)

## Requirements

1. Configuring Apache Airflow to upload data files in S3 bucket

2. Configuring AWS Glue to create pipeline

3. Adding Glue Crawlers for each dataset to create table in Glue Data Catalog

5. Creating Jobs in AWS Glue Studio and configuring Job Details for running the job

6. Creating Quicksight account for Visulization

7. Configuring Dataset in AWS QuickSight

## Test Results

#### Creating script to upload data in S3 bucket using "Boto3" in Apache Airflow

- exceuted **Sevir Pipeline** in DAG Console

#### Data Preprocessing and Transformation in Glue

**AWS Glue** is a serverless data integration service that makes it easy to discover, prepare, and combine data for analytics, machine learning, and application development.

- Created a new Glue Database
- Added Glue Crawlers and executed them to access data from S3 bucket in Glue Data Catalog Table
- Created ETL Jobs in Glue Studio to clean, rename columns, drop columns, create a new column, join the two Data Catalog tables
- Provided the target path of the ETL jobs as S3 bucket
- Configured ETL Jobs and provided IAM role with Glue ServiceRole access for execution

```
1. Combined Storm Event Details 2018 data with Storm Events Fatality 2018 data
2. Transformed Sevir Metadata(Catalog) and added a new ID column excluding character in dataset
3. Used the new ID column of Sevir data to join with Storm Event Details

```

#### Data Query Using Athena and Visualization in Quicksight

**Athena** is used to query the dataset created in AWS Glue Data Catalog

**Amazon QuickSight** is a scalable, serverless, embeddable, machine learning-powered business intelligence (BI) service built for the cloud. 
QuickSight lets you easily create and publish interactive BI dashboards that include Machine Learning-powered insights.

- Loaded the dataset in Quicksight deom S3 bucket storage
- Uploaded manifest.json file with the location of the S3 bucket folder
- We can create the Dashboard in the Analysis console of Quicksight

```
1. Combined Sevir Metadata(catalogue) with Storm Events Details 2018 Dashboard
- Showing count of image-types(vis,vil,ir069,ir107,lght) County wise
- Sum of injuries by State distributed by timezones
- Magnitude of event by State and Event Type
- Showing datewise, idwise, count of image types

2. Combined Storm Event Details 2018 and Storm Events Fatality 2018 dashboard
- Sum of deaths by year and state
- Sum of deaths by Event Type
- Sum of deaths by Sex and County
- Damaged Property by state

```
