# e = {53: {35, 56, 34}}
# print(e[53])
# print(list(e[53]))

para = "hello, this is python in working."
l = []
for i in para.split(" "):
    l.append(i)
print(l)
s = set(l)
print(s)
d = {}
for x in s:
    d[x] = "raj"
print(d)


for x in d.items():
    print(x)

for x in d.values():
    print(x)
