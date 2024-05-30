#Retrieves data from the csv file

import csv
import requests
import datetime
import sys
   

def getNewData(): # download the latest data from Our World In Data and save it in the data folder
    newData = requests.get("https://covid.ourworldindata.org/data/owid-covid-data.csv")
    open("countriesData/owid-covid-data.csv", "wb").write(newData.content)

def convertDate(date): # simple way to turn YYYY-MM-DD dates into numbers for easy sorting/filtering
    return(int(date.replace("-", ""))) # no need for failsafes as they have already been checked

def dateError(date): # simple function to avoid repeating this code twice
    print("Invalid date:", date)
    print("Please use the YYYY-MM-DD format for start and end dates")
    sys.exit(1)

def checkDate(date): # used to check if input dates are real dates for reading data
    try: # split the date into its parts
        year, month, day = date.split("-")
    except ValueError: # make sure the date has the expected number of parts
        dateError(date)
    try: # check if the date exists
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        dateError(date)

def readFile(file): # a small function to make reading files with the same format easier
    return(csv.reader(file, dialect="excel"))

# These functions handle the data used by the programme
# OWID uses ISO Alpha-3 country codes, so it's also used here
# all dates are expected in YYYY-MM-DD format

def writeCountryData(country, dataList): # save the data to a simplified file for easier future reference
    with open("countriesData/"+country+".csv", "w", newline="") as file:
        csv.writer(file, dialect="excel").writerows(dataList)

def buildCountryData(country): # take the relevant data from the OWID csv and put it in a country file
    with open("countriesData/owid-covid-data.csv") as file:
        fileReader = readFile(file)
        dataList = [[row[3], row[39]] for row in fileReader if row[0] == country] # 3 is the column for dates, 39 for cumulative vaccinations per hundred
    writeCountryData(country, dataList)
    
# having specific country files allows the programme to get data faster without searching the main file
# it also makes it possible for the user to input their own data more easily
# for now this isn't implemented, instead the country files are rebuilt each time

def readCountryData(country, startDate, endDate): # read data from country-specific csv and return it as a list
    for date in startDate, endDate: # make sure dates are valid before trying to read
        checkDate(date)
    if convertDate(startDate) >= convertDate(endDate):
        print("Error: end date is not later than start date")
        sys.exit(1)
    buildCountryData(country) # build country data as part of reading rather than a separate option
    with open("countriesData/"+country+".csv", "r") as file:
        fileReader = readFile(file)
        dataList = []
        for row in fileReader: # this is too long and messy to fit in a list comprehension
            if convertDate(startDate) <= convertDate(row[0]) <= convertDate(endDate): # with YYYYMMDD format, dates can be treated like numbers
                if row[1] != "": # a lot of countries have gaps in data that have to be skipped
                    dataList.append([row[0], float(row[1])]) # data from the csv file is all floats
        return(dataList)
        
# The functions below are tools to help development, not part of the final programme

def listColumns(): # print a list of column titles and their positions in the csv file
    with open("countriesData/owid-covid-data.csv") as file:
        index = 0
        fileReader = readFile(file)
        for item in fileReader.__next__():
            print(index, item)
            index += 1

def getCountryCodes(): # create a set of country codes for reference
    with open("countriesData/owid-covid-data.csv") as file:
        fileReader = readFile(file)
        countries = set([row[0] for row in fileReader if row[0] != "iso_code"])
        print(countries)
