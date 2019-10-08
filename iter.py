# d = {"a": 1, "b": 2, "c": 3}
# for key in d:
#     print(key)
for ch in "ABC":
    print(ch)
from collections import Iterable

isinstance("abc", Iterable)
isinstance([1, 2, 3], Iterable)
isinstance(123, Iterable)

#
# enumerate
for i, value in enumerate(["A", "B", "c"]):
    print(i, value)
