## Big Data Systems and Int Analytics

## Labs

#### Team Information

| NAME              |     NUID        |
|------------------ |-----------------|
|   Tanvi Gurav     |   001306848     |
|   Keerti Ozha     |   001050173     |
| Priyanka Malpekar |   001302741     |


## Lab 9 - Acne Type Classification Pipeline using CNN 

#### CLAAT Link
https://codelabs-preview.appspot.com/?file_id=1CnjVfvr_sCzdwPA1lF4MeIoD4AmcN5XVtOfdC7jY0M0#0

## About

**This lab demonstrates how to create a training pipeline that aims to identify the type of Acne-Rosacea, by training a model with images scraped from dermnet.com with a confidence score. The front-end application uses Streamlit to predict using the trained model.
**

<img src="/airflow_cnn_pipeline/img/approach.jpg" alt="approach" width="200"/>


#### Model - MobileNet (CNN) 
- Depthwise Separable Convolution is used to reduce the model size and complexity. It is particularly useful for mobile and embedded vision applications
- The model can be used in edge devices such as IoT devices or mobile applications - owing to its small size.

#### Continuous Model Integration

- Made possible by chaining all processes using Airflow
- The pipeline can be scheduled to run at a predefined cadence and is constantly retraining the model
- Continuously upload the trained graph and labels to S3

![pipeline](/airflow_cnn_pipeline/img/airflow.jpg)

### Training Pipeline

Airflow is a platform to programmatically author, schedule and monitor workflows.
Use airflow to author workflows as directed acyclic graphs (DAGs) of tasks. 

The airflow scheduler executes your tasks on an array of workers while following the specified dependencies. Rich command line utilities make performing complex surgeries on DAGs a snap. The rich user interface makes it easy to visualize pipelines running in production, monitor progress, and troubleshoot issues when needed. [1]

#### Use Cases

- Replace cron jobs: Monitoring cron jobs is hard and tedious. Instead of manually ssh to servers to find out if/why your jobs fail, you can visually see whether your code run or not through the UI and have Airflow notifies you when a job fails.
- Extract data: Airflow, with its many integrations, are used a lot for data engineering tasks. You can write tasks to extract data from your production databases, check data quality, and write the results to your on-cloud data warehouse.
- Transform data: You can interface with external services to process your data. For example, you can have a pipeline that submits a job to EMR to process data in S3 with Spark and writes the results to your Redshift data warehouse.
- Train machine learning models: You can extract data from a data warehouse, do feature engineering, train a model, and write the results to a NoSQL database to be consumed by other applications.
- Crawl data from the Internet: You can write tasks to periodically crawl data from the Internet and write to your database. For instance, you can get daily competitor’s prices or get all comments from your company’s Facebook page. [2]

### Requirements

** Note: This tutorial is performed using Python 3.7.9**

1. Install the dependencies as outlined in the `requirements.txt` by running
```
pip install -r requirements.txt
```

2. Update S3 Bucket details

Provide the S3 bucket name in the `bucket_name` parameter in `s3_uploader/upload_models.py`


3. Once Airflow is installed, configure the same by running:

```
# Use your present working directory as
# the airflow home
export AIRFLOW_HOME=~(pwd)

# export Python Path to allow use
# of custom modules by Airflow
export PYTHONPATH="${PYTHONPATH}:${AIRFLOW_HOME}"


# initialize the database
airflow db init

airflow users create \
    --username admin \
    --firstname YourName \
    --lastname YourLastName \
    --role Admin \
    --email example@example.com
```

4. Using Airflow

Start the Airflow server in daemon & Airflow Scheduler
```
airflow webserver -D

airflow scheduler
```

Access the Airflow console by visiting http://127.0.0.1:8080/home on your browser.

To kill the Airflow webserver daemon:
```
lsof -i tcp:8080  

Kill the process by running `kill <PID>` - in this case, it would be `kill 13280`

### Running the Pipeline

Login to Airflow on your browser and turn on the `CNN-Training-Pipeline` DAG from the UI. Start the pipeline by choosing the DAG and clicking on Run.


### API Usage

The API endpoints allow the following:
- Starting the Airflow Webserver & Scheduler
- Starting the training pipeline
- Inference

Start the API server by running
```
cd api
uvicorn main:app --reload
```

API Documentation can be viewed by visiting 127.0.0.1:8000/docs

### Inference

#### Using the Streamlit App

We can validate our retrained model by running the streamlit app which calculates the confidence score for its acne condition for each new uploaded images based on the retrained model with scraped images

The Streamlit app can be used for Inference. Start the server by running `streamlit run app.py` from your terminal. Open the app by visiting http://localhost:8501 on your browser.

You may use the `predict.py` script for inference. Provide the path to your image and run the script.

#### References

https://airflow.apache.org/docs/apache-airflow/stable/index.html
https://medium.com/@dustinstansbury/understanding-apache-airflows-key-concepts-a96efed52b1a
https://towardsdatascience.com/getting-started-with-airflow-locally-and-remotely-d068df7fcb4
