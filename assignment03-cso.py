'''Assignment 03
Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json"

Upload this program to the same repository you used for the XML assignment
Save this assignment as "assignment03-cso.py"
This program should not be a long one
I don't need you to reformat or analyse the data in any way
It should be about 10ish lines long (I have not counted)
You will need to find the dataset in CSO.ie, try economic and then finance.'''

import requests # allows importing using http
import json # import json package

# url for source of data set:
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

def getAll(): # method is getAll - to retrieve all the date
    response = requests.get(url) #let response equal to requesting from the url specified above
    return response.json() # return response in json format

if __name__== "__main__": #allows execution as a  script but not when imported from a  module - safeguarding
    with open("cso.json", "wt") as fp: #save to a file -wt write text, file is fp
        print(json.dumps(getAll()), file=fp) # print as json dumps - fp - file pointer
    # print("Hello, it works")