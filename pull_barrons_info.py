pull_barrons_infoFile = open("/home/pi/projects/barrons/data/downs/searchpage-profile.cfm_001.html")
#print(dir(pull_barrons_infoFile))
pull_barrons_infoContent = pull_barrons_infoFile.read()
#print(pull_barrons_infoContent) #Prints Everything 
import bs4
pull_barrons_infoSoup = bs4.BeautifulSoup(pull_barrons_infoFile.read(), "html.parser")
print(type(pull_barrons_infoSoup))
print(pull_barrons_infoSoup.prettify())
#th = pull_barrons_infoSoup.select('html body#search-profile.searchpage div#page-wrapper div#content-wrapper div#searchleftcol div.searchcontent table.tbl-profile tbody.basic-info tr')
#td = pull_barrons_infoSoup.select('html body#search-profile.searchpage div#page-wrapper dic#content-wrapper div#searchleftcol div.searchcontent table.tbl-profile tbody.basic-info tr td')
td = pull_barrons_infoSoup.select('html')# body div div div div table tbody tr td')
print(td)
#print(th)
      