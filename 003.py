def primeFactor(n): # n의 가장 큰 소인수를 구한다
    div = 2 # 나누는 수
    while div < int(n ** 0.5): # div가 n의 제곱근보다 작을 동안 반복한다
        if n % div == 0: # n이 div로 나눠지면, 즉 div가 n의 소인수이면
            n = n // div # n을 div로 나눈다
            div = 2 # div는 2로 초기화한다
        else:
            div += 1 # n이 div로 나눠지지 않으면, 즉 div가 n의 소인수가 아니면 div를 1만큼 증가시킨다
    print(n)

primeFactor(600851475143)


