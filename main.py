from ets2.ets2 import Ets


def main():
    ets = Ets()
    try:
        last_line = ets.tail()
    except:
        print("No log file found")
        exit()

    while (True):
        ets.translateMessage(True)


if __name__ == "__main__":
    main()
