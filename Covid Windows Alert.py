# Importing required libraries
import requests
from win10toast import ToastNotifier
import datetime

# Testing connection to REST API
try:
    data = requests.get("http://corona-rest-api.herokuapp.com/Api/india")
except:
    print("You are not connected to a network. Please check internet connection.")
    data = None

if data is not None:
    getData = data.json()
    covidPK = getData["Success"]

    # Alert Title 
    title ="""Covid Pakistan / {}""".format(datetime.date.today())
    # Covid statistics
    message="""In Pakistan Covid-19 Cases: {}, Deaths: {}, Recovered: {}, Cases Today: {}""".format(covidPK["cases"],covidPK["deaths"],covidPK["recovered"],covidPK["todayCases"])

    # Assigning Win10Toast to var
    toaster = ToastNotifier()

    # Defining icon image path
    toaster.show_toast(title, message, icon_path="E:\Software\Python 3\Python Projects/covid-icon.ico", duration=10)