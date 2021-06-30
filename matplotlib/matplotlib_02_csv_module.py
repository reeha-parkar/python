import csv
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    language_counter = Counter()
    
    ''' row = next(csv_reader)
    # print(row)
    print(row['LanguagesWorkedWith'].split(';')) '''

    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

plt.title("Most Popular Languages")
# plt.ylabel("Programming Languages")
plt.xlabel("No. of people who use")

plt.tight_layout()

plt.show()
