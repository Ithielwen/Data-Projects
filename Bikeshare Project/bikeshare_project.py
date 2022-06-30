"""
Instructor: Charlotte Chaze
Class: Udacity Data Analyst
Semester: Summer 2022
Assignment: Bikeshare Data 
Student: Emma Hungrige
"""

#Import Section
import time
import pandas as pd
import numpy as np

#CSV Variable
city_data = { 'Chicago': 'chicago.csv', 'New York City': 'new_york_city.csv', 'Washington': 'washington.csv'}

#Definitions
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        city (str) - name of the city to analyze
        month (str) - name of the month to filter by, or "all" to apply no month filter
        day (str) - name of the day of the week to filter by, or "all" to apply no day filter
    """

    print("Hello! Welcome to the Bikeshare Analysis Program.")
    print()

    #Get user input for the city
    while True:
        city = input("Which city would you like to filter by? Please enter either New York City, Chicago, or Washington.\n").lower().strip()

        if city != "new york city" or "chicago" or "washington":
            print("ERROR! INVALID ANSWER.")
            continue
        else:
            break
    
    #Get user input for month
    while True:
        month = input("Which month would you like to filter by? Please enter January, February, March, April, May, June, or 'all' if you do not have any preference.\n").lower().strip()
        if month != "january" or "february" or "march" or "april" or "may" or "june" or "all":
            print("ERROR! INVALID ANSWER.")
            continue
        else:
            break
    
    #Get user input for day of the week
    while True:
        day = input("Which day of the week would you like to filter by? Please enter either S, M, T, W, Th, F, Sa or 'all'.\n").lower().strip()
        if day != "sunday" or "monday" or "tuesday" or "wednesday" or "thursday" or "friday" or "saturday" or "all":
            print("ERROR! INVALID ANSWER!")
            continue
        else:
            break
    
    print("-"*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Arguments:
        city (str) - name of the city to analyze
        month (str) - name of the month to filter by, or "all" to apply no month filter
        day (str) - name of the day of the week to filter by, or "all" to apply no day filter
    
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    #Load data file into a dataframe
    df = pd.read_csv(city_data[city])

    #Convert start time column to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    #Extract month and day of week from start time column to create new columns
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.weekday_name

    #Filter by month if applicable
    if month != "all":
        #Use index of the months list to get corresponding int
        months = ["January,", "February", "March", "April", "May", "June"]
        month = months.index(month) + 1

        #Filter by month to create the new dataframe
        df = df[df["month"] == month]

    #Filter by week if applicable
    if day != "all":
        #Filter by day of the week to create the new dataframe
        df = df[df["day_of_week"] == day.title()]
    
    return df

def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    """

    print("Calculating the most frequent times of travel...\n")
    start_time = time.time()

    #Display the most common month
    pop_month = df["month"].mode()[0]
    print(f"Most Common Month: {pop_month}")

    #Display the most common day of the week
    pop_day = df["day_of_week"].mode()[0]
    print(f"Most Common Day: {pop_day}")

    #Display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    pop_hour = df["hour"].mode()[0]
    print(f"Most Common Hour: {pop_hour}")

    print("This took %s seconds." % (time.time() - start_time))
    print("-"*40)

def station_stats(df):
    """
    Displays statistics on the most popular stations and trips.
    """

    print("Calculating the most popular stations and trips...\n")
    start_time = time.time()

    #Display most commonly used start station
    start_station = df["Start Station"].value_counts().idxmax()
    print(f"Most Commonly Used Start Station: {start_station}")

    #Display most commonly used end station
    end_station = df["End Station"].value_counts().idxmax()
    print(f"Most Commonly Used End Station: {end_station}")

    #Display most frequent combination of start station and end station trips
    combined_station_trips = df.groupby(["Start Station", "End Station"]).count()
    print(f"Most Commonly Used Combinations of Start Station and End Station Trips: {combined_station_trips}")

    print("This took %s seconds." % (time.time() - start_time))
    print("-"*40)

