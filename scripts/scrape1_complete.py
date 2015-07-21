#!/usr/bin/env python

#import three third-party libraries
#One to handle the http requests to the website
import requests
#To parse the html itself, import the BeautifulSoup class from the bs4 module
from bs4 import BeautifulSoup
#One to write the resulting data to a csv and deal with any encoding issues.
import unicodecsv

#declare a variable called "url" and assign the url of the scheduled executions page to it.
url = 'https://s3.amazonaws.com/python-at-ire15/death_row/dr_scheduled_executions.html'

#make a get request to the URL and assign the resulting response object to a variable called "r"
r = requests.get(url)

#take the content attribute of "r" and assign it to a variable called "html"
html = r.content

#using BeautifulSoup, parse the html and assign it to a variable called "soup"
soup = BeautifulSoup(html)

#find the main body div in the html of "soup"
body_text = soup.find("div", id='body')

#within that body text, find the table and assign it to "our_table"
our_table = body_text.find('table')

#grab our headers by finding the ('tr') tag in our_table
headers = our_table.find('tr')

#create an empty list that we can drop our headers into
myheaders = []

#using a for loop, we'll iterate through all the 'th' tags that we find in the 'tr' section of the table
for th in headers.find_all('th'):
	#we'll append the text inside each 'th' tag to the "myheaders" list
    myheaders.append(th.text)

#now we need to name the csv file we want to write. Let's call this variable "output_file"
output_file = 'scheduled.csv'

#we'll open up a file object and call it "f" and we'll pass the open function two parameters, output_file and "wb" for write-binary.
f = open(output_file,'wb')

#Now we need to create a unicodecsv.writer object. Let's call this w
w = unicodecsv.writer(f, encoding='utf-8')

#now that we have w, we can write a single row to it, our list of headers
w.writerow(myheaders)

#now another for loop to cycle through all of the body <tr>s after the header in our_table
for tr in our_table.find_all('tr')[1:]:
    #grab all of the <td> tags in the <tr> row
    tds = tr.find_all('td')
    #assign the text of the first item in the tds list to a variable called date (remember we start counting from 0 in Python)
    date = tds[0].text
    #assign to a variable called "link", the 'href' value that we get from the 'a' tag that we find in the second td.
    link = tds[1].find('a').get('href')
    #grab the text of the third td item, call it last
    last = tds[2].text
    #create a "first" variable that will hold the text of the 4th td
    first = tds[3].text
    #create "number", this will be assigned the text of the 5th td. Notice a pattern developing here?
    number = tds[4].text
    #make this variable "dob". What should we assign to it?
    dob = tds[5].text
    #create a race variable
    race = tds[6].text
    #make an indate variable
    indate = tds[7].text
    #finally, a variable for the county
    county = tds[8].text
    #now, we make a list that stores all of the variables, starting with date, that correspond, in order to our column headers we already wrote.
    rowitems = [date, link, last, first, number, dob, race, indate, county]
    #now, write the rowitems list to a row in w
    w.writerow(rowitems)

#remember to close our file object f to end the script
f.close()