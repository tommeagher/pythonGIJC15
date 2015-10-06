#!/usr/bin/env python

#import three third-party libraries
#One to handle the http requests to the website

#To parse the html itself, import the BeautifulSoup class from the bs4 module
 
#One to write the resulting data to a csv and deal with any encoding issues.


#declare a variable called "url" and assign the url of the scheduled executions page to it.
#http://python-at-ire15.s3.amazonaws.com/death_row/dr_scheduled_executions.html

#make a get request to the URL and assign the resulting response object to a variable called "r"


#take the content attribute of "r" and assign it to a variable called "html"


#using BeautifulSoup, parse the html and assign it to a variable called "soup"


#find the main body div in the html of "soup"


#within that body text, find the table and assign it to "our_table"


#grab our headers by finding the ('tr') tag in our_table


#create an empty list that we can drop our headers into


#using a for loop, we'll iterate through all the 'th' tags that we find in the 'tr' section of the table

	#we'll append the text inside each 'th' tag to the "myheaders" list


#now we need to name the csv file we want to write. Let's call this variable "output_file"


#we'll open up a file object and call it "f" and we'll pass the open function two parameters, output_file and "wb" for write-binary.


#Now we need to create a unicodecsv.writer object. Let's call this w


#now that we have w, we can write a single row to it, our list of headers


#now another for loop to cycle through all of the body <tr>s after the header in our_table

    #grab all of the <td> tags in the <tr> row

    #assign the text of the first item in the tds list to a variable called date (remember we start counting from 0 in Python)

    #assign to a variable called "link", the 'href' value that we get from the 'a' tag that we find in the second td.

    #grab the text of the third td item, call it last

    #create a "first" variable that will hold the text of the 4th td

    #create "number", this will be assigned the text of the 5th td. Notice a pattern developing here?

    #make this variable "dob". What should we assign to it?

    #create a race variable

    #make an indate variable

    #finally, a variable for the county

    #now, we make a list that stores all of the variables, starting with date, that correspond, in order to our column headers we already wrote.

    #now, write the rowitems list to a row in w


#remember to close our file object f to end the script
