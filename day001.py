# 序列化&反序列化
# class序列化为json
import json

d = dict(name='Bob', age=20, score=80, talkLouder=False)
j = json.dumps(d)
print("序列化后的json：", j)

d1 = json.loads(j)
print("反序列化后的dict：", d1)


class Student(object):

    def __init__(self, name, age, score, absent):
        Student.name = name
        Student.age = age
        Student.score = score
        Student.absent = absent


def student2dict(stu):
    # 将对象stu的数据转为dict对象返回
    return {"name": stu.name,
            "age": stu.age,
            "score": stu.score,
            "absent": stu.absent
    }


def dict2student(dic):
    # 将对象stu的数据转为dict对象返回
    return Student(name=dic['name'], age=dic['age'], score=dic['score'], absent=dic['absent'])


std = Student('小明', 20, 88, False)
j2 = json.dumps(Student, default=student2dict)
print("python任意class对象实例序列化为json数据：", j2)

std1 = json.loads(j2, object_hook=dict2student)
print("json数据反序列化为python任意class对象实例：", std1)
print(std1.name, std1.age, std1.score, std1.absent)
