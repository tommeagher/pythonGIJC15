#!/usr/bin/env python


























#everything above this is the same as scrape2_complete.py

#now, let's add another piece to the loop to grab the "occupation" and "record" for each death row inmate who has one listed on his detail page.
#here we need to extend our myheaders list, but passing it a list of two additional column heds, 'occupation' and 'record'


#name our output_file


#open the output_file to write binary


#create our unicodecsv.writer object, w


#write our header row. This should all look very familiar


#start a for loop through the trs in our_table starting with the first row of data

    #the next 11 rows should be the same as the for loop in scrape2_complete.py, grabbing all the same data from the page.












    #here's where things get really interesting. For each row, we want to add another request to the inmate's detail page.
    #But, older inmates don't have a detail page, just a scanned JPG of their bio sheet.
    #so we need a link statement that says if the url of the link variable ends with 'html', proceed, or else say 
    #the record and occupations are in the JPEG file

        #create a new request object that gets the detail page. 
        #(hint: the url uses the base_url and the link variable from the outer loop)

        #make a soup of the response content

        #in the soup, let's look for the tag with the "body" id

        #find the <hr> tag

        #find the first <p> tag after the <hr> tag

        #the TDCJ changed how they did things over time, so first try to split the text of the graf on the ":"
        #and grab the second item (the occupation name)


        #except, if that doesn't work...

            #try to split the text on the carriage return ('\r\n')


            #except if that fails, we'll assume that there is no occupation listed.


        #try to do the same thing for the "record" graf
        #find the next <p> tag after the graf for the occupation

            #try to split it on the ":"

        #except, if that fails

            #try to split it on the '\r\n'




    #now, if the file doesn't end with "html", then we'll use an else statement

        #set the occupation and record to some filler text like "In JPG"



    #assign all of our collected data variables to a list

    #write that list to a write with w


#close our f file object!
