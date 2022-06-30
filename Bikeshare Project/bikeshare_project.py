"""
Instructor: Charlotte Chaze
Class: Udacity Data Analyst
Semester: Summer 2022
Assignment: Bikeshare Data 
Student: Emma Hungrige
"""

#Import Section
import time
from tracemalloc import start
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

        if city not in ("new york city", "chicago", "washington"):
            print("ERROR! INVALID ANSWER.")
            continue
        else:
            break
    
    #Get user input for month
    while True:
        month = input("Which month would you like to filter by? Please enter January, February, March, April, May, June, or 'all' if you do not have any preference.\n").lower().strip()
        if month not in ("january", "february", "march", "april", "may", "june", "all"):
            print("ERROR! INVALID ANSWER.")
            continue
        else:
            break
    
    #Get user input for day of the week
    while True:
        day = input("Which day of the week would you like to filter by? Please enter either Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or 'all'.\n").lower().strip()
        if day not in ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all"):
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

def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip durations.
    """
    print("Calculating trip durations...\n")
    start_time = time.time()

    #Display total travel time
    total_travel_time = sum(df["Trip Duration"])
    print(f"Total Travel Time: {total_travel_time/86400} days.")

    #Display mean travel time
    avg_travel_time = df["Trip Duration"].mean()
    print(f"Average Travel Time: {avg_travel_time/60} minutes.")

    print("This took %s seconds." % (time.time() - start_time))
    print("-"*40)

def user_stats(df):
    """
    Displays statistics on bikeshare users.
    """

    print("Calculating user statistics...\n")
    start_time = time.time()

    #Display counts of user types
    user_types = df["User Type"].value_counts()
    print(f"User Types:\n {user_types}")

    #Display counts of gender
    try:
        gender_types = df["Gender"].value_counts()
        print(f"Gender Types:\n {gender_types}")
    except KeyError:
        print("Gender Types: NO DATA AVAILABLE FOR THIS MONTH.")
    
    #Display earliest, most recent, and most common birth year
    try:
        earliest = df["Birth Year"].min()
        print(f"Earliest Birth Year: {earliest}")
    except KeyError:
        print("Earliest Birth Year: NO DATA AVAILABLE FOR THIS MONTH.")
    
    try:
        recent = df["Birth Year"].max()
        print(f"Most Recent Birth Year: {recent}")
    except KeyError:
        print("Most Recent Birth Year: NO DATA AVAILABLE FOR THIS MONTH.")
    
    try:
        avg_birth_year = df["Birth Year"].value_counts().idxmax()
        print(f"Most Common Birth Year: {avg_birth_year}")
    except KeyError:
        print("Most Common Birth Year: NO DATA AVAILABLE FOR THIS MONTH.")
    
    print("This took %s seconds." % (time.time() - start_time))
    print("-"*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input("Would you like to start over? Y or N?\n").lower().strip()
        if restart != 'y':
            break

if __name__ == "__main__":
    main() 