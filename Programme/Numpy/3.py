def DictMergeSum(d1, d2):
    m = {}

    for key, value in d2.items():
        try:
            m[key] = value + d1[key]
        except KeyError:
            m[key] = value
    for key, value in d1.items():
        try:
            m[key]
        except KeyError:
            m[key] = value

    return m

d1 = dict(a=1, b=1, c=1)
d2 = dict(a=3, c=4, d=1)

print(DictMergeSum(d1, d2))