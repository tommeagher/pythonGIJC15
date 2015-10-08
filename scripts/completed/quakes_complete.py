import requests
import unicodecsv
from io import StringIO

#what country has the most serious earthquakes lately?
url = "http://python-gijc15.s3.eu-central-1.amazonaws.com/all_month.csv"

r = requests.get(url)

text = StringIO(r.text)

reader = unicodecsv.DictReader(text, dialect='excel')

new_collection = []
for row in reader:
    if row['type'] == "earthquake":
        if float(row['mag'])>=6.0:
            new_collection.append(row)
        else:
            pass
    else:
        pass

for item in new_collection:
    item[u'nearest']=item['place'].split(',')[-1].strip()

#write the results to a new csv
filename = "serious_quakes.csv"

print new_collection[0].keys()

fieldnames = [u'time', u'latitude', u'longitude', u'mag', u'type', u'id', u'place', u'nearest']

with open(filename, "wb") as f:
    writer = unicodecsv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()

    for item in new_collection:
        writer.writerow(item)
