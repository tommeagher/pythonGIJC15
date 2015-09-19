d# Scraping in the Newsroom with Python
##At [GIJC 2015](http://gijc2015.org/) in Lillehammer, Norway.

Before class, be sure [you've installed Python 2.7](PRE-CLASS.md) and all the necessary tools. 

Here's a rough outline of the five, 1-hour sessions. Follow along [with the slides](http://www.tommeagher.com/pythonGIJC15/#/).

##[Day One](http://www.tommeagher.com/pythonGIJC15) with [Tommy Kaas](http://www.kaasogmulvad.dk/)
###Hour One:
* Why code at all, and why Python?
* Strings, ints, variables, and lists. [Everything](https://github.com/tommeagher/pythonGIJC15/blob/master/scripts/day_one/the_basics.py) you need to know about programming you probably already learned in Excel
* How the hell do you scrape a website? A quick exercise in breaking down a problem into its components and writing functions. http://www.tommeagher.com/pythonGIJC15/#/15

###Hour Two:
* We'll be scraping the Texas Department of Criminal Justice's website for its [list of death row inmates](http://tdcj.state.tx.us/death_row/dr_offenders_on_dr.html) and [its list of scheduled executions](http://tdcj.state.tx.us/death_row/dr_scheduled_executions.html). Because we don't want to hammer the TDCJ website, I've mirrored the pages on s3. We'll be scraping [the scheduled executions](https://s3.amazonaws.com/python-at-ire15/death_row/dr_scheduled_executions.html). Let's code [this](https://github.com/tommeagher/pythonGIJC15/blob/master/scripts/day_one/scrape1.py) together

##[Day Two](http://www.tommeagher.com/pythonGIJC15/daytwo.html) with [Adriana Homolova](http://ada.homolova.sk/)
###Hour Three:
* We'll recap what we covered the first day and pick up where we left off.
* We already scraped one page, now we'll use the same script to try it on [the list of all death row inmates](https://s3.amazonaws.com/python-at-ire15/death_row/dr_offenders_on_dr.html) by adding [one column and a loop](https://github.com/tommeagher/pythonGIJC15/blob/master/scripts/day_two/scrape2.py) to our script. There's extra credit for you to work on at home. With this scraper, make an additional request for each prisoner's profile page. 

###Hour Four:
* Next, we'll tackle another scraper. This time, we want to gather information about the size and capacity of the United Kingdom's prison systems. We also want to see how many prisons have made adjustments over time to allow them to hold more prisoners than they were originally designed for. We'll be scraping a clone of the UK's Justice ministry's [Prison Finder website](https://www.justice.gov.uk/contacts/prison-finder/). We'll want to compare each facility's [certified normal accomodation to its operational capacity](http://www.bbc.com/news/uk-19395427).

###Hour Five: 
* We'll wrap up our UK prison scraper.
* There's so much weirdness in coding and quirks to any programming language, we can't possibly do it all in two days. So here are [some resources](https://github.com/ireapps/pycar/tree/master/takehome).