import csv
with open('HyperlocalData.csv') as csvfile:
    data = csv.reader(csvfile)
    
    for url in data:
        
        if int(url[1]) > 5:
            print(url[0])
