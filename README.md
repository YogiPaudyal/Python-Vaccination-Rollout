# Instructions on how to run the program

- Clone the repository
- Begin by opening the terminal within your local cloned repository
- You will need to install requests by doing pip install requests

- Run the python script cli.py (this is the main file)
- You must provide 5 arguments

Command line entry point as such:

    $ python cli.py country1 country2 start-date end-date save/show       # required arguments
    $ python cli.py iso1 iso2 yyyy-mm-dd yyyy-mm-dd save/show             # format
    $ python cli.py gbr fra 2021-04-01 2021-04-10 show                    # example     
    $ python cli.py -h                                                    # help menu (contains iso codes and date format)
    

- This will output a plot (which will be saved or shown)
- A few comparison metrics will also be outputed

- You may rerun the program with different countries (iso codes) or start/end dates
