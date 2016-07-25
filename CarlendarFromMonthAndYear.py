Leap=0
d = 1; m = input(); y = input()
dom = ([[0,31,28,31,30,31,30,31,31,30,31,30,31],[0,31,29,31,30,31,30,31,31,30,31,30,31]])
dow = (['Sun','Mon','Tue','Wed','Thr','Fri','Sat'])
nbDays = 0
for year in range(1950,y):
	if(((year%4==0) and (year%100!=0)) or (year%400==0)):
		nbDays += 366
	else:
		nbDays += 365
for month in range(1,m):
	if(((y%4==0) and (y%100!=0)) or (y%400==0)):
		nbDays += dom[1][month]
		Leap=1
	else:
		nbDays += dom[0][month]
nbDays += d- 1
res = (nbDays) % 7
Month = ['January','February','March','April','May','June','July','August','September','October','November','Dece    mber']
print'\t', Month[m-1] , y
print 'Su Mo Tu We Th Fr Sa '
for i in range (0,res):
	print '  ',
print ' 1',
if(res%7==6):
	print
for i in range(2,dom[Leap][m]):
	if(res%7==6):
		print
		print'%2d'%(i),
	else:
		print'%2d'%(i),
   res+=1