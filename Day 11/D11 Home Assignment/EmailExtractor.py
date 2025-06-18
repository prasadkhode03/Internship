'''15.	Email Extractor
o	From a text file containing a paragraph, 
extract all words containing '@' and save them as a list of emails to emails.txt'''

with open("text.txt", "r") as text_file:
    readData = text_file.read()
    splitted = readData.split()
    emails = []
    for word in splitted:
        if "@" in word:
            emails.append(word)
    print("List of emails : \n",emails)

with open("emails.txt", "w") as email_file:
    for i in emails:
        email_file.write(f"{i}\n")