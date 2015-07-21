# Python at GIJC15
An introduction to using Python in the newsroom at [GIJC 2015](http://gijc2015.org/) in Lillehammer, Norway.

Follow along [with the slides](http://www.tommeagher.com/pythonIRE15/#/).

We'll learn the basics of coding in the newsroom by scraping the Texas Department of Criminal Justice's website for its [list of death row inmates](http://tdcj.state.tx.us/death_row/dr_offenders_on_dr.html) and [its list of scheduled executions](http://tdcj.state.tx.us/death_row/dr_scheduled_executions.html).

Because we don't want to hammer the TDCJ website, I've mirrored the pages on s3, so first we'll be scraping the scheduled executions: https://s3.amazonaws.com/python-at-ire15/death_row/dr_scheduled_executions.html
Then we'll do the list of all death row inmates, adding a column to our scraper: https://s3.amazonaws.com/python-at-ire15/death_row/dr_offenders_on_dr.html

A rough outline of the two, 1-hour sessions:

Hour One:
* Why code at all and why Python?
* Strings, ints, variables, and lists. Everything you need to know about programming you probably learned in Excel
* How the hell do you scrape a website? A quick exercise in breaking down a problem into components and writing functions.

Hour Two:
* Let's code [this](https://github.com/tommeagher/pythonIRE15/blob/master/scripts/scrape1.py) together
* Now you try it on the list of [other death row inmates](https://github.com/tommeagher/pythonIRE15/blob/master/scripts/scrape2.py) (add one column and a loop)!
* There's so much weirdness in coding and quirks to any programming language, we can't possibly do it all in two hours. So here are [some resources](https://github.com/ireapps/pycar/tree/master/takehome).