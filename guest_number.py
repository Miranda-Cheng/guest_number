import random
r = random.randint(1 , 100)
while True:
	a = input('請猜數字:')
	a = int(a)
	if a < r:
		print('比答案小')
	elif a > r:
		print('比答案大')
	else:
		print('恭喜你 ~ 終於猜對了!!!')
		break