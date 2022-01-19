import os, csv
import sys
from datetime import date
# open and store the csv file
IDs = {}
with open('newnames.csv','r') as csvfile:
    csv_data = csv.reader(csvfile)
    next(csv_data)
    # build dictionary with associated IDs
    for row in csv_data:
        IDs[row[0]] = row[1]

# Rename file from initial folder to temporary folder using the delimiter '_'. 
# This assumes that the initial file name has the following format: ############_textornumbersoranyothercharacter.pdf
inifold = 'Initial_FD/'
tempfold = 'Transit_FD/'

for fl_name in os.listdir(inifold):
    os.rename(os.path.join(inifold, fl_name), os.path.join(tempfold, (os.path.basename(fl_name).split('_')[0])))

# Rename files from temporary folder to the result folder using by associating the value of the title "the number in this case" 
# with its corresponding text in the csv file. It also prompt the user to enter a date
# It will ignore files in SrPath that does not have a corrsponding name in the csv file. 
# These files can be added to the csv file since there is no match
SrPath = 'Transit_FD/'
RsPath = 'Result/'
date = input('Enter date(yyyy-mm-dd): ')

for oldname in os.listdir(SrPath):
    if oldname in IDs:
        try:
            os.rename(os.path.join(SrPath, oldname), os.path.join(RsPath, (os.path.splitext(oldname)[0])+"_"+date+IDs[oldname]))
        except:
            print ('File ' + oldname + ' could not be renamed to ' + IDs[oldname] + '!')