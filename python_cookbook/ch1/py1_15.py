from operator import itemgetter
from itertools import groupby

rows=[
    {'fname':'brian2','lname':'jones3','uid':'1004'},
    {'fname':'brian','lname':'jones','uid':'1003'},
    {'fname':'brian3','lname':'jones4','uid':'1009'},
    {'fname':'brian1','lname':'jones2','uid':'1002'}
]

rows.sort(key=itemgetter('fname'))
print(rows)

for id,name in groupby(rows,key=itemgetter('uid')):
    print(id)
    for i in name:
        print(' ',i)

from collections import defaultdict
rows_by_date=defaultdict(list)
for row in rows:
    rows_by_date[row['uid']].append(row)
print(rows)