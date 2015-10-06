#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import unicodecsv

base_url = 'https://s3.amazonaws.com/python-at-ire15/death_row/'

new_page = 'dr_offenders_on_dr.html'

url = base_url + new_page

r = requests.get(url)

html = r.content

soup = BeautifulSoup(html)

body_text = soup.find("div", id='body')

our_table = body_text.find('table')

headers = our_table.find('tr')
myheaders = []

for th in headers.find_all('th'):
	myheaders.append(th.text)

#everything above this is the same as scrape2_complete.py

#now, let's add another piece to the loop to grab the "occupation" and "record" for each death row inmate who has one listed on his detail page.
#here we need to extend our myheaders list, but passing it a list of two additional column heds, 'occupation' and 'record'
myheaders.extend(['occupation','record'])

#name our output_file
output_file = 'deathrow.csv'

#open the output_file to write binary
f = open(output_file,'wb')

#create our unicodecsv.writer object, w
w = unicodecsv.writer(f, encoding='utf-8')

#write our header row. This should all look very familiar
w.writerow(myheaders)

#start a for loop through the trs in our_table starting with the first row of data
for tr in our_table.find_all('tr')[1:]:
    #the next 11 rows should be the same as the for loop in scrape2_complete.py, grabbing all the same data from the page.
    tds = tr.find_all('td')
    number = tds[0].text
    link = tds[1].find('a').get('href')
    last = tds[2].text
    first = tds[3].text
    dob = tds[4].text
    gender = tds[5].text
    race = tds[6].text
    indate = tds[7].text
    county = tds[8].text
    offensedate = tds[9]

    #here's where things get really interesting. For each row, we want to add another request to the inmate's detail page.
    #But, older inmates don't have a detail page, just a scanned JPG of their bio sheet.
    #so we need a link statement that says if the url of the link variable ends with 'html', proceed, or else say 
    #the record and occupations are in the JPEG file
    if link.endswith('html'):
        #create a new request object that gets the detail page. 
        #(hint: the url uses the base_url and the link variable from the outer loop)
        newreq = requests.get(base_url+link)
        #make a soup of the response content
        newsoup = BeautifulSoup(newreq.content)
        #in the soup, let's look for the tag with the "body" id
        body = newsoup.find(id='body')
        #find the <hr> tag
        hr = body.find('hr')
        #find the first <p> tag after the <hr> tag
        graf = hr.find_next('p')
        #the TDCJ changed how they did things over time, so first try to split the text of the graf on the ":"
        #and grab the second item (the occupation name)
        try: 
            occupation = graf.text.split(':')[1].strip()
        #except, if that doesn't work...
        except:
            #try to split the text on the carriage return ('\r\n')
            try:
                occupation = graf.text.split('\r\n')[1].strip()
            #except if that fails, we'll assume that there is no occupation listed.
            except:
                occupation = ''
        #try to do the same thing for the "record" graf
        #find the next <p> tag after the graf for the occupation
        try:
            #try to split it on the ":"
            record = graf.find_next('p').text.split(':')[1].strip()
        #except, if that fails
        except:
            #try to split it on the '\r\n'
            try: 
                record = graf.find_next('p').text.split('\r\n')[1].strip()
            except:
                record = 'None'
    #now, if the file doesn't end with "html", then we'll use an else statement
    else:
        #set the occupation and record to some filler text like "In JPG"
    	occupation = 'Look in JPG'
    	record = 'Look in JPG'

    #assign all of our collected data variables to a list
    rowitems = [number, link, last, first, dob, gender, race, indate, county, offensedate, occupation, record]
    #write that list to a write with w
    w.writerow(rowitems)

#close our f file object!
f.close()