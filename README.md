# emailAddressGenerator
Creates full email address from a .csv file with only staff names

This script reads a list of user names and coverts them into firstname.surname@isp; email format.  The results are outputted to a .txt file which python then opens in Notepad for easy copying into a draft email.

The original data may exist in 'firstname surname' OR 'surname, firstname' format.  
The script will recognise the data format and convert each line of the .csv accordingly.
Where the same user name is found, the script skips adding the output to the list, so duplicate email addresses are not created.

The last version of the script will read spaces before or after the username and strip or replace them accordingly.
