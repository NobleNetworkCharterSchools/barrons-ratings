
"""
The program takes a folder full of HTML files and takes specific
information from each file, such as the Name and Competitiveness, and
then  writes that information to a spreadsheet. 
"""

import os, bs4, csv, itertools  

DATADIR = "/home/pi/projects/barrons/data/downs_full"
DEFAULT_NO_COMP = "Not Available"


def scrape_files():
    
    """
        Scrapes each html file for college name and competitivenes rating. 
    """
    csvWriter = create_csvWriter()
    input_files_names = os.listdir(DATADIR)
    for file_name in input_files_names:
        if file_name.endswith(".html"):
            print(".", end="", flush=True)
            
            
            ###Opens the files, and creates the Soup object.
            file = (os.path.join(DATADIR, file_name))
            pull_barrons_infoFile = open(file, 'r')
            pull_barrons_infoContent = pull_barrons_infoFile.read()
            pull_barrons_infoSoup = bs4.BeautifulSoup(pull_barrons_infoContent, "html.parser") 
            ###
            
            
            ###Finds and takes the College names from each of the files if present.
            th_elements = pull_barrons_infoSoup.select('html #search-profile #page-wrapper div#content-wrapper div#searchleftcol div.searchcontent table.tbl-profile tbody.basic-info tr th')
            try:
                school_name = th_elements[-1].text
                #For a handfull of files, a semicolon is not present in the html file, but gets inserted. 
                school_name = school_name.replace(";", "")
            except IndexError:
                continue
            ###
            
            
            ###Finds an takes the competitiveness of each of the files if present. 
            td_elements = pull_barrons_infoSoup.select('html #search-profile #page-wrapper #content-wrapper #searchleftcol div table tbody.basic-info tr td')
            
            try:
                #Takes the last object in the td list and prints it 
                competitivenes = td_elements[-1].text
        
            except IndexError:
                #if there is no values for td in the file then the code prints "unknown value"
                print("Not Available")
                competitivenes = None 
                #If none present, writes none available
            if competitivenes == " ": 
                competitivenes = DEFAULT_NO_COMP
        
            #Some files only had an ACT as final list object. No other competitivesnes rating available.
            elif competitivenes.startswith("ACT:"):
                competitivenes = DEFAULT_NO_COMP
            ###
                
                ###Writes all the data to the rows.  
            csvWriter.writerow([school_name, competitivenes, file_name])
                ###
    print("Finished")

    csvFile.close()
def create_csvWriter():
    """
    Generates the spreadsheet, and writes the header row.     
    """
    csvFile = open('college.csv', 'w', newline='')
    csvWriter = csv.writer(csvFile)
    #Creates the rows on the spreadsheet in which the data will be writen in.
    csvWriter.writerow(['College Name', 'Selectivity', 'file_name'])
    print("starting")
    return csvWriter

if __name__ == "__main__":
    scrape_files()
    