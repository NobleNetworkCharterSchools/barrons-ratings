
"""
The program takes a folder full of HTML files and takes specific
information from each file, such as the Name and Competitiveness, and
then  writes that information to a spreadsheet. 
"""

import os, bs4, csv, itertools  

DATADIR = "/home/pi/projects/barrons/data/downs_full"
DEFAULT_NO_COMP = "Not Available"


def main():
    
    """Main function.
    
    Scrapes each html file for college name and competitivenes
    rating. 
    """
    csvFile = open('college.csv', 'w', newline='')
    csvWriter = create_csvWriter(csvFile)
    input_files_names = os.listdir(DATADIR)
    for file_name in input_files_names:
        if file_name.endswith(".html"):
            print(".", end="", flush=True)
            soup = create_soup(file_name)
            name = college_names(soup)
            if name is None:
                continue
            selectivity = competitivenes(soup)
            
            #print(selectivity)
            
###Writes all the data to the rows.  
        csvWriter.writerow([name, selectivity, file_name])

    print("Finished")
    csvFile.close()
            
            
def create_soup(file_name):
    """
    Opens each of the html files and creates a soup object.
    """
    file = (os.path.join(DATADIR, file_name))
    pull_barrons_infoFile = open(file, 'r')
    pull_barrons_infoContent = pull_barrons_infoFile.read()
    pull_barrons_infoSoup = bs4.BeautifulSoup(
        pull_barrons_infoContent, "html.parser"
    ) 
    ###Finds and takes the College names from each of the files if present.
    return pull_barrons_infoSoup 
    
    

def college_names(soup):
    """
        Takes the names of each of the colleges from the files.
    """
    
    th_elements = soup.select('html #search-profile #page-wrapper div#content-wrapper div#searchleftcol div.searchcontent table.tbl-profile tbody.basic-info tr th')
    try:
        school_name = th_elements[-1].text
        #For a handfull of files, a semicolon is not present in the html file, but gets inserted. 
        school_name = school_name.replace(";", "")
    except IndexError:
        return None 
    ###
    
    return school_name 


def competitivenes(soup):
    """
        Takes the competitiveness rating for each of the files if available.
    """
    td_elements = soup.select('html #search-profile #page-wrapper #content-wrapper #searchleftcol div table tbody.basic-info tr td')
            
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
    return competitivenes
                

    
def create_csvWriter(csvFile):
    """
    Generates the spreadsheet, and writes the header row.     
    """
    csvWriter = csv.writer(csvFile)
    #Creates the rows on the spreadsheet in which the data will be writen in.
    csvWriter.writerow(['College Name', 'Selectivity', 'file_name'])
    print("starting")
    return csvWriter


if __name__ == "__main__":
    main()
    #open_files()
    #write_data()