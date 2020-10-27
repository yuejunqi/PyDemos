import pickle

d = dict(name='Bob', age=20, score=80, talkLouder=False)
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()
print("序列化存储成功")
f1 = open('dump.txt', 'rb')
d1 = pickle.load(f1)
print(d1)
print("反序列化存储成功")


