for c in range(int(input())):
 input();*l,=map(int,input().split());l[::2],l[1::2]=map(sorted,(l[::2],l[1::2]))
 print('Case #%d:'%-~c,['OK',*(i for i in range(len(l)-1)if l[i]>l[i+1])][l!=sorted(l)])
