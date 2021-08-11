l1 = ["Bhindi", "Aloo", "chopsticks", "chowmein"]

# i = 1
# for item in l1:
#     if i%2 is not 0:
#         print(f"Jarvis please buy {item}")
#     i += 1

for index, item in enumerate(l1):
    if index%2==0:
        print(f"Jarvis please buy {item}")

# But if you want to enumerate through both keys and values this is the way:
# example_dict = {1:'a', 2:'b', 3:'c', 4:'d'}
# for i, (k, v) in enumerate(example_dict.items()):
#     print(i, k, v)
# Which outputs:

# 0 1 a
# 1 2 b
# 2 3 c
# 3 4 d


"""The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.

The enumerate() function adds a counter as the key of the enumerate object.
enumerate(iterable, start)

x = ('apple', 'banana', 'cherry')
y = enumerate(x)
output:
[(0, 'apple'), (1, 'banana'), (2, 'cherry')]
"""  
