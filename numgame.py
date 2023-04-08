import random

sum = 0
min = 1
max = 10

num = random.randint(min,max)
#print("生成的数字为:%d" % num)
print("随机生成了%d-%d之间的数字,猜一猜吧!" % (min,max))

while True:
    res = int(input("请输入数字:\n"))
    if res > num:
        print("太大了")
        sum += 1
    elif res < num:
        print("太小了")
        sum +=1
    else:
        print("答对了")
        sum +=1
        print("你猜了%d次" % sum)
        break

print("Bye!")