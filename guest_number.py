import random
r = random.randint(1 , 100)
count = 0
while True:
	count += 1   # count = count + 1的快寫法
	a = input('請猜數字:')
	a = int(a)
	if a < r:
		print('比答案小')
	elif a > r:
		print('比答案大')
	else:
		print('恭喜你 ~ 終於猜對了!!!')
		print('這是你猜的第' ,count , '次')
		break
	print('這是你猜的第' ,count , '次')