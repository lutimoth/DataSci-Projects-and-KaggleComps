<p align="center">
  <img src="./images/algs-2-0-featured-image.jpg.adapt.crop16x9.1023w.jpg" width=60% height=60%>
</p>

# Apex Legends Global Series Data Scraping Project

This project scraped web data from the ALGS Year 2 season for the purposes of data visualization and submission into the IronViz competition.

The data is openly available on [Liquidpedia ALGS 2021-2022 Data](https://liquipedia.net/apexlegends/Apex_Legends_Global_Series/2022/Championship) and is publically available. I scraped the data so that it can be used in Tableau for data visualization. The final visualization can be found at the following link to my [IronViz Tableau Public link](https://public.tableau.com/app/profile/timothy.lu3564/viz/TimothyLu_ALGS_IronVizFinal/algs?publish=yes).

## Data Scraping Process
I built out the scraper initially using BeautifulSoup as a means of understanding the overall structure of the website. This was followed by utilizing Pandas's built-in html reader in order to more efficiently gather tables.

I wrote custom functions which would grab all the tables from the Liquidpedia website and convert them to Pandas dataframes before saving them to a csv file.

## Data Cleaning Process
I cleaned the tables by remove extraneous columns and renaming column titles so that the tables can be grouped together more easily.

There were different cleaning processes depending on the table.

## Data Grouping Process
I grouped the csv files in multiple stages. First by each individual game, then by region, then by all the regions together.

Some of the regions had slightly different formats and thus slightly different processes for grouping.
