"insert into student1 values('12345')"

with open('sql','w') as f:
    for i in range(1000000):
        f.write("insert into student1 values('12345');\n")