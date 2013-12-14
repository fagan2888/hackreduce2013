import csv
count = 0
day = {'1':'01',
        '2':'02',
        '3':'03',
        '4':'04',
        '5':'05',
        '6':'06',
        '7':'07',
        '8':'08',
        '9':'09',
        '10':'10',
        '11':'11',
        '12':'12'}
with open('MBCR_Trip_Records_2011.csv','r') as in_file, open('real2011data.csv', 'r') as in_file2, open('datescorrect.csv','w') as out_file:
    seen = set()
    reader = csv.reader(in_file, delimiter=',')
    writer = csv.writer(out_file)
    for row in reader:
        #print (row[13])
        s = row[13].split('/')
        c = ""
        t = ""
        for char in s:
            if (len(char)>1):
                c += char
            else:
                c += day[char]
        t = c[-4:] + c[0:2] + c[2:4]
        writer.writerow([t])
    print (count)
