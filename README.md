# barrons-ratings
Pull ratings from Barrons site files

Program open multiple HTML files located in a given folder, and scrapes the college name and competitiviness rating from each of the files. Then records all of the data on a spreadsheet. Files were pulled from 

## Requirements
- Python 3.5
- Beautiful Soup
- Requests

## Usage

The project direcory must be changed in the script by editing the DATADIR variable, and the files must end in .html.

The files must have the names of each of the colleges found as the first and only TH value, and the competitiveness rating as the final TD value. The files being used are all files containing information on different universities. 

When run it save the competitiveness, and the name of the university to a csv file "college.csv". In the case that some files do not have the information "Not Available" is printed in its place. 

### About 
Completed in the Spring of 2018 as a Senior internship project. 

Author: Edwin Vallecillo 
