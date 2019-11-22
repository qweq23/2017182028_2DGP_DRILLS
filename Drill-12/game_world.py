
# layer 0: Background Objects
# layer 1: Foreground Objects
objects = [[],[]]


def add_object(o, layer):
    objects[layer].append(o)


def add_objects(l, layer):
    objects[layer] += l


def remove_object(o):
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o
            break




def clear():
    global objects
    for o in all_objects():
        del o  # 각각 인스턴스 된 아이들을 삭제함

    for i in range(len(objects)):
        for j in range(len(objects[i])):
            objects[i].pop()  # 월드 객체 리스트를 비워줌

def destroy():
    clear()
    objects.clear()


def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o

