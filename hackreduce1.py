import csv
import sys
import operator

inclusion = ['2011']

with open('noaa_weather.csv','r') as in_file, open('sorted1.csv','w') as out_file:
    mycsv = csv.reader(in_file)
    sortedlist = sorted(mycsv, key=operator.itemgetter(5), reverse=True)


