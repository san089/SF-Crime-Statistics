
# SF-Crime-Statistics

## **STEP 1**
### kafka consumer console output
![Consumer console output
	    ](https://github.com/san089/SF-Crime-Statistics/blob/master/kafka-console-consumer-output.PNG)




## **STEP 2**
### Streaming progress reporter
![Progress Reporter
	    ](https://github.com/san089/SF-Crime-Statistics/blob/master/spark-streaming-progress-report.PNG)



## **STEP 3**

##### 1.  How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

Ans: Experimented with `maxOffsetsPerTrigger`, `inputRowsPerSecond` and `processedRowsPerSecond`. Optimized by experimenting with different value for these parameters and performance tuned the application.

    
##### 2.  What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

Ans: Tuned `spark.sql.shuffle.partitions`, `spark.streaming.kafka.maxRatePerPartition` and `spark.default.parallelism` by following the spark performance tuning documentation(link below).

#### Reference: [https://spark.apache.org/docs/latest/sql-performance-tuning.html](https://spark.apache.org/docs/latest/sql-performance-tuning.html)


### Environment

 - Java 1.8.x
 - Python 3.6 or above
 - Zookeeper
 - Kafka
 - Scala 2.11.x
 - Spark 2.4.x


### How to Run?
#### Start Zookeeper and Kafka Server 
```
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties
```
#### Run Kafka Producer server
`python kafka_server.py`

#### Run the kafka Consumer server 
`python kafka_consumer.py`

#### Submit Spark Streaming Job
`spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_stream.py`
