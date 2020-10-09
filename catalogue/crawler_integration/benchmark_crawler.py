#!/usr/bin/env python
import csv
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
import math

CPU_URL = 'https://www.cpubenchmark.net/cpu_list.php'
GPU_URL = 'https://www.videocardbenchmark.net/gpu_list.php'

def scrape(website:str='cpu', filename:str='newbenchmark.csv', selection:str='web') -> str:
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

    table = soup.find('table', attrs={'id': 'cputable', 'class': 'cpulist'})
    headers = [header.text for header in table.find('thead').find_all('th')]
    headers.insert(0,"Link")
    rows = []
    count = 0
    for row in table.find_all('tr'):
        tableRow = row.find_all("td")
        try:
            rowLink = tableRow[0].find("a")["href"].replace("cpu_lookup","cpu")
            rowCPU = tableRow[0].text
            rowCPUMark = tableRow[1].text
            rowRank = tableRow[2].text
            rowCPUValue = tableRow[3].text
            rowPrice = tableRow[4].text
            rows.append([rowLink, rowCPU, rowCPUMark, rowRank, rowCPUValue, rowPrice])
        except IndexError:
            pass

    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(row for row in rows if row)
        return os.path.join(os.getcwd(), f.name)

from datetime import datetime

def getPriceRec(itemName, age:int, rating:int=5, mining:str='no'):
    depreciation_per_year = 0.05
    depreciation_if_mining = 5
    depreciaton_per_rating = 5

    csv_file = csv.reader(open('newbenchmark.csv', "r"), delimiter=',')
    for row in csv_file:
        if itemName in row[1]:
            price = int(float(row[5].replace("$","").replace("*","")))

    ageInYears = int(datetime.today().year) - int(age[-4:])
    deprecationValue = ageInYears * depreciation_per_year
    recommendedPrice = int(float(price * deprecationValue))
    print("Recommended Price: $" + str(recommendedPrice))
        
CPU_DESC_URL = 'https://www.cpubenchmark.net/'
GPU_DESC_URL = 'https://www.gpubenchmark.net/'

def scrapeDescInfo(website:str='cpu', filename:str='oneDesc.csv', selection:str='Intel Core i5-4590 @ 3.30GHz') -> str:
    website_types = ['cpu', 'gpu']
    if website in website_types:
        if website == 'cpu':
            website = CPU_DESC_URL
        elif website == 'gpu':
            website = GPU_DESC_URL
    csv_file = csv.reader(open('newbenchmark.csv', "r"), delimiter=',')
    for row in csv_file:
        if selection in row[1]:
            linkRequired = row[0]
    websiteURL = website + linkRequired
    with urlopen(websiteURL) as website:
        soup = BeautifulSoup(website, 'html.parser')
    descInfo = soup.find('div', attrs={'class': 'left-desc-cpu'})
    deepInfo = descInfo.find_all('p')
    print("Item Name: " + selection)
    for info in deepInfo:
        print(info.text)
    ageInfo = soup.find('div', attrs={'class': 'desc-foot'})
    deepAge = ageInfo.find_all('p')
    ageInfo = "Year of Release: " + deepAge[1].text[-7:]
    print(ageInfo)
    getPriceRec(selection, deepAge[1].text[-7:])


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