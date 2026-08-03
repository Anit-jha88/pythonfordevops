# create a function that can be reuse the and it show system info
import psutil

def systemdetail():

    cpu = psutil.cpu_percent(interval=1);

    memory = psutil.virtual_memory().percent;

    disk = psutil.disk_usage('/').percent;


    systeminfo = {

        "cpu" : cpu,
        "memory" : memory,
        "disk" : disk

    }

    print(systeminfo);