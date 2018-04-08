def e(s):
 d=x=1
 for c in s:
  if c<'D':x*=2
  else:d+=x
 return~-d
for c in range(int(input())):
 v,s=input().split();n=v=int(v);y=v>=s.count('S')
 if y:
  while e(s)>v:x=s.rfind('CS');s=s[:x]+'SC'+s[x+2:];n+=1
 print('Case #%d:'%-~c,['IMPOSSIBLE',n-v][y])
