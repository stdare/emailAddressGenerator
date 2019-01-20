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

#CommaFlag checks if name contains ',' and branches to correct IF for the
#  appropriate name format
#Loop through data, replace space with ., remove new lines, add domain and store
for names in NamesRaw:
    if (names.find(',') == -1):                     #no comma found
        namesCleaned = names.lower()
        namesCleaned = namesCleaned.replace(' ','.')
        namesCleaned = namesCleaned.replace('\n', '@sample.isp')
        NamesEdited.append(namesCleaned)
    else:                          #comma found, do more complex replace process
        namesClean = names.replace('\n', '')
#        namesClean = namesClean.strip()        #this line not working (don't know why)
        namesClean = namesClean.lower()
        stringSplit = namesClean.find(',')
        firstname = namesClean[stringSplit+2:]
        surname = namesClean[0:stringSplit]
        namesClean = firstname+"."+surname
        namesClean = namesClean.replace('"','')
        namesClean = namesClean+'@sample.isp'
        NamesEdited.append(namesClean)

#display edited data in IDLE without list indicators for easy copying
print (" ")
for FormattedEmails in NamesEdited:
    print (FormattedEmails+';')
print (" ")
print ("-- end of list--")
