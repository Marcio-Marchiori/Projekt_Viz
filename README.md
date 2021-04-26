![phylo](https://user-images.githubusercontent.com/80441475/116099169-139dcc80-a682-11eb-9532-1e0646774d09.jpg)

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

After connecting our PostgreSQL database to Tableau we are finally able to start figuring out the data and finding our insights.

Before diving in the graphics, we need to understand what each score means and its parameters:

* Polarity

Ranges from -1 to 1, -1 being a negative rating, 1 being a positive rating and 0 being the neutral rating.

* Subjectivity

Ranges from 0 to 1 where 0 is very objective and 1 is very subjective.


### The gender comparison

![Box_pol](https://user-images.githubusercontent.com/80441475/116087535-54441880-a677-11eb-9e50-4c668eecf39b.png)

As we can see from this box plot comparison women tend to have a smaller albeit higher Polarity, and while the men do have a significant amount of outliers above the 0.4 mark, women have the only outlier able to crack the 0.6 barrier.

Men on the other hand have the record negative outlier, breaking the negative average polarity record by an astonishing difference.

### Data Density

![Density Map: Average Polarity vs Average Subjectivity](https://user-images.githubusercontent.com/80441475/116091375-219c1f00-a67b-11eb-85b8-bda3135b0e93.png)



From the image we can see that albeit there’s concentration in an area, the data is seemingly scattered over a  considerable area, how can we better visualize it for a better insight? 

![Density Map: Average Polarity vs Average Subjectivity with Median Line and Standard Deviation Band](https://user-images.githubusercontent.com/80441475/116091395-2660d300-a67b-11eb-88e9-624438984511.png)

Plotting the median Line and the Standard Deviation Band we now can see that even though the data might look scattered the majority of it is still close to the median and within 1 Standard Deviation from the mean. 

### Visualizing The Outliers And The Best Candidates For The Campaign


![Best Candidates](https://user-images.githubusercontent.com/80441475/116092576-4d6bd480-a67c-11eb-8d79-8668ee559da6.png)

Now with all the names plotted out we can finally have a better grasp on the outliers, first looking at the lonely Ivan the Terrible on the top left corner as he no only is the candidate with the lowest average polarity, but he is also the one with the highest average subjectivity, that indicates the tweets made about him contained the most subjective content out all of the sample. That would make Ivan a candidate that we don’t really want in our marketing department!

Now looking at the highest average polarity scores we can see that they also rank very high on the subjectivity scale, the 4 most expressive being Al Pacino, Muhammad ibn Musa al-Khwarizmi, Suleiman the Magnificent and Isabella I of Castile. 

From these we can infer that both extremes on the polarity scale are associated with little to no objectivity in their mentions, while the polar opposite, candidates that rank as being mentioned as objectivitive are ranked as neutral or close to when it comes to polarity, we can see Louis XV, Louis XVI and Dmitri Mendeleev fit clearly on that criteria, highly objective but almost neutral when it comes to polarity.

# Conclusion

From the data gathered we can see that if we want to use a beloved figure, there will be a considerable amount of subjectivity in how the overall public perceives those figures. That poses an opportunity to gather engagement through public sentiment and subjectivity. We might even mix the neutral candidates with the most prominent beloved ones to create an expo that would attract public interest and subsequently revitalize the face of the museum.


