lenth=int(input())
width=int(input())
hight=int(input())
percent=float(input())
m3=lenth*width*hight
litter=m3/1000
fill_space=percent/100
needed_lt=litter*(1-0.17)
print(needed_lt)