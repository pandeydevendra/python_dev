import unicodecsv

enrollments = []
f = open('enrollments.csv', 'rb')
reader = unicodecsv.DictReader(f)

for row in reader:
    enrollments.append(row)

f.close()

enrollments[0]

# OR

import unicodecsv

with open('enrollments.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    enrollments = list(reader)

enrollments[0]
