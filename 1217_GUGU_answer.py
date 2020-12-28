import random
import time

correctAns = 0
wrongAns = 0

count = int(input("몇 번 할까요?"))

while count !=0:
    a = random.randint(3, 9)
    b = random.randint(3, 9)

    if a == 5 or b == 5:
        continue
    count = count -1

    print("%d X %d?" %(a,b))
    startTime = time.time( )
    product = int(input( ))
    endTime = time.time( )
    print("%.1f 초만에 답을 했어요!!"%(endTime-startTime))
    timeout=endTime-startTime
    if timeout>5 :
        print("시간을 초과하였습니다.")
        break

    if product == a*b:
        correctAns = correctAns+1
        print("맞혔습니다.\n")
    else:
        wrongAns = wrongAns+1
        print("다시 도전하세요\n")

print("%d번 중 %d번 밎혔어요!!" %(correctAns +wrongAns,correctAns))
