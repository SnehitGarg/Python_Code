import random
import timeit
import sys

def test():
  SETUP_CODE = '''
from __main__ import sort
from random import randint'''
  
  TEST_CODE = '''
array = []
for x in range(1000):
  array.append(x)
sort(array)
  '''
  times = timeit.repeat( setup = SETUP_CODE,
                          stmt = TEST_CODE,  
                          number = 10,
                          repeat = 5) 

  print('Min Time: {}'.format(min(times)))
  print('Max Time: {}'.format(max(times)))