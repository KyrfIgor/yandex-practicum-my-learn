import time
from threading import Thread, current_thread


def custom_func(n):
    th = current_thread()
    print(f"{th.name} started")

    for _ in range(n):
        time.sleep(1)
        print(f"{th.name} still alive")

    print(f"{th.name} finished")


if __name__ == '__main__':
    main_thread = current_thread()
    print(f"{main_thread.name} started")

    child_thread = Thread(name="ChildThread", target=custom_func, args=(5,))
    child_thread.start()

    print(f"{main_thread.name} finished")