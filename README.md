#Scraping in the Newsroom with Python
##At [GIJC 2015](http://gijc2015.org/) in Lillehammer, Norway.

Before class, be sure [you've installed Python 2.7](PRE-CLASS.md) and all the necessary tools. 

Here's a rough outline of the five, one-hour sessions. Follow along along with the slides: [Day One](http://www.tommeagher.com/pythonGIJC15) and [Day Two](http://www.tommeagher.com/pythonGIJC15/daytwo.html).

##[Day One](http://www.tommeagher.com/pythonGIJC15) with [Tommy Kaas](http://www.kaasogmulvad.dk/)
###Hour One:
* Why code at all, and why Python?
* [Everything](https://github.com/tommeagher/pythonGIJC15/blob/master/scripts/day_one/the_basics.py) you need to know about programming you probably already learned in Excel: Strings, ints, floats, variables, and lists.
* How the hell do you scrape a website? A quick exercise in breaking down a problem into its components and writing functions.

###Hour Two:
* We'll be scraping the Texas Department of Criminal Justice's website for its [its list of scheduled executions](http://tdcj.state.tx.us/death_row/dr_scheduled_executions.html). Because we don't want to hammer the TDCJ website, I've mirrored the pages on s3. We'll be scraping [the scheduled executions](https://s3.amazonaws.com/python-at-ire15/death_row/dr_scheduled_executions.html). Let's code [this](https://github.com/tommeagher/pythonGIJC15/blob/master/scripts/day_one/scrape1.py) together

##[Day Two](http://www.tommeagher.com/pythonGIJC15/daytwo.html) with [Adriana Homolova](http://ada.homolova.sk/)
###Hour Three:
* We'll recap what we covered the first day and pick up where we left off.
* We already scraped one page. Now we'll modify our first script to grab [the list of all death row inmates](https://s3.amazonaws.com/python-at-ire15/death_row/dr_offenders_on_dr.html) by adding [one column and a loop](https://github.com/tommeagher/pythonGIJC15/blob/master/scripts/day_two/scrape2.py) to our script. There's [extra credit](https://github.com/tommeagher/pythonGIJC15/blob/master/scripts/day_two/extracredit.py) for you to work on at home. With this scraper, make an additional request for each prisoner's profile page to collect other data. 

###Hour Four:
* Next, we'll tackle another scraper. This time, we'll look at the USGS' monthly release of [earthquakes data](http://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php). Again, I've mirrored the CSV on S3 and you can grab it here: http://python-gijc15.s3.eu-central-1.amazonaws.com/all_month.csv
* We'll want to download the CSV, turn it into a dictionary, clean up the date, strip out the country, filter out only the earthquakes above a 6.0. Keep lat/lon and ID. Then we want to write this to a new csv. How would you attack this problem?

###Hour Five: 
* Let's finish our earthquakes scraper. If we have extra time, we can try the extra credit from Texas or we can take a look at the [UK prisons data](http://python-gijc15.s3.eu-central-1.amazonaws.com/contacts/prison-finder/index.html) to grab the capacity of the facilities in the UK.
* Finally, we'll recap and talk about how to take this home with you. There's so much weirdness in coding and quirks to any programming language, we can't possibly do it all in two days. So here are [some resources](https://github.com/ireapps/pycar/tree/master/takehome).