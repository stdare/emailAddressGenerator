# emailAddressGenerator
Creates full email address from a .csv file with only staff names

This script pulls a list of user names and coverts them into firstname.surname@isp; email format.  The results are outputted to a .txt file which python then opens in notepad for easy copying into a draft email.

The original data may exist in 'firstname surname' OR 'surname, firstname' format.  
The script will recognise the data format and convert each line of the .csv accordingly.

There is no provision (yet) to manage errors/complexities in name format (such as missing space in the comma format or surnames with a space).  I may do this in subsequent versions - for a challenge more than anything.  split() doesn't seem to work as expected for some reason.
