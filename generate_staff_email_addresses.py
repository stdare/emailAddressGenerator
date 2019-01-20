"""
This script will open a .txt file containing staff names,
remove spaces and replace with '.' then generate the full email address,
sending it to a .txt file which then opens in Notepad.
"""

#read contents of .csv file with just staff names without email addresses.

with open("staff_names.csv", "r") as csvfile:
    NamesRaw = csvfile.readlines()

#Create empty list to receive edited output
NamesEdited = []

#Check if name contains ',' and branches to correct IF
#   for the appropriate name format.
#Loop through data, replace space with ., remove new lines, add domain and store.
for names in NamesRaw:
    if (names.find(',') == -1):                     #no comma found
        namesCleaned = names.lower()
        namesCleaned = namesCleaned.replace(' ','.')
        namesCleaned = namesCleaned.replace('\n', '@myisp.com.au; ')
        NamesEdited.append(namesCleaned)
    else:                          #comma found, do more complex replace process
        namesClean = names.replace('\n', '')
#        namesClean = namesClean.strip()    #this line not working(don't know why)
        namesClean = namesClean.lower()
        stringSplit = namesClean.find(',')
        firstname = namesClean[stringSplit+2:]
        surname = namesClean[0:stringSplit]
        namesClean = firstname+"."+surname
        namesClean = namesClean.replace('"','')
        namesClean = namesClean+'@myisp.com.au; '
        NamesEdited.append(namesClean)

#write the results to a new .txt file
with open("generated_emails.txt", "w") as f:
        for row in NamesEdited:
            print(row, file=f)

#open the text file in Notepad
import webbrowser
webbrowser.open("generated_emails.txt")
