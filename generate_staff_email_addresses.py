"""
This script will open a .txt file containing staff names,
remove spaces and replace with '.' then generate the full email address,
sending it to Py Shell for copying to an email.
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
    if (names.find(',') == -1):          #no comma found, do simple clean process
        namesCleaned = names.lower()
        namesCleaned = namesCleaned.strip()
        namesCleaned = namesCleaned.replace(' ','.')
        namesCleaned = namesCleaned+'@isp.com.au; '
        if (namesCleaned not in NamesEdited):       #check for duplicate entries
            NamesEdited.append(namesCleaned)
    else:                            #comma found, do more complex clean process
        namesClean = names.replace('\n', '')
        namesClean = namesClean.lower()
        stringSplit = namesClean.find(',')
        firstname = namesClean[stringSplit+2:]
        surname = namesClean[0:stringSplit]
        namesClean = firstname+"."+surname
        namesClean = namesClean.replace('"','')
        namesClean = namesClean.replace(' ','')
        namesClean = namesClean+'@isp.com.au; '
        if (namesClean not in NamesEdited):         #check for duplicate entries
            NamesEdited.append(namesClean)

#write the results to a new .txt file
with open("generated_emails.txt", "w") as f:
        for row in NamesEdited:
            print(row, file=f)

#open the .txt file in Notepad to copy output
import webbrowser
webbrowser.open("generated_emails.txt")
