#Startup script

def start():
    options=input("""\nPress 1 to select the 2 countries you would like to compare
Press 2 to view list of countries
Press 3 to exit program
=> """)
    if options=="1":
        country1=input("\nPlease enter the initials for the 1st country: ")
        country2=input("Please enter the initials for the 2nd country: ")
  

    elif options=="2":
        print("""\nPlease enter these initials at the country select menu:
GB= United Kingdom
US= United States of America
BR= Brazil
IN= India
FR= France
RU= Russia
IT= Italy
TR= Turkey
ES= Spain
DE= Germany""")


start()
