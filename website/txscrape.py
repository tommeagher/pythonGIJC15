from time import sleep
from lxml import html
from StringIO import StringIO
import requests
from PIL import Image

base_url = "http://tdcj.state.tx.us/death_row/"

page1 = "dr_offenders_on_dr.html"

big_get = requests.get(base_url+page1)

pagehtml = big_get.text

tree = html.fromstring(pagehtml)

tablerows = tree.xpath('//*[@id="body"]/table/tbody/tr')


for row in tablerows:
    if row[1].text=='Link':
        pass
    else:
        new_url = row[1].getchildren()[0].values()[0]
        new_request = requests.get(base_url+new_url)
        new_output = 'death_row/'+new_url
        if new_url.endswith('.html'):
#            with open(new_output, 'wb') as f:
#                f.write(new_request.text)
    	    pass

        elif new_url.endswith('.jpg'):
            i = Image.open(StringIO(new_request.content)).save(new_output)
            print new_url + " saved."
            sleep(1)






