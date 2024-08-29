"""Нужно реализовать класс Stack со следующими методами:
is_empty — проверка стека на пустоту. Метод возвращает True или False;
push — добавляет новый элемент на вершину стека. Метод ничего не возвращает;
pop — удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека;
peek — возвращает верхний элемент стека, но не удаляет его. Стек не меняется;
size — возвращает количество элементов в стеке.
"""

class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return not self.stack

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Пустой Stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Пустой Stack")
        return self.stack[-1]

    def size(self):
        return len(self.stack)