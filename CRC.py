divisor = input("Enter the Generator Bits : ") # list(map(int, )))
dividend = input("Enter the Data Bits: ") # list(map(int, ))

def xor(a, b):
	ans = ""
	for i in range(len(a)):
		if a[i] == b[i]:
			ans += "0"
		else:
			ans += "1"
	return ans
# print(xor("10001", "01110"))

def mod2div(num, den):
	temp = num[:len(den)]
	count = len(den)

dividend += "0" * (len(divisor) -1)

print(dividend)
