# Дана строка из любых символов. Вам необходимо вывести букву, которая встречается чаще всего.
# Буквы могут быть любого алфавита. Задание выполняется без учета регистра.
# Оформить в виде функции most_wanted_letter. Аргументом функции является строка с любым содержимым.
# Функция должна возвращать фразу с буквой (например, как на следующем слайде) или фразу с
# предупреждением, что букв здесь нет.

def MostWantedLetter(entradaLetras):
    resultado = 0
    for cadaLetra in entradaLetras:
        if cadaLetra.isalpha():
            if entradaLetras.count(cadaLetra) > resultado:
                laMasBuscado = cadaLetra
                resultado = entradaLetras.count(cadaLetra)
            elif entradaLetras.count(cadaLetra) == resultado:
                if cadaLetra < laMasBuscado:
                    laMasBuscado = cadaLetra
                    resultado = entradaLetras.count(cadaLetra)
    print(laMasBuscado)
entradaLetras = input().lower()
MostWantedLetter(entradaLetras)