# https://www.acmicpc.net/problem/24416

N = int(input())  # 인덱스 지정
f = [0] * (N + 2)  # 피보나치 수를 저장하기 위한 배열 생성

cnt = 0  # 얼마나 반복하는지에 대한 cnt 변수 생성


def fibonacci(n):  # 매개변수로 몇 번째 피보나치 수를 출력할지를 지정
    global cnt  # 전역변수 수정을 위한 글로벌 키워드 사용
    f[1] = 1
    f[2] = 1  # 위 두개는 초기값 설정
    for i in range(3, n + 1):
        cnt += 1  # 횟수 증가
        f[i] = f[i - 1] + f[i - 2]  # 피보나치 수식 진행
    return f[n]  # 결과값 반환


print(
    fibonacci(N), cnt
)  # 함수로 받은 반환값과 그 함수 안에서 증가한 카운트 변수를 한 줄에 표현
