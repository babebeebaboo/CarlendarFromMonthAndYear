LeapYear=0
d = 1; m = input(); y = input()
DayOfMonth = ( [ [0,31,28,31,30,31,30,31,31,30,31,30,31] , [0,31,29,31,30,31,30,31,31,30,31,30,31] ] )
DayOfWeek = ( ['Sun','Mon','Tue','Wed','Thr','Fri','Sat'] )
nbDays = 0
for year in range( 1950,y ):
	if( ( ( year%4==0 ) and ( year%100!=0 ) ) or ( year%400==0 ) ):
		nbDays += 366
	else:
		nbDays += 365
for month in range(1,m):
	if( ( ( year%4==0 ) and ( year%100!=0 ) ) or ( year%400==0 ) ):
		nbDays += DayOfMonth[1][month]
		LeapYear = 1
	else:
		nbDays += DayOfMonth[0][month]
nbDays += d- 1
Result = (nbDays) % 7
Month = ['January','February','March','April','May','June','July','August','September','October','November','December']
print '\t' , Month[m-1] , y
print 'Su Mo Tu We Th Fr Sa '
for i in range ( 0,Result ):
	print '  ',
print ' 1',
if( Result%7 == 6 ):
	print
for i in range(2,DayOfMonth[LeapYear][m]):
	if(Result%7 == 6):
		print
		print '%2d' %(i),
	else:
		print '%2d' %(i),
   Result += s1