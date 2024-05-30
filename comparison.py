#### definition of function that compares the data between two countries (country 1 and 2)

def compare(country1,country2,name1,name2):
    highest1 = country1[0]                   #initialization of variables for highest and lowest vaccine values in country1
    lowest1 = country1[0]
    for item in country1:                    # a for loop is used to determine the lowest and highest values in country1
        if item > highest1:
            highest1 = item
        if item < lowest1:
            lowest_1 = item
    highest2 = country2[0]                 
    lowest2 = country2[0]
    for item in country2:                   # a for loop to determine the highest and lowest value in country2
        if item > highest2:
            highest2 = item
        if item < lowest2:
            lowest2 = item
            
    # this compares the highest and lowest of the two lists
    
    highest = 0
    if highest1 > highest2:                # a conditional statement to determine the highest value of both country1 and country2
        highest = highest1
    else:
        highest = highest2
    if lowest1 < lowest2:
        lowest = lowest1                   # a conditional statement that determines the lowest value of both country1 and country2
    else:
        lowest = lowest2

    difference=highest-lowest                                    # the difference is the comparison between the highest and lowest values to determine the difference in values
    print("\n"+name1+" Highest value: ",highest1,
          "Lowest value: ", lowest1,'\n'+name2+" Highest value: ",
          highest2,"Lowest value: ", lowest2,)
    print(" \n \nThe total highest value is: ",                  # lines of code that outputs the comparison data collected. 
          highest," \nThe total lowest value is:"
          ,lowest,
          " \nThe total difference in vaccinations between the dates: ",difference)
