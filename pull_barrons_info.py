
import os, bs4, csv 
directory = os.listdir("/home/pi/projects/barrons/data/downs")
for file in directory:
    if file.endswith(".html"):
        pull_barrons_infoFile = open(file)
        pull_barrons_infoContent = pull_barrons_infoFile.read()
        pull_barrons_infoSoup = bs4.BeautifulSoup(pull_barrons_infoContent, "html.parser")
        th = pull_barrons_infoSoup.select('html #search-profile #page-wrapper div#content-wrapper div#searchleftcol div.searchcontent table.tbl-profile tbody.basic-info tr th')
#---------------------------------------------------------------------------------------------------------------------------------------------------------
    # Put the names into a spreadsheet.
#Take the names from the output, separate them by commas(somehow?) plave them in a spreadsheet. 
        #td = pull_barrons_infoSoup.select('html #search-profile #page-wrapper #content-wrapper #searchleftcol div table tbody.basic-info tr td')
        #print(td)
        print(th)
#print(dir(pull_barrons_infoFile))
##pull_barrons_infoContent = pull_barrons_infoFile.read()
#print(pull_barrons_infoContent) #Prints Everything 
#import bs4
#pull_barrons_infoSoup = bs4.BeautifulSoup(pull_barrons_infoContent, "html.parser")
#print(type(pull_barrons_infoSoup))
        #print(file)
#th = pull_barrons_infoSoup.select('html #search-profile #page-wrapper div#content-wrapper div#searchleftcol div.searchcontent table.tbl-profile tbody.basic-info tr th')
    #td = pull_barrons_infoSoup.select('html #search-profile #page-wrapper #content-wrapper #searchleftcol div table tbody.basic-info tr td')
#td = pull_barrons_infoSoup.select('html')#body div div div div table tbody tr td')
#print(td)
#print(th)
      
