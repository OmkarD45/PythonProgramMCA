'''
Q.22 Write python program to demonstrate thread synchronization and resolve
the race condition.
'''
import threading

counter = 0
lock = threading.Lock()

def increment_counter():
    global counter
    with lock:
        for _ in range(1000000):
            counter += 1

thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Final counter value:", counter)
