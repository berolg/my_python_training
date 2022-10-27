objects = ['Maths']
objects.append('Literature')
objects.append('Biology')
objects.append('Russian')
objects.append('Chemistry')

print(objects[0] + '\n' + objects[1] + '\n' + objects[2] + '\n' + objects[3] + '\n' + objects[4])

for obj in objects:
    obj_id = objects.index(obj)
    print(objects[obj_id])

