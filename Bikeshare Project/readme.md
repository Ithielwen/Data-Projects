# Project Overview
In this project, we make use of Python to explore data related to bike share systems for three major cities
in the United States - Chicago, New York City, and Washington. A script has been written to import the data
and answer interesting questions about it by computing descriptive statistics. The script also takes in raw 
input to create an interactive experience in the termincal to present these statistics.

# The Datasets
The datasets are provided by Motivate, a bike share system provider in the United States, and contains 
randomly selected data for the first six months of 2017 for all three cities. The data files for all three
cities contains the same core six columns:
1. Start Time
2. End Time
3. Trip Duration
4. Start Station
5. End Station
6. User Type

The Chicago and New York City files also have the following two columns:
1. Gender
2. Birth Year

# Statistics Computed
The written script provides the following information:
1. Popular times of travel
  a. Most common month
  b. Most common day of the week
  c. Most common hour of the day
  
2. Popular Stations and Trips
  a. Most common start station
  b. Most common end station
  c. Most common trip from start to end
  
3. Trip Durations
  a. Total travel time
  b. Average travel time

4. User Information
  a. Counts of each user type
  b. Counts of each gender (only available for NYC and Chicago)
  c. Earliest, most recent, and most common birth year (only available for NYC and Chicago)

# How to Run the Project
Download zipped folder
Run python bikeshare_project.py
  
# References
https://github.com/beingjainparas/Udacity-Explore_US_Bikeshare_Data
https://github.com/khaledimad/Explore-US-Bikeshare-Data
https://stackoverflow.com/questions/60214194/error-in-reading-stock-data-datetimeproperties-object-has-no-attribute-week
