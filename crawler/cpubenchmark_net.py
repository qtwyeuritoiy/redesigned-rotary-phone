#!/usr/bin/env python
import csv
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen

TARGET_URL = 'https://www.cpubenchmark.net/cpu_list.php'
FILENAME = 'cpubenchmark_cpu_list.csv'

def scrape_cpu() -> str:
    # a function that scrapes a website, saves as CSV format, and returns the path to file
    with urlopen(TARGET_URL) as website:
        soup = BeautifulSoup(website, 'html.parser')
        table = soup.find('table', attrs={'id' : 'cputable', 'class': 'cpulist'})
        headers = [header.text for header in table.find('thead').find_all('th')]
        rows = []

        for row in table.find_all('tr'):
            rows.append([val.text.replace(',', '').replace('NA', '') for val in row.find_all('td')])

        with open(FILENAME, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(row for row in rows if row)

            return os.path.join(os.getcwd(), f.name)
