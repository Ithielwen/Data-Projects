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
        if day != "s" or "m" or "t" or "w" or "th" or "f" or "sa" or "all":
            print("ERROR! INVALID ANSWER!")
            continue
        else:
            break
    
    print('-'*40)
    return city, month, day
    
