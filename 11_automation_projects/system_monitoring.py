import psutil
import time
import os


def clearscreen():
    os.system("cls" if os.name == "nt" else "clear")


def show_stats():
    print("")
    print("System resource monitor")
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    print(f"CPU: {cpu}%")
    print(
        f"RAM: {ram.percent}% and {round(ram.used/1e9,2)}GB used of {round(ram.total/1e9,2)}"
    )  # because ram is given in bytes by default
    print(
        f"Disk: {disk.percent}% {round(disk.used/1e9,2)}GB used of {round(disk.total/1e9,2)}"
    )


if __name__ == "__main__":
    try:
        while True:
            # clearscreen()
            show_stats()
            time.sleep(0.01)
    except KeyboardInterrupt:
        print("Stopped")
