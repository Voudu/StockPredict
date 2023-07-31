import yfinance as yf
import os

on = True

while on:
    ticker = input("Enter a ticker to get current data: ")

    # try to get the ticker data that was entered by the user
    try:
        data = yf.Ticker(ticker)
        
        print('\n')
        print(data.history(period="1mo"))       # this is a pandas data frame
        print('\n')

        res = input("Do you want to donwload the price data? (Y/N): ")

        if res.lower() == 'y':              
            dl = yf.download(ticker, period="1mo")   # download the data TO RAM not as a file


            currDir = os.getcwd()

            # TEMPORARY BUILD A STRING FOR FILE NAME
            timeperiod = '1mo'
            filename = ticker+timeperiod+'.csv'
            # REMOVE THE 2 LINES ABOVE ONCE THIS IS ABSTRACTED OUT

            filePath = os.path.join(currDir, 'csvs', filename)      # current directory/csvs/filename.csv
            dl.to_csv(filePath) # this downloads the file locally

        # for any other input that wasn't yes go back to beginning

    # catch any exceptions. This will typically just be that ticker name did not exist
    except Exception as e:
        print("There was a problem with the ticker entered. Try again.\n")
    