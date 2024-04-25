

l1 = [1, 2, 3, 4, 5, 6, 7, 8]
v_sum = 0

for i in l1:
    if i % 2 == 0:
        v_sum += i

print(v_sum)

# for one_element in l1:
#     print(one_element)

d1 = {
    'one': 123,
    'two': 456
}

for k in d1.keys():
    print(k, type(d1.get(k)))

i = 0
import time

# while i < 100:
#     print('hello!', i)
#     i += 1
#     time.sleep(1)

for i in [1, 2, 3]:
    print(f'Hi {i}')
