# 7/22/2020 Saidakbar P
# context manager
# context manager helps us create a temporary env for performing some actions.
with open('my_file.txt') as my_file:
    text = my_file.read()
print(text)

with open('alice.txt') as file:
    text = file.read()
n = 0
for word in text.split():
    if word.lower() in ['cat', 'cats']:
        n += 1

print('Lewis Caroll uses the word "cat" {} times'.format(n))

import contextlib
import time
@contextlib.contextmanager
def timer():
    """Time the execution of a context block.

    Yields:
      None
    """
    start = time.time()
    # Send control back to the context block

    end = time.time()
    print('Elapsed: {:.2f}s'.format(end - start))
    yield 
with timer():
    print('This should take approximately 0.25 seconds')
    time.sleep(0.25)
	
@contextlib.contextmanager
# checking context manager for read only files
def read_only_file(filename):
    """Opens file for read only
      Args:
         filename
      Yields:
         file content
    """
    read_only_file = open(filename, 'r')
    yield read_only_file
    read_only_file.close()
with read_only_file('my_file.txt') as my_file:
    open_read_only = my_file.read()
    print(open_read_only)
# record 10 timesteps of price data by writing it to the file NVDA.txt
with stock('NVDA') as nvda:
    with open('NVDA.txt', 'w') as f_out:
        for _ in range(10):
              value = nvda.price()
              print('Logging ${:.2f} for NVDA'.format(value))
              f_out.write('{:.2f}\n'.format(value))
			  

