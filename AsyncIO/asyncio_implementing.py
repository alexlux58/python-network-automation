import asyncio
import time

# Asynchronous Programming: asyncio provides a framework for writing single-threaded concurrent code using coroutines,
# multiplexing I/O access, and running network clients and servers.

# Event Loop: The core feature of asyncio is the event loop, which is the central execution device.
# It provides multiple facilities including registering, executing, and cancelling delayed calls (timers),
# and creating client and server transports for various kinds of communication.

# Coroutines: A key aspect of asyncio, coroutines are special functions that work asynchronously.
# They are defined with async def and allow the use of await to pause their execution until the awaited task is complete, without blocking the event loop.

# Futures and Tasks: These are objects that represent the eventual result of asynchronous operations.
# A Task is a subclass of Future that runs a coroutine. When a coroutine awaits on a Future,
# it yields control back to the event loop, which can then keep running other code until the Future is ready.


def sync_f():
    print('one', end=' ')
    # I'm simulating an expensive task like working with an external resource. I want it to wait for 1 sec
    time.sleep(1)
    print('two', end=' ')

# ASYNCHRONOUS


async def async_f():
    print('one', end=' ')
    await asyncio.sleep(1)

    print('two', end=' ')


async def main():
    # Note that there are 3 awaitable objects: coroutines, tasks and futures.
    tasks = [async_f() for _ in range(3)]

    # we schedule the coroutines to run asap by gathering the tasks like this:
    await asyncio.gather(*tasks)


s = time.time()

# The entrance point of any asyncio program is asyncio.run(main()), where main() is a top-level coroutine.
# asyncio.run() was introduced in Python 3.7, and calling it creates an event loop
# and runs a coroutine on it for you. run() creates the event loop.
asyncio.run(main())  # prints out: one one one two two two and takes 1 second
print(f'Execution time (ASYNC):{time.time()-s}')

print('\n')

s = time.time()
for _ in range(3):
    sync_f()  # prints out: one two one two one two and takes 3 seconds
print(f'Execution time (SYNC):{time.time()-s}')
