import csv
import re

counter = 0
languages = {} 

with open("language.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        language = row["language"].strip().upper()
        if re.search("^(C|SCRATCH)$",language):
            counter += 1

# def get_value(language):
#     return languages[language]  
# instead used lambda function

# for l in sorted(languages, key=lambda language: languages[language], reverse=True):
#     print(l, languages[l])

print(f"Number of people not using python are {counter}")
