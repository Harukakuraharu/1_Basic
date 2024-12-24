from typing import Any


class ObjList:
    """Node Definition"""

    def __init__(self, data: Any = None) -> None:
        self.__next = None
        self.__prev = None
        self.__data = data

    @property
    def get_next(self):
        return self.__next

    @get_next.setter
    def set_next(self, obj) -> None:
        self.__next = obj

    @property
    def get_prev(self):
        return self.__prev

    @get_prev.setter
    def set_prev(self, obj) -> None:
        self.__prev = obj

    @property
    def get_data(self):
        return self.__data

    @get_data.setter
    def set_data(self, data) -> None:
        self.__data = data


class LinkedList:
    """Class for doubly linked list"""

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add_obj(self, obj: ObjList) -> None:
        """Add an object to the end of the list"""

        if self.head is None:
            self.head = obj
            self.tail = obj
        else:
            self.tail.set_next = obj
            obj.set_prev = self.tail
            self.tail = obj

    def remove_obj(self) -> None:
        """Remove an object to the end of the list"""

        if self.head is None:
            raise AttributeError("List is empty")

        self.tail = self.tail.get_prev
        if self.tail is not None:
            self.tail.set_next = None
        else:
            self.head = None

    def get_data(self) -> list[Any]:
        """Get all objects from list"""

        result = []
        current_obj = self.head
        while current_obj is not None:
            result.append(current_obj.get_data)
            current_obj = current_obj.get_next
        return result

