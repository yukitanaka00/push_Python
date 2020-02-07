
import linecache

f = open('input.txt', 'r')
line = f.readline()
line1 = line.split(':')

count = 0
result = []
with open('input.txt') as a:
    for line in a:
        count += 1

target_line = linecache.getline('input.txt', count)


#1行目の処理
if(int(target_line) % int(line1[0])==0):
    result.append(str(line1[1]))

#2行目以降
sa = open('input.txt', 'r')
line2 = sa.readline()
for i in range(count-1):
    s = line2.split(':')

    if(int(target_line) % int(s[0])==0):
        result.append(str(s[1]))
    line2 = sa.readline()

total=''
for a in result:
    a = a.strip("\n")
    total += a
print(total)
if(total == ''):
    print(target_line)
linecache.clearcache() 
f.close()
