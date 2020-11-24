board = ['X','O',' ','X',' ','O',' ','X','O']
str = "".join(board)
print(str)
dup = board.copy() 
for count, item in enumerate(dup):
    if item=='X':
        dup[count]='9'
    if item=='O':
        dup[count]='5'
    if item==' ':
        dup[count]='0'
 
dup.insert(0,'0')
dup.insert(4,'0')
dup.insert(5,'0')
dup.insert(9,'0')
dup.insert(10,'0')
dup.insert(14,'0')
dup.insert(15,'0')
dup.insert(19,'0')
dup.insert(20,'0')
dup.insert(24,'0')
dup.insert(5,':')
dup.insert(11,':')
dup.insert(17,':')
dup.insert(0,'0')
dup.insert(0,'0')
dup.insert(0,'0')
dup.insert(0,'0')
dup.insert(0,'0')
dup.insert(5,':')

print(''.join(dup))