#요세푸스 문제
#큐, 원형링크드리스트 이외 방법

# 스택 사용
class Stack:
    def __init__(self):
        self.stack = []
# 입력 값 추가
    def push(self, num):
        for i in range(1, num+1):
            self.stack.append(i)
# 제거
    def pop(self, man):
        if man < len(self.stack):
            return self.stack.pop(man)
        return None

# 크기 확인
    def size(self):
        return len(self.stack)

# 요세라는 스택 생성
yose = Stack()
#입력 값만큼 스택에 저장, 배수를 변수 k에 지정
n, k = map(int, input().split())
yose.push(n)
# 죽는 사람을 리스트로
kill = []
man = 0
# 크기가 0이 될 때까지
while yose.size() > 0:
    man = (man + (k-1)) % len(yose.stack) # 모듈러 방식 활용
    kill.append(yose.pop(man)) # kill 리스트에 담기

print("<", ", ".join(map(str, kill)), ">", sep="") # 리스트를 문자열로 변환




"""
while yose.size != 0: # 스택이 다 빌 때까지
    #if yose.size > b: # 스택 크기가 배수보다 큰 경우
        circle = yose.size # circle은 스택에 돌고 도는 수
        for i in range(yose.size): # 남은 인원 수만큼 진행
            if circle > k*i: # 남은 인원 수가 배수의 일정 수 곱보다 크면
                yose.pop(k*i) # 넘지 않은 배수는 삭제
            else : # 남은 인원 수가 배수의 일정 수 곱보다 작으면 남은 인원 수에 죽고 남은 인원 수를 더해야 함
                circle = circle + yose.size

"""




