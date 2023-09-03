d = {}
for people in range (0,5):
    who = input('name= ')
    point = input('分數=  ')
    d[who] = point
    print(end='\n')
print(d)
print(end='\n')

for searchwho in range (0,5):
    search = input('查誰 ')
    print(d.get(search,'沒有這個人:('))
