from quixstreams import Application
import json 

def main():
    print("Starting Quix Streams consumer...")
    app = Application(
        broker_address="localhost:9092",
        loglevel="DEBUG",
        consumer_group="flight_streams",
        auto_offset_reset="earliest",
    )
    
    #Define the consumer to subscrib eto the consumer topic.
    with app.get_consumer() as consumer:
        consumer.subscribe(["Crypto-data"])
        
        while True:
            #Set the poll to 30 seconds to wait for a new message from the producer. 
            msg = consumer.poll(30)
            
            if msg is None:
                print("waiting....")
                
            else:
                key = msg.key().decode("utf-8")
                value = json.loads(msg.value())
                offset = msg.offset()
                print(f"{key}, {value}, {offset}")
                consumer.store_offsets(msg)
        
if __name__ == "__main__":
    main()