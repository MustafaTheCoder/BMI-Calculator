
Height=float(input("Enter Height In Centimeters: "))
Weight=float(input("Enter Weight In Kg: "))
Height = Height/100
BMI=Weight/(Height*Height)
print("BMI: ",BMI)
if(BMI>0):
	if(BMI<=16):
		print("You are severely underweight!")
	elif(BMI<=18.5):
		print("You are underweight!")
	elif(BMI<=25):
		print("You are healthy!")
	elif(BMI<=30):
		print("You are overweight!")
	else: print("You are severely overweight!")
else:("Enter Valid Details!")