import uuid
import re

newline1 = ''
with open('aa', 'r') as f:
    lines = f.readlines()
    for line in lines:
        if line.startswith('values'):
            line = line.replace('1ae3d5c0-d302-4a6d-a39d-c493dbbbf406', 'aa')
            uuida = uuid.uuid4()
            line = re.sub('to_date\(.*?\)', 'sysdate', line, re.S)
            line = re.sub("values \('.*?'", "values ('" + str(uuida) + "'", line, re.S)
            # print(line,end='')
        newline1 += line
    print(newline1)

with open('bb','w') as f:
    f.writelines(newline1)
