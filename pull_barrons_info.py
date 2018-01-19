
import os, bs4, csv, itertools  

DATADIR = "/home/pi/projects/barrons/data/downs"

input_files_names = os.listdir(DATADIR)

for file_name in input_files_names:
    if file_name.endswith(".html"):
        file = (os.path.join(DATADIR, file_name))
        pull_barrons_infoFile = open(file, 'r')
        pull_barrons_infoContent = pull_barrons_infoFile.read()
        pull_barrons_infoSoup = bs4.BeautifulSoup(pull_barrons_infoContent, "html.parser") 
        th_elements = pull_barrons_infoSoup.select('html #search-profile #page-wrapper div#content-wrapper div#searchleftcol div.searchcontent table.tbl-profile tbody.basic-info tr th')
        #print(th_elements)
        try:
            school_name = th_elements[0]
            print("school_name: " , school_name.text, type(school_name.text), *school_name, type(*school_name))
        except IndexError:
            print(file_name)
            #print(school_name)
#---------------------------------------------------------------------------------------------------------------------------------------------------------
    # Put the names into a spreadsheet.
#Take the names from the output, separate them by commas(somehow?) plave them in a spreadsheet. 
        td_elements = pull_barrons_infoSoup.select('html #search-profile #page-wrapper #content-wrapper #searchleftcol div table tbody.basic-info tr td')
        reader = csv.reader(file)
#takes the data in td and forms a list with it 
        allRows = [row for row in reader]
        try:
#Takes the last object in the td list and prints it 
            competitivenes = td_elements[-1]
            print("Selectivity: " , *competitivenes)
        except IndexError:
#if there is no values for td in the file then the code prints "unknown value"
            print("Unknown Value")
csvFile = open('college.csv', 'w', newline='')
csvWriter = csv.writer(csvFile)#, delimiter='\t', lineterminator='\n\n')
csvWriter.writerow(['College Name', 'Selectivity'])
csvFile.close()