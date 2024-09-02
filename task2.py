from task1 import Stack

"""Используя стек из задания 1, решите задачу на проверку сбалансированности скобок. 
Сбалансированность скобок означает, что каждый открывающий символ имеет соответствующий 
ему закрывающий, и пары скобок правильно вложены друг в друга.
Пример сбалансированных последовательностей скобок:

(((([{}]))))
[([])((([[[]]])))]{()}
{{[()]}}
Несбалансированные последовательности:

}{}
{{[(])]}}
[[{())}]

Программа ожидает на вход строку со скобками. На выход сообщение: 
«Сбалансированно», если строка корректная, и «Несбалансированно», 
если строка составлена неверно."""
def balance(symbols):
    balance_list = ["(", "[", "{"]
    revers_list = [")", "]", "}"]
    if len(symbols) % 2 != 0:
        return False
    else:
        for symbol in symbols:
            if symbol in balance_list:
                s.push(symbol)
            else:
                if s.is_empty():
                    return False
                else:
                    if balance_list[revers_list.index(symbol)] in s.peek() or symbol in s.peek():
                        s.pop()

        if len(s.stack) > 0:
            return False

s = Stack()

in_symbols = input("Ввод: ")

if __name__ == '__main__':
    print("Несбалансированно") if balance(in_symbols) == False else print("Сбалансированно")



