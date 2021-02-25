### Lab - Snowflake  

#### Requirements

```
To Prepare for our Lab Environment we registered for a Snowflake free 30-day trial and used Snowflake Enterprise Edition, AWS cloud provider, and selected US East region.
```
#### What is Snowflake Data Cloud
Snowflake’s Data Cloud is powered by an advanced data platform provided as Software-as-a-Service (SaaS). Snowflake enables data storage, processing, and analytic solutions 
that are faster, easier to use, and far more flexible than traditional offerings.Snowflake combines a completely new SQL query engine with an innovative architecture natively 
designed for the cloud. To the user, Snowflake provides all of the functionality of an enterprise analytic database, along with many additional special features and unique 
capabilities.


#### Contents
-Preparing to Load Data
-Loading Data
-Analytical Queries, Results Cache, Cloning
-Working With Semi-Structured Data, Views, JOIN
-Time Travelling
-Role based Access Controls

#### Preparing to Load Data
First step is to create a database and table on the Snowflake Cloud
External stage needs to be created to copy data from S3bucket into table created
   ```
    create or replace stage citibike_trips url = 's3://snowflake-workshop-lab/citibike-trips';
   ```
We have to created a file format for data that will be stored in table

#### Loading Data
In order to stage data from S3 into table we need to create datawarehouse using below query
```   
 create or replace warehouse analytics_wh with warehouse_size = 'large' warehouse_type = 'standard' 
     auto_suspend = 600 auto_resume = true;
```
Loading data into table using below query
```    
copy into trips from @citibike_trips file_format=csv;
```

#### Analytical Queries, Results Cache, Cloning
Performed select queries on dataset and checked the results before and after caching
Cloning the existing table using below command
```     
create table trips_dev1 clone trips;
```

#### Working with Semi structured data, views
Load weather data in JSON format held in a public S3 bucket
```     
copy into json_weather_data from @nyc_weather file_format = (type=json);
```
Created a View and query the semi-structured data using SQL dot notation

#### Time Travelling
Restoring weather data after deleting it accidently using below query
```     
undrop table json_weather_data;
```
Rolling back the update action

#### Role based Access Controls
Granting access to user using below query
```
create role junior_dba;
grant role junior_dba to user KEERTI26;-
```





