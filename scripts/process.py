import csv
#import os
import urllib
#import dataconverters.xls
sources = [ "http://cdiac.ornl.gov/ftp/trends/temp/hansen/gl_land.txt?force_download=true",
            "http://cdiac.ornl.gov/ftp/trends/temp/hansen/gl_land_ocean.txt?force_download=true",
            "http://cdiac.ornl.gov/ftp/trends/temp/hansen/nhsh.txt?force_download=true",
            "http://cdiac.ornl.gov/ftp/trends/temp/hansen/norlowsou.txt?force_download=true" ]
cache = 'cache/'
out_annual = 'data/global-temp-annual.csv'
out_5yr = 'data/global-temp-5yr.csv'

def string_between(string, before, after):
	temp = string.split(before)[1]
	temp = temp.split(after)[0]
	return temp

def execute():
    names = []
    for s in sources:
        name = string_between(s,'hansen/','?force_download')
        urllib.urlretrieve(s, cache+name)
        names.append(name)

    header = ['Year', 'Land', 'Land and Ocean','N Hem','S Hem','Band 1','Band 2','Band 3']

    records_annual = []
    records_5yr = []
    temp = 0
    for line in open(cache+'gl_land.txt'):
        if '--------' in line:
            temp+=1
            continue
        if(temp < 2):
            continue
        data = line.strip().split(' ')
        data = filter(None,data)
        year = data[0]
        half = (len(data) - 1)/2
        records_annual.append([year] + data[1:half+1])
        records_5yr.append([year] + data[half+1:])

    temp = 0
    for line in open(cache+'gl_land_ocean.txt'):
        if '--------' in line:
            temp+=1
            continue
        if(temp < 2):
            continue
        data = line.strip().split(' ')
        data = filter(None,data)
        year = data[0]
        half = (len(data) - 1)/2
        i = int(year) - 1880
        records_annual[i]+=data[1:half+1]
        records_5yr[i]+=data[half+1:]

    temp = 0
    for line in open(cache+'nhsh.txt'):
        if '--------' in line:
            temp+=1
            continue
        if(temp < 2):
            continue
        data = line.strip().split(' ')
        data = filter(None,data)
        year = data[0]
        half = (len(data) - 1)/2
        i = int(year) - 1880
        records_annual[i]+=data[1:half+1]
        records_5yr[i]+=data[half+1:]

    temp = 0
    for line in open(cache+'norlowsou.txt'):
        if '--------' in line:
            temp+=1
            continue
        if(temp < 2):
            continue
        data = line.strip().split(' ')
        data = filter(None,data)
        year = data[0]
        half = (len(data) - 1)/2
        i = int(year) - 1880
        records_annual[i]+=data[1:half+1]
        records_5yr[i]+=data[half+1:]

    for i in range(len(records_annual)):
        r = records_annual[i]
        if len(r) < 8:
            r+=['']*(8-len(r))
        records_annual[i] = [x.replace('-99.99','') for x in r[:-3]]
        records_annual[i]+= [x.replace('-9.99','') for x in r[-3:]]

    for i in range(len(records_5yr)):
        r = records_5yr[i]
        if len(r) < 8:
            r+=['']*(8-len(r))
        records_5yr[i] = [x.replace('-99.99','') for x in r[:-3]]
        records_5yr[i]+= [x.replace('-9.99','') for x in r[-3:]]

    writer = csv.writer(open(out_annual, 'w'), lineterminator='\n')
    writer.writerow(header)
    writer.writerows(records_annual)
    writer = csv.writer(open(out_5yr, 'w'), lineterminator='\n')
    writer.writerow(header)
    writer.writerows(records_5yr)

execute()
