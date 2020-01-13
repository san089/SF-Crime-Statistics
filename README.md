# SF-Crime-Statistics

## **STEP 1**
### kafka consumer console output
![Consumer console output
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
	    ](https://github.com/san089/SF-Crime-Statistics/blob/master/kafka-console-consumer-output.PNG)




## **STEP 2**
### Streaming progress reporter
![Progress Reporter
	    ](https://github.com/san089/SF-Crime-Statistics/blob/master/spark-streaming-progress-report.PNG)



## **STEP 3**

1.  How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

Ans: 
    
2.  What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

Ans: 
