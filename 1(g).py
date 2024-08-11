def check(a,b,c):

	if (a < 0 or b < 0 or c < 0 or (a+b <= c) or (a+c <=b) or (b+c <=a) ):
		print('Not a valid triangle')
		return
		
	s = (a + b + c) / 2
	
	area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
	print('Area of a triangle is %f' %area)



a = int(input("Enter Your Value :"))

b = int(input("Enter Your Value :"))

c = int(input("Enter Your Value :"))

check(a,b,c)

