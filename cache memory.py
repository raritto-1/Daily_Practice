from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n * 5

print(fx(2))
print('done for 5')
print(fx(8))
print('done for 6')
print(fx(6))
print('done for 9')
print(fx(7))
print('done for 3')
print(fx(8))
print('done for 95')


print(fx(2))
print('done for 5')
print(fx(8))
print('done for 6')
print(fx(6))
print('done for 9')
print(fx(7))
print('done for 3')
print(fx(8))
print('done for 95')