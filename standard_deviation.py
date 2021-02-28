numbers= [13,8,4,9,7,12,10] #Enter your list of number here
sq_diff =[]
summ, count= 0, 0
for m in numbers:
    summ = summ + m
    count = count + 1
print('The mean for the given data is ',summ/count)
for m in numbers:
    square = (m - summ/count)**2
    sq_diff.append(square)
print("the is ", sq_diff)
ssd = 0
for i in sq_diff:
    ssd = ssd + i
print (ssd)
variance = ssd/count
print(variance)
sd = variance**(1/2)
print(sd)
