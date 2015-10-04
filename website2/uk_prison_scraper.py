from time import sleep
from bs4 import BeautifulSoup
import os

import requests
from lxml import html

#terrible, untested scraper to mirror the UK prison finder. Probably doesn't work

def relocate_href(link):
    if link.startswith('https://www.justice.gov.uk'):
        url = link[len('https://www.justice.gov.uk'):]
        url = ''+ url
        return url
    else:
        return link


base_url = "https://www.justice.gov.uk/contacts/prison-finder/"

index_base = "prisonfinder-a-z"

home_request = requests.get(base_url)
soup = BeautifulSoup(home_request.text)
for a in soup.findAll(href=True):
    a['href'] = relocate_href(a['href']).replace('?', '__').replace('#', '__')
    if a['href'].endswith('.css'):
        a['href']=a['href']
    else:
        a['href'] = a['href']+"/index.html"
for a in soup.findAll(src=True):
    a['src'] = relocate_href(a['src'])

with open('index.html', 'wb') as i:
    i.write(str(soup))

index_request = base_url+index_base

first_request = requests.get(index_request)

soup = BeautifulSoup(first_request.text)
for a in soup.findAll(href=True):
    a['href'] = relocate_href(a['href']).replace('?', '__').replace('#', '__')
    if a['href'].endswith('.css'):
        a['href']=a['href']
    else:
        a['href'] = a['href']+"/index.html"
for a in soup.findAll(src=True):
    a['src'] = relocate_href(a['src'])

filename='contacts/prison-finder/prisonfinder-a-z/'
dir = filename
if not os.path.exists(dir):
    os.makedirs(dir)

with open(dir + 'index.html', 'wb') as i:
    i.write(str(soup))

page_html = first_request.text
tree = html.fromstring(page_html)

tablerows = tree.xpath('//*[@id="content"]/article/div[2]/div/ul/li')

alpha_urls = []

for row in tablerows:
    if len(row.xpath('a'))>0:
        new_url = row.xpath('a')[0].values()[0]
        alpha_urls.append(new_url)

detail_urls = []

for url in alpha_urls:
    print url
    make_request = requests.get(url)
    page_html = make_request.text
    soup = BeautifulSoup(page_html)
    for a in soup.findAll(href=True):
        a['href'] = relocate_href(a['href']).replace('?', '__').replace('#', '__')
        if a['href'].endswith('.css'):
            a['href']=a['href']
        else:
            a['href'] = a['href']+"/index.html"
    for a in soup.findAll(src=True):
        a['src'] = relocate_href(a['src'])
    filename = url.split('https://www.justice.gov.uk/')[1].replace('?', '__').replace('#', '__')
    dir = filename

    if not os.path.exists(dir):
        os.makedirs(dir)
    with open(filename+'/index.html', 'wb') as f:
        f.write(str(soup))

    new_tree = html.fromstring(page_html)
    starter = new_tree.xpath('//*[@id="content"]/article/div[2]/p[1]')
    next_ul = starter[0].getnext()
    while next_ul.tag == 'ul':
        added_url = next_ul.xpath('a')[0].values()[0]
        print added_url
        detail_urls.append(added_url)
        next_ul = next_ul.getnext()

    sleep(2)


for detail in detail_urls:
    print detail
    r = requests.head(detail)
    if r.status_code==302:
        q = requests.head(detail, allow_redirects=True)
        filename = r.url.split('https://www.justice.gov.uk/')[1]
        #write this 
        new_filename = '/'.join(filename.split('/')[:-1])
        os.chmod(new_filename, 0777)
        if q.status_code==200:
            next_url = q.url
            z = requests.get(next_url)
        new_text = '<head><meta http-equiv="refresh" content="0;url={0}" /></head><body></body>'.format(q.url.split('https://www.justice.gov.uk')[1]+"/index.html")
        dir = filename
        if not os.path.exists(dir):
            os.makedirs(dir)
        with open(filename+"/index.html", 'wb') as f:
            f.write(new_text)
            print filename+"/index.html"
        q_filename = q.url.split('https://www.justice.gov.uk/')[1]
        new_html = z.text
        soup = BeautifulSoup(new_html)
        for a in soup.findAll(href=True):
            a['href'] = relocate_href(a['href'])
            if a['href'].endswith('.css'):
                a['href']=a['href']
            else:
                a['href'] = a['href']+"/index.html"
        for a in soup.findAll(src=True):
            a['src'] = relocate_href(a['src'])

        dir = q_filename
        if not os.path.exists(dir+"/"):
            os.makedirs(dir)
        with open(q_filename+"/index.html", 'wb') as g:
           html_string = str(soup)
           g.write(html_string)
           print q_filename+"/index.html"

    elif r.status_code==200:
        r = requests.get(detail)
        new_html = r.text
        q_filename = r.url.split('https://www.justice.gov.uk/')[1]
        soup = BeautifulSoup(new_html)
        for a in soup.findAll(href=True):
            if a:
                a['href'] = relocate_href(a['href'])
                if a['href'].endswith('.css'):
                    a['href']=a['href']
                else:
                    a['href'] = a['href']+"/index.html"
        for a in soup.findAll(src=True):
            a['src'] = relocate_href(a['src'])
        dir = q_filename
        if not os.path.exists(dir+"/"):
            os.makedirs(dir)
        with open(q_filename+"/index.html", 'wb') as f:
            html_string = str(soup)
            f.write(html_string)
            print q_filename+"/index.html"

    sleep(2)


