## Big Data Systems and Int Analytics

## Assignment2

#### Team Information

| NAME              |     NUID        |
|------------------ |-----------------|
|   Tanvi Gurav     |   001443824     |
|   Keerti Ojha     |   001050173     |
| Priyanka Malpekar |   001302741     |
 
 **Submission Date: 26th March'21

#### Data Pipeline in AWS

#### CLAAT Link

https://codelabs-preview.appspot.com/?file_id=1jRDq1PIwklosCZ56j8xRczTw_2W8J8OCJ_UVoWYbeHk#8

## About

**The aim of this assignment is to build four fully functional pipelines from using text analytics API to perform sentiment analysis, getting the labelled data and building machine learning models using transfer learnings, using Flask to then deploy the model and finally storing the results in a Docker container.**


### Dataset

**Edgar Datasets

Dataset provided to us was the scraped data from Edgar datasets. 

It consisted of financial data of  50 companies. 


## Annotation Pipeline 1

Implementing a fully functional data pipeline using scraped data stored in S3 bucket, pre-processing the data to remove special characters and white-spaces, labelling and assigning sentiment scores by using ‘IBM Watson’ text API and loading the labelled data with its corresponding json file in S3 bucket.

Architecture Diagram for Annotation Pipeline:

![Pipeline1](https://user-images.githubusercontent.com/59594174/112587701-71fe3380-8dd4-11eb-91ce-19db601407fe.png)


1. Data Scraping:

Loading the scraped data from the Edgar Datasets in the S3 bucket.

2. Accessing the Pre-Processed Data:

The scraped data in then pre-processed to remove special characters & white spaces and the clean data is loaded in the S3 bucket 

3. Using IBM-Watson text API

The clean data is passed through IBM Watson text API which performs sentimental analysis on the clean data and provides us with a sentiment score. The data is then labelled by giving a value 1 to the positive sentiments and 0 to negative sentiments.

4. Loading in S3 bucket

The labelled data is then stored back in S3 bucket. The final file is in json format. 
Also, the labeled dataset output in csv format looks like this:

## LUIGI

The Annotation pipeline is automated in Luigi. Luigi - a python package helps us build complex pipelines on batch jobs.

Tasks automated in Luigi:
Loading scraped data in S3 bucket
Data Pre-Processing
Loading the clean data in S3 bucket
Performing Sentiment Analysis using IBM-Watson Text API
Loading the labeled data back in S3 bucket

![Luigi1png](https://user-images.githubusercontent.com/59594174/112587857-bbe71980-8dd4-11eb-84e2-44453eb6d99d.png)


![Luigi2](https://user-images.githubusercontent.com/59594174/112587866-c1dcfa80-8dd4-11eb-82a1-5bbec31e6248.png)

## Training Pipeline 2

Using the concept of transfer learning and making use of a pre-trained Tensorflow model to train our model and storing the results in a S3 bucket. 

![Pipeline2](https://user-images.githubusercontent.com/59594174/112587719-7c203200-8dd4-11eb-9306-7162cac05ef1.png)


Using a Pre-Trained TensorFlow Model to perform a Text Classification

We will be performing transfer-learning with TensorFlow Hub and Keras.

1. Getting texts and labels in the given format of Texts and Labels.

2. Encoding the labels for converting it into numerical values. Input data consists of sentences. Labels to predict are either 1 (positive) or 0 (negative).

3. Splitting the data into test and train.

4. Building the Model: 

   Pre-trained Model = tf2-preview/gnews-swivel-20dim

5. Evaluating the model and Calculating the model Accuracy

6. Prediction: Making predictions on the test data.

## SKLearn

We are automating the training pipeline using SKLearn - Python package scikit-learn provides a Pipeline utility to help automate machine learning workflows.

Tasks automated using SKLearn:

1.Reading Labelled Data
2.Training the Model
3.Saving the Model
4.Making Predictions

## Pipeline 3: Microservices

## Pipeline 4: Inference Pipeline

Dockerized Flask App - running the Generated Model to predict sentiments


## Flask

## Docker









