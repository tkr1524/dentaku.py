print("四則演算電卓")

while True:
	a = float(input("一つ目の数字"))
	op = input("計算方法(+ - × ÷):")
	b = float(input("2つ目の数字"))
	
	if op == "+":
		print("解:", a + b)
		
	elif op == "-":
			print("解:", a - b)
			
	elif op == "×":
			print("解:", a * b)
			
	elif op == "÷":
			if b == 0:
				print("未定義")
			else:
				print("解:", a / b)
				
	else:
			print("計算不可")
			
	again = input("もう一度計算する(y/n):")
		
	if again == "n":
			print("終了します")
			break
