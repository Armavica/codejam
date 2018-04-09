e=lambda s,p:0 if s<'B'else(s>'D')*p+e(s[1:],p+(s<'D')*p)
for c in range(int(input())):
 v,s=input().split();n=v=int(v);y=v>=s.count('S')
 if y:
  while e(s,1)>v:x=s.rfind('CS');s=s[:x]+'SC'+s[x+2:];n+=1
 print('Case #%d:'%-~c,['IMPOSSIBLE',n-v][y])
