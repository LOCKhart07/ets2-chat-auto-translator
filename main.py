from ets2.ets2 import Ets
import time

def main():
    ets = Ets()
    try:
        ets.tail()
    except:
        print("No log file found")
        exit()

    while (True):
        ets.translateMessage(True)
        time.sleep(0.01)

if __name__ == "__main__":
    main()