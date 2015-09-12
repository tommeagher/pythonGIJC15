# Scraping in the Newsroom with Python
##At [GIJC 2015](http://gijc2015.org/) in Lillehammer, Norway.

Before class, be sure that [you have installed Python 2.7](PRE-CLASS.md) and all the necessary tools. 

A rough outline of the five, 1-hour sessions. Follow along [with the slides](http://www.tommeagher.com/pythonGIJC15/#/).

##[Day One](http://www.tommeagher.com/pythonGIJC15) with [Tommy Kaas](http://www.kaasogmulvad.dk/)
###Hour One:
* Why code at all and why Python?
* Strings, ints, variables, and lists. [Everything](https://github.com/tommeagher/pythonGIJC15/blob/master/scripts/day_one/the_basics.py) you need to know about programming you probably learned in Excel
* How the hell do you scrape a website? A quick exercise in breaking down a problem into its components and writing functions. http://www.tommeagher.com/pythonGIJC15/#/15

###Hour Two:
* We'll be scraping the Texas Department of Criminal Justice's website for its [list of death row inmates](http://tdcj.state.tx.us/death_row/dr_offenders_on_dr.html) and [its list of scheduled executions](http://tdcj.state.tx.us/death_row/dr_scheduled_executions.html). Because we don't want to hammer the TDCJ website, I've mirrored the pages on s3, so first we'll be scraping [the scheduled executions](https://s3.amazonaws.com/python-at-ire15/death_row/dr_scheduled_executions.html). Then we'll reuse the code to scrape [the list of all death row inmates](https://s3.amazonaws.com/python-at-ire15/death_row/dr_offenders_on_dr.html), adding a column to our scraper. Let's code [this](https://github.com/tommeagher/pythonGIJC15/blob/master/scripts/day_one/scrape1.py) together

##[Day Two](http://www.tommeagher.com/pythonGIJC15/daytwo.html) with [Adriana Homolova](http://ada.homolova.sk/)
###Hour Three:
* We'll recap what we covered the first day and pick up where we left off.
* We already scraped one page, now we'll use the same script to try it on the list of [other death row inmates](https://github.com/tommeagher/pythonGIJC15/blob/master/scripts/day_two/scrape2.py) (add one column and a loop)!

###Hour Four:
* Let's tackle the Texas extra credit, making additional requests for each profile page. Or should this be part one of a new scraper? Probably.

###Hour Five: 
* Next, we'll tackle another scraper, this time one with incrementing parameters in the URL. Or maybe talk about APIs and using JSON in Python scripts.
* There's so much weirdness in coding and quirks to any programming language, we can't possibly do it all in two days. So here are [some resources](https://github.com/ireapps/pycar/tree/master/takehome).