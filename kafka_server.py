import producer_server
import time


def run_kafka_server():
	# TODO get the json file path
    input_file = "police-department-calls-for-service.json"

    # TODO fill in blanks
    producer = producer_server.ProducerServer(
        input_file=input_file,
        topic="police.service.calls",
        bootstrap_servers="localhost:9092",
        client_id=None
    )
    
    if producer.bootstrap_connected():
        print("Connected to bootstrap")
    
    return producer


def feed():
    producer = run_kafka_server()
    try:
        producer.generate_data()
    except:
        producer.counter = 0
        producer.flush()
        producer.close()


if __name__ == "__main__":
    start = time.time()
    feed()
    end = time.time()
    print(f"Program start time : {start}\nProgram end time : {end}\nExecution time : {round(end - start,2)}")
