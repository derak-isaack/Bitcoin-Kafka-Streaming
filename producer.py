from quixstreams import Application
import requests 
import json 
import logging
import time 
import pandas as pd

#Function to get the flight data.
def get_flights_data():
    url = "http://api.coincap.io/v2/assets"

    headers = {
            'Content-Type': 'application/json',
            'Accept-Encoding': 'deflate'
        }

    resp = requests.get(url, headers)
    # print(resp.json().keys())
    # print(resp.json()['data'][0].keys())
    data = resp.json()
        
    #         # Get the first item in the 'data' array to inspect its keys and value types
    # first_item = data['data'][0]
            
    #         # Print keys and their corresponding value types
    # for key, value in first_item.items():
    #     value_type = type(value).__name__
    #     print(f"Key: {key}, Value Type: {value_type}")
    for item in data['data']:
            # Convert numeric fields to appropriate types
            item['rank'] = int(item['rank'])
            item['supply'] = float(item['supply'])
            item['maxSupply'] = float(item['maxSupply']) if item['maxSupply'] else None
            item['marketCapUsd'] = float(item['marketCapUsd'])
            item['volumeUsd24Hr'] = float(item['volumeUsd24Hr'])
            item['priceUsd'] = float(item['priceUsd'])
            item['changePercent24Hr'] = float(item['changePercent24Hr'])
            item['vwap24Hr'] = float(item['vwap24Hr']) if item['vwap24Hr'] else None
            
    return data
    
    # Print the first item's keys and their updated types
# first_item = data['data'][0]
# for key, value in first_item.items():
#         value_type = type(value).__name__
#         print(f"Key: {key}, Value Type: {value_type}")

# resp2 = resp.json()
    # resp2 = resp.json()
    # resp3 = pd.json_normalize(resp2, record_path='data')

# data = get_flights_data()
# data2 = data.

#Define the main function to start the kafka application.
def main():
    app = Application(
        broker_address="localhost:9092",
        loglevel="DEBUG",
        auto_offset_reset="earliest",
    )

    with app.get_producer() as producer:
        while True:
            response = get_flights_data()
            logging.debug("producing message: {}".format(response))
            producer.produce(topic="Crypto-data", 
                            value= json.dumps(response),
                            key="Cryptocurrency",
                            )
            logging.info("flushing...")
            time.sleep(60)

if __name__ == "__main__":
    logging.basicConfig(level="DEBUG")
    main()