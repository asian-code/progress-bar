import time


def display_progress(timer=.1, value=0):
    while value <= 100:
        print("[ok] downloading: {}%".format(value), end="")
        time.sleep(timer)
        value += 1
        print("\r", end="")
    print("\n[+] Download is complete")


display_progress()
