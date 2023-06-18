print(10&7)

print(10|7)

print(10^7)

print(123&7)

print(123&456)

print(123|456)

print(123^456)

# # & (비트논리곱 : and 연산자) : 둘다 참일때 참
# | (비트논리합 : or 연산자) : 둘중에 하나라도 참임녀 참
# ^ (배타적비트논리합 : xor연산자) : 둘다 같은 값이면 거짓, 다르면 참
# 비트 연산자의 개념
# 정수를 2진수로 변환한 후 각 자리의 비트끼리 연산 수행
# 비트 연산자의 종류 : &(비트논리곱), |(비트논리합), ^(비트배타적논리합), ~(비트부정), <<(비트왼쪽이동), >>(비트오른쪽이동)

a = 10
~a  # 1의 보수

~a+1    # 2의 보수 = 1의 보수 + 1

# 비트 부정 연산자(또는 보수 연산자) : 두 수를 연산하는 것이 아니라, 하나만 가지고 각 비트를 반대로 만드는 연산
# 반전된 값을 1의 보수라고 하고, 그 값에 1을 더한 값을 2의 보수라고 한다.
# 2의 보수는 해당 값이 양수일 경우 음수(-)값(음수일떄는 양수)을 찾고자 할 때 사용

a = 10
a<<1

a<<2

a<<3

a<<4

# 시프트연산자 (<<: 왼쪽 시프트 연산자, >>: 오른쪾 시프트 연산자)
# 왼쪽 시프트 연산자 : 왼쪽으로 시프할 때 마다 2의n승을 곱한 효과

a = 10

a>>1

a>>2

a>>3

# 오른쪽으로 시프트 연산자 : 오른쪽으로 시프트할떄마다 2의 n승으로 나눈 몫의 효과