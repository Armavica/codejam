for c in range(int(input())):
 a=eval(input());b=(6-2*a*a)**.5;print('Case #%d:'%-~c)
 for v in[[3+a+b,2*a-b,3-a-b],[b-2*a,2*a+2*b,2*a-b],[3-a-b,b-2*a,3+a+b]]:print(*[x/12 for x in v])
