### Lab - GCP-Datalab/Dataflow/BigQuery 

#### Requirements

```
-In the Google Cloud Console, on the project selector page, select or create a Google Cloud project.
-Enabled the BigQuery, AI Platform, Cloud Source Repositories, Dataflow, and Datalab APIs.
```
#### What is GCP
Google Cloud Platform (GCP), offered by Google, is a suite of cloud computing services that runs on the same infrastructure that Google
uses internally for its end-user products, such as Google Search, Gmail, file storage, and YouTube. Alongside a set of management tools,
it provides a series of modular cloud services including computing, data storage, data analytics and machine learning.


#### Dataset
We used public Natality dataset to create an ML model to predict a baby's weight given a number of factors about the pregnancy and the baby's mother.
```
We cloned the https://github.com/GoogleCloudPlatform/training-data-analyst github path and used training-data-analyst/blogs/babyweight/babyweight.ipynb 
notebook for our data processing and model creation.
```
#### Launching Datalab

Open Cloud Shell. Unless otherwise noted, you execute the rest of the tutorial from inside Cloud Shell.

Run the following command to retrieve your project ID. Make a note of it for use later in this tutorial.
``` 
gcloud config list project --format "value(core.project)"
```
Create a Datalab instance:
```
datalab create --zone us-central1-a mydatalab
```
It can take a minute or more to create the instance. After the instance is created, Datalab displays the following output.
```
The connection to Datalab is now open and will remain
until this command is killed.
Click on the *Web Preview* (up-arrow button at top-left), select
*port 8081*, and start using Datalab.
We have to created a file format for data that will be stored in table
```

#### Perform preprocessing and Visualization
-Project ID and Bucket setup in notebook
```
BUCKET = 'sunlit-adviser-303301-ml'
PROJECT = 'sunlit-adviser-303301'
REGION = 'us-central1'
```
-In the first cell, set the variable PROJECT to your project ID.
-Set the variable BUCKET to your bucket name in the first cell. For your bucket name, use your project ID as a prefix and my-bucket:
 project-ID-my-bucket
-Leave REGION as us-central1.

#### Preprocessing using apache beam
We modified the data such that we can simulate what is known if no ultrasound has been performed. If I didn't need preprocessing, 
I could have used the web console. Also, I prefer to script it out rather than run queries on the user interface. 
Therefore, I am using Cloud Dataflow for the preprocessing.



