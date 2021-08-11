s = set()
# print(type(s))
l = [1, 2, 3, 4]
s_from_list = set(l)
print(s_from_list)
print(type(s_from_list))
s.add(1)
s.add(2)
# l.append(33)
# print(l)
s.remove(2)
s1 = {4, 6}
print(s.isdisjoint(s1))
# some others-union ,intersection , symmetry etc