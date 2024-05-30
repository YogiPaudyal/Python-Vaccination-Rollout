#!/usr/bin/env python
#Function that graphs the plot using the given real data

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def threeGraphs(A, B, C, D, xAxis, yAxis, country1, country2, save):    #this creates the the function called threeGraphs and all the inputs required to call it
    difference = []                         #creates a list called diffferent
    for i in range(len(B)):                 #runs the for loop the number of times equal to the length of the list
        difference.append(B[i]-D[i])        #adds the difference of the two numbers to the new list
    gs = gridspec.GridSpec(2, 2)            #creates a 2x2 gridspace
  
    plt.figure()                                    #creates a figure
    plt.rcParams['font.size'] = '6'                 #changes the fontsize on the plot to 6
    ax = plt.subplot(gs[0, 0])                      #creates a plot in the top left corner of the gridspace
    plt.plot(A,B,'tab:blue')                        #plots a against b in blue on the plot
    plt.grid(b=True, which='major', axis='both')    #created gridlines
    plt.ylabel(yAxis)                               #gives the y axis the label of yAxis variable
    plt.title(country1, loc='center')               #gives the plot the title of country1 variable
    plt.xticks(rotation = 90)                       #rotates the points on the x axis by 90 degrees
    
    ax = plt.subplot(gs[0, 1])                      #creates a plot in the top right corner of the gridspace
    plt.plot(C,D,'tab:red')                         #plots C against D in blue on the plot
    plt.grid(b=True, which='major', axis='both')    #created gridlines
    plt.title(country2, loc='center')               #gives the plot the title of country2 variable
    plt.ylabel(yAxis)                               #gives the y axis the label of yAxis variable
    plt.xticks(rotation = 90)                       #rotates the points on the x axis by 90 degrees

    ax = plt.subplot(gs[1, :])                          #creates a plot in the bottom of the gridspace, left and right corner
    plt.plot(A,difference,'tab:green')                  #plots C against D in blue on the plot
    plt.grid(b=True, which='major', axis='both')        #created gridlines
    plt.ylabel("Difference in "+yAxis)                  #gives the y axis the label of "difference in "+yAxis variable
    plt.title((country1+" - "+country2), loc='center')  #gives the plot the title of country1+" - "+country2 variables
    plt.xticks(rotation = 90)                           #rotates the points on the x axis by 90 degrees
    plt.tight_layout()                                  #fix the layout
    if save == True:                                    #checks if save is true from thr inputs
        fileName = country1+" vs "+country2+".png"      #if save is true it creates a file name from the inputs of the function
        plt.savefig(fileName, dpi=300)                           #then saves all 3 graphs on 1 screen
    plt.show()                                          #shows the plot

