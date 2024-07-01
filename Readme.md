![Bitcoin](https://img.shields.io/badge/Bitcoin-F7931A?logo=bitcoin&logoColor=fff&style=for-the-badge)
![kafka](https://img.shields.io/badge/Apache%20Kafka-231F20?logo=apachekafka&logoColor=fff&style=for-the-badge)

![Bitcoin](images/bitcoin2.jpg)

## <div style="padding: 20px;color:white;margin:10;font-size:90%;text-align:left;display:fill;border-radius:10px;overflow:hidden;background-image: url(https://w0.peakpx.com/wallpaper/957/661/HD-wallpaper-white-marble-white-stone-texture-marble-stone-background-white-stone.jpg)"><b><span style='color:black'> Project Overview</span></b> </div>

Stream `Real-time` prices of bitcoin prices with a higher ranking on a `one-minute` interval using `Apache Kafka`.Streaming is enabled by use of the `CoinCap API` which displays real-time data of bitcoin prices. 

Filter and transform the streaming data to only include the top ten ranked Bitcoins and order their prices in descending order. 

## <div style="padding: 20px;color:white;margin:10;font-size:90%;text-align:left;display:fill;border-radius:10px;overflow:hidden;background-image: url(https://w0.peakpx.com/wallpaper/957/661/HD-wallpaper-white-marble-white-stone-texture-marble-stone-background-white-stone.jpg)"><b><span style='color:black'> Producer</span></b> </div>

The producer uses the `CoinCap API` to extract bitcoin prices on a one minute interval then later publishes the data to a `Kafka topic` for subscription by the consumer. 

Before data is ingeted into the kafka-topics, it is essential to change the data types from string to their respective data types for easier process of analysis and filtering of streaming data.

## <div style="padding: 20px;color:white;margin:10;font-size:90%;text-align:left;display:fill;border-radius:10px;overflow:hidden;background-image: url(https://w0.peakpx.com/wallpaper/957/661/HD-wallpaper-white-marble-white-stone-texture-marble-stone-background-white-stone.jpg)"><b><span style='color:black'> Consumer</span></b> </div>

The consumer subcribes to the `producer topic` and can be found [here](consumer_final.py). 

## <div style="padding: 20px;color:white;margin:10;font-size:90%;text-align:left;display:fill;border-radius:10px;overflow:hidden;background-image: url(https://w0.peakpx.com/wallpaper/957/661/HD-wallpaper-white-marble-white-stone-texture-marble-stone-background-white-stone.jpg)"><b><span style='color:black'> Transformer</span></b> </div>

The transformer filters the streaming data to only include the top ten bitcoin as well as filter the column names to have the neceesary columns for further analysis. It can be found [here](transformer_final.py). 

The following snippet shows how data moves downstream.
![transfomed](<images/Screenshot (1197).png>)