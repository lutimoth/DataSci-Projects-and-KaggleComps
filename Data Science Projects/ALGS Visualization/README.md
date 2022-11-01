<p align="center">
  <img src="./images/algs-2-0-featured-image.jpg.adapt.crop16x9.1023w.jpg" width=60% height=60%>
</p>

# Apex Legends Global Series Data Scraping Project

This project scraped web data from the Apex Legends Global Series (ALGS) Year 2 (spanning 2021-2022) season for the purposes of data visualization and submission into the IronViz competition.

The data is openly available on [Liquidpedia ALGS 2021-2022 Data](https://liquipedia.net/apexlegends/Apex_Legends_Global_Series/2022/Championship). I scraped the data for the purposes of creating visualizations in Tableau. The final visualization can be found at the following link to my [IronViz Tableau Public link](https://public.tableau.com/app/profile/timothy.lu3564/viz/TimothyLu_ALGS_IronVizFinal/algs?publish=yes).

## ALGS Overview

The ALGS tournament is played in the game Apex Legends, an on-line Battle Royale developed by Respawn and published by Electronic Arts. This tournament has multiple stages held on-line in multiple regions simultaneously leading up to 2 major in-person LAN tournaments. 

The 5 major regions are: North America, South America, EU/Middle East, Asia-Pacific North, Asia-Pacific South.

There are 4 major components in ALGS:

<p align="center">

|  ALGS Stage        |                    Amount of Games           |
|:------------------:| :-------------------------------------------:|
| Preseason Qualifier| Multiple weeks of gaming to qualify          |
| Split 1            | Challenger Circuit, Playoffs, Pro League     |
| Split 2            | Challenger Circuit, Pro League, LAN Playoffs |
| Championship       | Last-Chance Qualifier, LAN Championship      | 

</p>

To collect the data efficiently, I started by breaking down the overall structure of the ALGS tournament then took a methodical approach to collecting the data. This leads us to the process of data scraping.

## Data Scraping Process
I built out the scraper initially using BeautifulSoup as a means of understanding the overall structure of the website. This was followed by utilizing Pandas's built-in `read_html` function in order to more efficiently gather tables. 

Pandas' `read_html` creates a list of *all* tables in the given URL. I then found which items in that list were relevant. Since some pages contained multiple tables, I would have to iterate through these tables. Since the process was so repetitive, I wrote a custom function that would capture most cases and greatly speed up the process of collection. There were some exceptions such as the "finals" having only one table. 

I took this list of tables and converted them to dataframes and then saved them in CSV files. Thanks to my function, I was able to iterate by region and by round in other to gather data quickly. I found a few notable exceptions in some regions where the table numbers were slightly different. I adapted to those and manually collected the few exceptions. 

<p align="center">
  <img src="./images/data_scrape_codesnip.png" width=75% height=75%>
</p>

I'll briefly mention one example with the Preseason Qualifier as the other processes were similar. I was able to iterate by each region, then by each preseason qualifier round (there were 4), then collect the data for each preseason qualifier round (usually 4-6 rounds), and collect the data for each lobby in that round (up to 32 lobbies ending with 1 lobby for the final).

After collecting the data, I noticed that for some tables the website actually contained 2 sets of data. Teams get points for placement (where they finish the game) and kills. The tables were designed to toggle between either showing placement or the points given for placement. This caused duplicate data. I then set a process in place that would clean that data as shown below. 

## Data Cleaning Process
I cleaned the tables by remove extraneous columns and renaming column titles so that the tables can be grouped together more easily.

There were different cleaning processes depending on the table.

## Data Grouping Process
I grouped the csv files in multiple stages. First by each individual game, then by region, then by all the regions together.

Some of the regions had slightly different formats and thus slightly different processes for grouping.
