import signal, time

def handler(signum, time):
    print("\nI got a SIGINT, but i am not stopping.")

signal.signal(signal.SIGINT, handler)

i=0
while True:
    time.sleep(0.1)
    print("\r{}".format(i), end="")
    i += 1
