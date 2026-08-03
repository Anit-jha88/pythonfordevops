cpu=int(input("enter the cpu"));  #thake iput from user

if cpu > 50:

    print("Cup over load")

elif cpu > 20 and cpu < 50:

    print("send alert")


else:
    
    print("cpu ok")