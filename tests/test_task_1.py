from task_1 import LinkedList, ObjList


def test_add_obj():
    """Test for add object in LinkedList"""

    lst = LinkedList()
    obj_head = ObjList("hello")
    obj_tail = ObjList("world")
    lst.add_obj(obj_head)
    lst.add_obj(obj_tail)
    assert lst.head == obj_head
    assert lst.tail == obj_tail
    assert obj_head.get_prev is None
    assert obj_head.get_next == obj_tail
    assert obj_tail.get_prev == obj_head
    assert obj_tail.get_next is None


def test_remove_obj():
    """Test for remove object in LinkedList"""

    lst = LinkedList()
    obj = ObjList("hello")
    lst.add_obj(obj)
    lst.add_obj(ObjList("world"))
    lst.remove_obj()
    assert lst.head == obj
    assert lst.tail == obj
    assert obj.get_next is None
    assert obj.get_prev is None


def test_get_data():
    """Test for get list of objects from LinkedList"""

    lst = LinkedList()
    lst.add_obj(ObjList("hello"))
    lst.add_obj(ObjList("world"))
    result = lst.get_data()
    assert len(result) == 2
    assert result == ["hello", "world"]
