l=[[*map(int,i.split())]for i in[*open(0)][1:]]
m=min
r,g,b=0,0,0
for i in l:r,g,b=i[0]+m(g,b),i[1]+m(b,r),i[2]+m(r,g)
print(m(r,g,b))