def solution(price, grade):
	answer = 0
	if grade == "S":
		sal = price * 0.05
		answer = price - int(sal)
	elif grade == "G":
		sal = price * 0.1
		answer = price - int(sal)
	elif grade == "V":
		sal = price * 0.15
		answer = price - int(sal)
	return answer

price1 = 2500
grade1 = "V"
ret1 = solution(price1, grade1)

print("solution 함수의 반환 값은", ret1, "입니다.")

price2 = 96900
grade2 = "S"
ret2 = solution(price2, grade2)

print("solution 함수의 반환 값은", ret2, "입니다.")