# PDF_Rename
Bulk Rename PDF file names with a delimiter then Rename using a CSV column matched name

Problem to solve
A user needed a program that can automate the process of renaming multiple PDF files that had the following format "############_textornumbersoranyothercharacter.pdf". The new names are popullated in a CSV file named "newnames" with two columns one for Account and one for Name. 
First you need to have 3 folders named as follow:
Initial_FD
Transit_FD
Result

You will also need a CSV file named "newnames". This file contain the 2 column headers one is "Account" and the other is "Name". Account should have the values ############.pdf and the name should have the desired name ending with.pdf.

The program also prompt for a date that will be inserted between the account number and the new name to have the following final format:

############_date namename.pdf
