#!/usr/bin/env python
import csv
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen

CPU_URL = 'https://www.cpubenchmark.net/cpu_list.php'
GPU_URL = 'https://www.videocardbenchmark.net/gpu_list.php'

def scrape(website:str='cpu', filename:str='benchmark.csv', selection:str='web') -> str:
    # a function that scrapes a website, saves as CSV format, and returns the path to file
    website_types = ['cpu', 'gpu']
    if selection == 'web':
        if website in website_types:
            if website == 'cpu':
                    website = CPU_URL
            elif website == 'gpu':
                    website = GPU_URL
            with urlopen(website) as website:
                soup = BeautifulSoup(website, 'html.parser')
    elif selection == 'file':
        file = open(website, 'r')
        soup = BeautifulSoup(file, 'html.parser')
        file.close()

    table = soup.find('table', attrs={'id' : 'cputable', 'class': 'cpulist'})
    headers = [header.text for header in table.find('thead').find_all('th')]
    rows = []

    for row in table.find_all('tr'):
        rows.append([val.text.replace(',', '').replace('NA', '') for val in row.find_all('td')])

    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(row for row in rows if row)
        return os.path.join(os.getcwd(), f.name)

from django.db import *
from django.db import transaction

def pushDB(filename:str='benchmark.csv'):
    filetoPush = filename
    with open(filetoPush, newline='') as csv_contents:
        fileReader = csv.reader(csv_contents, delimiter = ',')
        with transaction.atomic():
            for row in fileReader:
                if "Mobile" not in row[0]:
                    if "*" not in row[4]:
                        newEntry = cpu(cpu_Name = row[0], cpu_Mark = row[1], cpu_Rank = row[2], cpu_Value = row[3], cpu_Price = row[4][2:])
                    else:
                        newEntry = cpu(cpu_Name = row[0], cpu_Mark = row[1], cpu_Rank = row[2], cpu_Value = row[3], cpu_Price = row[4][2:-1])
                newEntry.save()
        
'''        
    cpu_Name = models.CharField(max_length=255)
    cpu_Mark = models.IntegerField()
    cpu_Rank = models.IntegerField()
    cpu_Value = models.IntegerField()
    cpu_Price = models.IntegerField()

        '''
pushDB()
