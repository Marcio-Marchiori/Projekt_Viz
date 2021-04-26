# The New Face For Your Museum

This project set out to find the new face of a Museum from a list of historically important people from all the human recorded history by scraping Twitter data for mentions and utilizing NLP to categorize the mentions by how each historic figure was perceived by the general public by analyzing two metrics:

* Polarity
* Subjectivity


## Tools used

On this project we used several Python libraries:

* pandas
* sqlalchemy
* dotenv
* os
* tweepy
* psycopg2
* multiprocessing
* logging
* time
* re
* numpy
* TextBlob

While storing and using the data in a PostgreSQL database and Tableau for the visualization.


## Getting Started


The project was divided in 3 phases: Scraping the data and storing it in the database, treating it so it could be used, and finally using Tableau to visualize and get as many insights as possible.

### Scraping the Data

To define what names we were gonna use, we took as reference the [Pantheon Project](https://pantheon.world/data/faq), a project that collects and ranks the top figures from history.

After choosing the names we started using tweepy to get the latest 1000 tweets containg a reference to that person with the parameters that the tweet couldn’t be a retweet and the language should be english and storing in the database, that took a considerate amount of time as Twitter severely limits the amount of both requests and tweets we can retrieve, resetting that amount every 15 minutes.

### Treating the data

Once we collected enough datapoints to make our analysis it was time to clean it to make it easier for our algorithm to process it, we started by removing every link and username mention and subsequently removing other special characters that wouldn’t contribute towards processing the data in a useful manner.

## Data Visualization to Find Insights

After connecting our PostgreSQL database to Tableau we are finally able to start figuring out the data and finding our insights 

### The gender comparison

![Box_pol](https://user-images.githubusercontent.com/80441475/116087535-54441880-a677-11eb-9e50-4c668eecf39b.png)

As we can see from this box plot comparison women tend to have a smaller, albeit higher, Polarity, and while the men do have a significant amount of outliers above the 0.4 mark, women have the only outlier able to crack the 0.6 barrier.

Men on the other hand have the record negative outlier, breaking the negative average polarity record by an astonishing difference.

### Data Density

LINK 2

From the image we can see that albeit there’s concentration in an area, the data is seemingly scattered over a  considerable area, how can we better visualize it for a better insight? 

LINK3

Plotting the median Line and the Standard Deviation Band we now can see that even though the data might look scattered the majority of it is still close to the median and within 1 Standard Deviation from the mean. 
