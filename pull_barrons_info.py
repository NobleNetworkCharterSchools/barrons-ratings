
import os, bs4, csv, itertools  

DATADIR = "/home/pi/projects/barrons/data/downs_full"

input_files_names = os.listdir(DATADIR)
csvFile = open('college.csv', 'w', newline='')
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['College Name', 'Selectivity', 'file_name'])
print("starting")

for file_name in input_files_names:
    if file_name.endswith(".html"):
        print(".", end="", flush=True)
        file = (os.path.join(DATADIR, file_name))
        pull_barrons_infoFile = open(file, 'r')
        pull_barrons_infoContent = pull_barrons_infoFile.read()
        pull_barrons_infoSoup = bs4.BeautifulSoup(pull_barrons_infoContent, "html.parser") 
        th_elements = pull_barrons_infoSoup.select('html #search-profile #page-wrapper div#content-wrapper div#searchleftcol div.searchcontent table.tbl-profile tbody.basic-info tr th')
        try:
            school_name = th_elements[-1].text
            #For a handfull of files, a semicolon is not present in the html file, but gets inserted. 
            school_name = school_name.replace(";", "")
        except IndexError:
            continue

        # Put the names into a spreadsheet.
        #Take the names from the output, separate them by commas(somehow?) place them in a spreadsheet. 
        td_elements = pull_barrons_infoSoup.select('html #search-profile #page-wrapper #content-wrapper #searchleftcol div table tbody.basic-info tr td')
        
        try:
            #Takes the last object in the td list and prints it 
            competitivenes = td_elements[-1].text
    
        except IndexError:
            #if there is no values for td in the file then the code prints "unknown value"
            print("Not Available")
            competitivenes = None 

        if competitivenes == " ": 
            competitivenes = "Was Empty"
    
        #Some files only had an ACT as final list object. No other competitivesnes rating available.
        elif competitivenes.startswith("ACT:"):
            competitivenes = "Not Available"
        #print(school_name, "'"+competitivenes+"'", file_name)
        csvWriter.writerow([school_name, competitivenes, file_name])
print("Finished")
csvFile.close()