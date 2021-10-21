def solution(N, M):
	answer = 0
	count = 0
	for i in range(N, M):
		if i % 2 == 0:
			count = i*i
			answer += count
	return answer
N = 4
M = 7
ret = solution(N, M)

print("solution 함수의 반환 값은", ret, "입니다.")