#!/usr/bin/env python
#Import the same libraries from our first script
import requests
from bs4 import BeautifulSoup
import unicodecsv

#create a base_url that is just the domain and the directories that don't change
base_url = 'https://s3.amazonaws.com/python-at-ire15/death_row/'

#create a new_page variable with the html page name
new_page = 'dr_offenders_on_dr.html'

#concatenate the base_url and new_page into a url variable
url = base_url + new_page

#make a get request
r = requests.get(url)

#assign the r.content to html
html = r.content

#make a soup out of the html
soup = BeautifulSoup(html)

#grab the body text. This is all the same as before
body_text = soup.find("div", id='body')

#pluck out the table from the body_text and assign it to "our_table"
our_table = body_text.find('table')

#find our first tr and assign it to headers
headers = our_table.find('tr')

#make an empty list that will hold our header names
myheaders = []

#make a for loop and append all the text of all the 'th' tags to the myheaders list
for th in headers.find_all('th'):
	myheaders.append(th.text)

#print myheaders out, so you can see how they differ
print myheaders

#create an output file name
output_file = 'deathrow.csv'

#open the f file object
f = open(output_file,'wb')

#create a w writer object
w = unicodecsv.writer(f, encoding='utf-8')

#write our header rows to the csv using w
w.writerow(myheaders)

#grab all the trs after the first in our_table and loop through them
#rename the variables in the right order and add new ones for offensedate, for instance
for tr in our_table.find_all('tr')[1:]:
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
    #gather all the variables into a list
    rowitems = [number, link, last, first, dob, gender, race, indate, county, offensedate]
    #write the list to the csv with w
    w.writerow(rowitems)

#close your f file object
f.close()


