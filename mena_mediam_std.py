import numpy as np

length = int(input('Length of your list: '))
random_list = np.random.randn(length)  

mean = np.mean(random_list)
median = np.median(random_list)
std_deviation = np.std(random_list)

print("Random List:", random_list)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_deviation)
