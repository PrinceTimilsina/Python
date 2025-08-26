phscale = int(input("Enter PH scale: "))
if phscale>7:
	print('Basic')
elif phscale<7:
	print('Acidic')
else:
	print('Neutral')