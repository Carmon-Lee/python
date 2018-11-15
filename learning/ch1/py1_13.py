from operator import itemgetter
rows=[
    {'fname':'brian2','lname':'jones3','uid':'1004'},
    {'fname':'brian','lname':'jones','uid':'1003'},
    {'fname':'brian3','lname':'jones4','uid':'1009'},
    {'fname':'brian1','lname':'jones2','uid':'1002'}
]


rows_by_fname=sorted(rows,key=itemgetter('fname'))

print(rows_by_fname)