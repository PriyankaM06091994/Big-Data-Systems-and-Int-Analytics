## Airflow TFX

From https://www.tensorflow.org/tfx/tutorials/tfx/airflow_workshop <br>
Codebase available here: https://github.com/tensorflow/tfx/tree/master/tfx/examples/airflow_workshop

This lab demonstrates the functionalities of Airflow to programmatically automate, author, schedule and monitor workflows. 

###pic

- Airflow is a platform to programmatically automate, schedule and monitor workflows. 
- In Airflow, a DAG – or a Directed Acyclic Graph – is a collection of all the tasks you want to run, organized in a way that reflects their relationships and   dependencies. 
- The Airflow scheduler executes your tasks on an array of workers while following the specified dependencies. 
- Rich command line utilities make performing complex surgeries on DAGs a snap. 
- The rich user interface makes it easy to visualize pipelines running in production, monitor progress, and troubleshoot issues when needed. 



#### Experiment Setup

1. Create a new project and install the required dependencies.

```
pip install apache-airflow.
```
2. export AIRFLOW_HOME - Enter the path of the present working directory

3. Initialize the instance.

```
airflow db init
```

4. Create an admin user.

airflow users create \
    --username admin \
    --firstname YourName \
    --lastname YourLastName \
    --role Admin \
    --email example@example.com

5. Start the Daemon in the background. It usually runs on port 8080.

```
airflow webserver -D
```

6. To check whether Airflow Daemon is running:

List the services running on port 8080

lsof -i tcp:8080 

7. Start the Airflow Scheduler

```
airflow scheduler
```

Once both are running - you should be able to access the Airflow UI by visiting http://127.0.0.1:8080/home on your browser.

8. To kill the Airflow webserver daemon:

```
lsof -i tcp:8080  
```

Kill the process by running `kill <PID>`

9. Create folder dags inside AIRFLOW_HOME

Place the python file under the ‘dags’ folder.

- Dags can be scheduled and run every minute or hourly/daily
- You can also pause/unpause the dag depending on the requirement

