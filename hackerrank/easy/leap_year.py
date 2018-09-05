def is_leap(year):

	if(year % 4 == 0):
		if(year % 100 == 0):
			if(year % 400 == 0):
				return True
			return False
		return True
	return False


print("Enter a year:", end=" ")
year = int(input())

if(is_leap(year)):
	print(year, "is a leap year")
else:
	print(year, "isn't a leap year")

