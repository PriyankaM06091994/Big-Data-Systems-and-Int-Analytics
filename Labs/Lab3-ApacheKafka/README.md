## Big Data Systems and Int Analytics

## Labs

#### Team Information

| NAME              |     NUID        |
|------------------ |-----------------|
|   Tanvi Gurav     |   001306848     |
|   Keerti Ojha     |   001050173     |
| Priyanka Malpekar |   001302741     |


## Lab 3 - Getting started with AWS + Lambda

#### CLAAT Link
https://codelabs-preview.appspot.com/?file_id=18gjiG4BLFSI-kqlX1QL7PYNOW0s6KEOY7O972kxY0ME#0

### Lab Completion Date

5th February’21

## About

**This lab demonstrates leveraging and implementing Kafka services for static data along with  real-timeTwitter streaming.**
 
 ## Kafka

**Apache Kafka** is a streaming message platform. It is a publish-subscribe based durable messaging system. Kafka is designed to be high performance, highly available, and redundant. It is used to collect, process, store, and integrate data at scale. A messaging system sends messages between processes, applications, and servers. 

It’s basic use cases includes:
- Stream Processing
- Messaging
- Website Activity Tracking
- Log aggregation
- Event Sourcing
- Application health monitoring

These are four main parts in a Kafka system:

- **Broker:** Handles all requests from clients (producer, consumer and metadata) and keeps data replicated within the cluster. There can be one or more brokers in a cluster
- **Zookeeper:** Keeps track of status of the Kafka clusters (brokers, topics, users)
- **Producer:** Sends records to a broker
- **Consumer:** Consumes batches of records from the broker


## Requirements







### Getting Started

#### Download & Configure Kafka
- Download Apache Kafka from [here](https://kafka.apache.org/downloads)
- Unzip contents of the downloaded file

#### Python Libraries 

- kafka-python - Install the Python client for the Apache Kafka by running `pip3 install kafka-python`. This library is designed to function much like the official java client & can help publish and receive messages from Python. Alternatively, you may use `confluent-kafka-python` as well, but for this exercise, we would be using `kafka-python`.

#### Starting Zookeeper & Kafka Broker

Navigate to the directory where the downloaded files are unzipped and start the Zookeeper service:
```
bin/zookeeper-server-start.sh config/zookeeper.properties
```
Additionally, start the Kafka broker by running:
```
bin/kafka-server-start.sh config/server.properties
```

### Usage

Once the Zookeeper and Kafka broker services are started, we can use the Python scripts on this repo.

#### Using `producer.py`
Run the script to publish events to the newly created topic `sample`

#### Using `consumer.py`
Run the script to consume the events published by the producer. This script should write messages to the console.

## Level UP! :arrow_up:

Let's work with a use-case that collects real-time sampled tweets from [Twitter](twitter.com) and publishes these to a Kafka Broker.

### Requirements

This requires the use of a Twitter Developer account. Apply for one [here](https://developer.twitter.com/en/apply-for-access). Once you have access to your developer account:

- Create a new Project on the dev console
- Generate your API keys and bearer tokens

:warning: Never share your tokens or push them to GitHub

### Usage

Use the `twitter-stream.py` script to fetch tweets using Twitter's API in real-time. Ensure that you enter your bearer token in the script under the `BEARER_TOKEN` param. This script:
- Fetches sampled tweets in real-time.
  
- Publishes these tweets to the Kafka Broker

On running `consumer.py` - you should see all the published events, that are collected by the consumer. 

ß
