# v1.4) https://github.com/inhadeepblue/2024_KEB_datastructure_algorithm 의
# v0.7 guess number 예제를 자동화하고 로그파일(guess.txt)을 남기도록 코드를 수정하시오.
# 단, 해당 프로그램이 로그시간을 갖도록 한다

import random

def auto_input_number(low, high,chance) -> int:
    guess = (low+high)//2
    answer = random.randint(low,high)
    with open ('guess.txt', 'w') as fp:
        while chance != 0:
            if guess == answer:
                print(f'You win. Answer is {answer}')
                fp.write(f'You win. Answer is {answer}')
                return
            elif guess > answer:
                chance = chance - 1
                print(f'{guess} is bigger. Chance left : {chance}')
                fp.write(f'{guess} is bigger. Chance left : {chance}')
                high = (high+low)//2
                guess = (low + high) // 2

            else:
                chance = chance - 1
                print(f'{guess} is lower. Chance left : {chance}')
                fp.write(f'{guess} is lower. Chance left : {chance}')
                low = (high+low)//2
                guess = (low + high) // 2
        else:
            print(f'You lost. Answer is {answer}')
            fp.write(f'you lost. Answer is {answer}')

auto_input_number(1,100,7)
