import json
import random
import time
from datetime import datetime
from kafka import KafkaProducer
from data_generation import generate_message

def serilizer(message):
    return json.dumps(message).encode('utf-8')

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer = serilizer
)

if __name__ == "__main__":
    while True:
        dummy_message = generate_message()
        
        print(f"Producing message @ {datetime.now()} | message = {str(dummy_message)}")
        producer.send('dummy_topic', dummy_message)
        
        time.sleep(random.randint(1,4))