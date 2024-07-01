from quixstreams import Application
import logging
from time import sleep


def main():
    logging.info("START...")
    app = Application(
        broker_address="localhost:9092",
        loglevel="DEBUG",
        auto_offset_reset="earliest",
        consumer_group="flight_streams"
    )
    
    input_topic = app.topic("Crypto-data")
    output_topic = app.topic("Crypto-filtered-data")
    
    
    def filter_top_10(stock_data):
        #Outline columns for keeping
        columns_to_keep = ['id', 'rank', 'symbol', 'name', 'priceUsd', 'volumeUsd24Hr']
        
        filtered_list = [
            {k: item[k] for k in columns_to_keep if k in item} 
            for item in stock_data['data'] 
            if int(item['rank']) <= 10
        ]
        
        #Values by price
        sorted_list = sorted(filtered_list, key=lambda x: x['priceUsd'], reverse=True)
        # Return the value with the filtered data
        print(f"{sorted_list}, {stock_data['timestamp']}")
    
    #Streaming dataframe
    sdf = app.dataframe(input_topic) 
    sdf = sdf.apply(filter_top_10)
    sdf.to_topic(output_topic)
    
    #Run the streaming dataframe.
    app.run(sdf)
    
if __name__ == "__main__":
    logging.basicConfig(level="DEBUG")
    main()