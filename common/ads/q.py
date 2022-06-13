class Queue:
    def __init__(self):
        self.__container = []

    def __len__(self):
        return len(self.__container)

    def enqueue(self, value):
        self.__container.append(value)

    def dequeue(self):
        return self.__container.pop(0)

    def isempty(self):
        return len(self.__container) == 0
