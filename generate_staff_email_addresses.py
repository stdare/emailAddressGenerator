"""
This script will open a .txt file containing staff names,
remove spaces and replace with '.' then generate the full email address,
sending it to Py Shell for copying to an email.
"""

#read contents of .csv file with unformatted staff names

with open("staff_names.csv", "r") as csvfile:
    NamesRaw = csvfile.readlines()

#Create empty list to recieve edited output
NamesEdited = []
print ("\n--Begin data conversion--")

#CommaFlag checks if name contains ',' and branches to correct IF for the appropriate name format
#Loop through data, replace space with ., remove new lines, add domain and store in a list
for names in NamesRaw:
    CommaFlag = names.find(',')
    if (CommaFlag == -1):                     #no comma found
        namesLower = names.lower()
        namesNoSpace = namesLower.replace(' ','.')
        correctEmail = namesNoSpace.replace('\n', '@sample.isp;')
        NamesEdited.append(correctEmail)
    else:                                     #comma found, do more complex replace process
        namesClean = names.replace('\n', '')
        namesLower = namesClean.lower()
        stringSplit = namesLower.find(',')
        first = namesLower[stringSplit+2:]
        second = namesLower[0:stringSplit]
        namesNoSpace = first+"."+second
        namesNoApost = namesNoSpace.replace('"','')
        correctEmail = namesNoApost+'@sample.isp;'
        NamesEdited.append(correctEmail)
        
#display edited data in IDLE without list indicators for easy copying
print (" ")
for newnames in NamesEdited:
    print (newnames)
print (" ")
print ("-- end of list--")






