#Command line interface script v2, Main file(final version)

################### #imported sub-scripts and modules

import argparse #main function used for this script, passing the command line arguments and using them as variables
import sys

import fileHandling #gathers latest data from csv file cointaining vacinnation information

from comparison import compare #metrics that compare the vaccination rollout between the countries

from graphing import threeGraphs #creates and saves plots

####################################### #iso codes are cross checked with users input in the terminal

isoCodes= {'TLS', 'GHA', 'OWID_AFR', 'BES', 'DJI', 'PAN', 'ABW', 'MDV', 'PNG', 'SEN', 'BMU', 'MYS', 'AZE', 'DMA', 'FRO', 'HTI',
'CHN', 'GEO', 'NGA', 'TUN', 'NRU', 'SUR', 'EGY', 'MDG', 'MNG', 'SHN', 'NOR', 'OWID_SAM', 'PSE', 'ZMB', 'COD', 'NAM','CYP', 'CHE',
'EST', 'PYF', 'GUY', 'KHM', 'IND', 'ARM', 'SLB', 'DNK', 'ATG', 'BHS', 'CMR', 'AUT', 'MKD', 'OMN', 'CUW','VUT', 'THA', 'BRA', 'MDA',
'SSD', 'ISL', 'POL', 'SOM', 'GBR', 'CAF', 'FRA', 'GRD', 'MSR', 'ITA', 'BFA', 'UGA', 'JPN', 'KGZ', 'LTU', 'OWID_WRL', 'BHR', 'YEM',
'KWT', 'OWID_OCE', 'AUS', 'NIC', 'CRI', 'OWID_NAM', 'PRY', 'ESP', 'TON', 'SYR', 'COL', 'JAM', 'NZL', 'AFG', 'FIN', 'BIH', 'GAB',
'AND', 'MOZ', 'LAO', 'LBY', 'SDN', 'GGY', 'COG', 'GIN', 'TUR', 'VEN', 'GIB', 'BGR', 'TZA', 'BGD', 'ETH', 'BDI', 'BLR', 'BOL',
'SLV', 'MAC', 'PRT', 'WSM', 'DEU', 'JEY', 'TCD', 'MMR', 'SWZ', 'PER', 'ISR', 'HUN', 'LKA', 'ROU', 'TWN', 'MAR', 'NLD', 'COM', 'MLI',
'SGP', 'UKR', 'LBR', 'KOR', 'AGO', 'MCO', 'BTN', 'LIE', 'LUX', 'LSO', 'SXM', 'PAK', 'VNM', 'FLK', 'ERI', 'OWID_EUR', 'HND', 'TTO',
'GNB', 'BEL', 'CHL', 'QAT', 'USA', 'WLF', 'CZE', 'IRQ', 'ZWE', 'TCA', 'CPV', 'TUV', 'RWA', 'ARG', 'HKG', 'DZA', 'OWID_INT', 'AIA', 'IRN',
'SRB', 'DOM', 'ECU', 'KAZ', 'NPL', 'OWID_KOS', 'MRT', 'LBN', 'LCA', 'BLZ', 'SLE', 'FSM', 'MLT', 'CUB', 'MNE', 'RUS', 'MHL', 'SAU', 'SYC',
'SVN', 'ALB', 'BWA', 'JOR', 'BRN', 'MWI', 'SWE', 'CYM', 'TKM', 'PHL', 'GTM', 'OWID_EUN', 'NCL', 'VAT', 'GRL', 'IMN', 'IDN', 'URY',
'OWID_CYN', 'FJI', 'OWID_ASI', 'BEN', 'TGO', 'GNQ', 'GMB', 'GRC', 'STP', 'UZB', 'CAN', 'KNA', 'IRL', 'ARE', 'CIV', 'LVA', 'MUS', 'ZAF',
'VCT','NER', 'BRB', 'HRV', 'KEN', 'SMR', 'TJK', 'MEX', 'SVK'}

isoCodeString=str(isoCodes) #allows iso code to be viewed in the help menu >>python cli.py -h

save=bool #save/show function is reset

####################################### #main program, command line interface (include argparse fucntion) that communicates user's input to all other scripts

def main():
                
    """Command line entry point:

    $ python cli.py country1 country2 start-date end-date save/show       # required arguments
    $ python cli.py iso1 iso2 yyyy-mm-dd yyyy-mm-dd save/show             # format
  >>> python cli.py gbr fra 2021-04-01 2021-04-10 show                    # example     
    $ python cli.py -h                                                    # help menu (contains iso codes and date format)
    """

    parser=argparse.ArgumentParser(prog="Vaccination Rollout ", description="Input format: isocodes "+isoCodeString+", Date format yyyy-mm-dd, save or show")

    if len(sys.argv)==1: #if user fails to provide any arguments the program stops
        print("""\nYou must provide 5 positional arguments (2 countries , 2 dates: start+end and save/show)""")
        sys.exit(1)

    parser.add_argument("country1",type=str, help="initial of country 1")   #
    parser.add_argument("country2",type=str, help="initial of country 2")   #
    parser.add_argument("date1",type=str, help="start date")                #positional/mandatory arguments
    parser.add_argument("date2",type=str, help="end date")                  #
    parser.add_argument("saveOrShow", type=str, help="saves or shows plot") #
    args=parser.parse_args()

    country1=args.country1.upper() #
    country2=args.country2.upper() #
    date1=args.date1               #user's inputs stored as variable
    date2=args.date2               #
    saveOrShow=args.saveOrShow     #



    if country1 not in isoCodes: #checks if iso code is valid 
        print("Invalid iso code")
        sys.exit(1)
    if country2 not in isoCodes:
        print("Invalid iso code")
        sys.exit(1)


    if saveOrShow.upper()=="SAVE": #saves or shows plot according to user
        save=True
    elif saveOrShow.upper()=="SHOW":
        save=False
    else:
        print("Please specify whether to show or save")
        sys.exit(1)    


    fileHandling.getNewData() #updates the data in the csv file at the cost of a small delay (everytime you run the program, the csv file is updated)

    place1=fileHandling.readCountryData(country1,date1, date2) #retrieves vaccination data between the dates from csv files
    place2=fileHandling.readCountryData(country2,date1, date2) #2 lists are created each cointaing the x and y values for the respective country

    x1=[i[0] for i in place1] # 
    y1=[i[1] for i in place1] #x and y values are 
    x2=[i[0] for i in place2] #seperated into 4 lists
    y2=[i[1] for i in place2] #
    


    compare(y1,y2,country1,country2) #compares data between the countries
    threeGraphs(x1,y1,x2,y2, "Time", "Vaccinated People", country1,country2, save) #creates the plots

########################################

main()
