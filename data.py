import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import sys

for page in range(0,1):
    response= requests.get("https://cfseu18.sched.com/directory/descriptions/1".format(page))
    soup= BeautifulSoup(response.content, "lxml")
    title = soup.select("div.sched-container-inner")
    company = soup.select("div.sched-container-inner > div.sched-page-attendees-data")
    position = soup.select("div.sched-container-inner > div.sched-page-attendees-data")
    for person in title:
        name = person.select_one("h4 > a").text.strip()
        lower = person.select_one("div#sched-page-attendees-data").text.strip().split('<br>')
        print(name,lower)
        with open('test.csv','a') as csv_file:
            write = csv.writer(csv_file)
            write.writerow([name, lower])

