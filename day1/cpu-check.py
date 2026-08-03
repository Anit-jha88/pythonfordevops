import psutil
thesold = float(input("Enter cpu thesold"))


for i in range(5):
    if psutil.cpu_percent(interval=1) > thesold:
        print("cpu is unhealthy")
    