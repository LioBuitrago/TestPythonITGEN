# Для решения этой задачи воспользуйтесь словарями. Программа запрашивает количество учеников в классе,
# а затем имя ученика и предметы (через пробел), которые он изучает. Добавьте функции:
# show_all, которая будет выводить содержимое словаря с учениками и предметами, отсортированное по 
# убыванию (ключ – имя ученика).
# student_for_sub, которая принимает имя ученика и возвращает список предметов, которые он изучает.
# sub_for_students, которая принимает предмет и возвращает список учеников, которые его изучают.


def adicion(diccionario, key, listValor):
    if key not in diccionario:
        diccionario[key] = list()
    diccionario[key].extend(listValor)
    return diccionario

def show_all():
    items = clase.items()
    print(sorted(items))

def student_for_sub(x):
    s = clase.get(x)
    if x not in clase:
        print("There are no students with this name.")
    else:
        print(s)

def sub_for_students(item):
    studSubs = []
    for key in clase.keys():
        if item in clase[key]:
            studSubs.append(key)
    print(studSubs)
    if studSubs == 0:
        print("There are no matching students.")

clase = {}

total = int(input("Write numbre of students: "))
for i in range(total):
    Estudiante = str(input("Name of student: "))
    Materias = []
    anadidos = str(input("Subjects of student: "))
    Materias += anadidos.split(' ')
    clase = adicion(clase, Estudiante, Materias)

show_all()
one = str(input("Student's subjetc: "))
student_for_sub(one)
two = str(input("Subject's student: "))
sub_for_students(two)
