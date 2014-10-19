import csv

word = []
pos = []
sub_type = []
franchise = []
sub_franchise = []

with open('nerdemipsum-db.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('nerdemipsum-db_new.csv', mode='w') as outfile:
    	for row in reader:
    		outfile.write(row[0] + '\n')
    #     writer = csv.writer(outfile)
    #     mydict = {rows[0]:rows[1] for rows in reader}
    #     print mydict