from task_3 import Data, Router, Server


def test_link_servers():
    """Test for check link servers for one router"""

    router = Router()
    router.link(Server())
    router.link(Server())
    assert len(router.servers) == 2
    assert list(router.servers.keys()) == [1, 2]


def test_unlink_servers():
    """Test for checl unlink server of router"""

    router = Router()
    server_2 = Server()
    router.link(Server())
    router.link(server_2)
    router.link(Server())
    assert list(router.servers.keys()) == [1, 2, 3]
    router.unlink(server_2)
    assert len(router.servers) == 2
    assert list(router.servers.keys()) == [1, 3]


def test_get_ip():
    """Test for get ip for server"""

    router = Router()
    router.link(Server())
    server_2 = Server()
    router.link(server_2)
    assert server_2.get_ip() == 2


def test_send_data_router():
    """Test for checksend data for router"""

    router = Router()
    server_from = Server()
    router.link(server_from)
    server_to = Server()
    router.link(server_to)
    data = Data("hello", server_to.get_ip())
    assert len(router.buffer) == 0
    server_from.send_data(data)
    assert len(router.buffer) == 1
    assert router.buffer[0].data == data.data


def test_send_data_server():
    """Test for checksend data for router and server"""

    router = Router()
    server_from = Server()
    router.link(server_from)
    server_to = Server()
    router.link(server_to)
    data = Data("hello", server_to.get_ip())
    server_from.send_data(data)
    assert len(router.buffer) == 1
    router.send_data()
    result = server_to.get_data()
    assert result[0].data == data.data
    assert len(router.buffer) == 0
