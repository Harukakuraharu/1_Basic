class Data:
    def __init__(self, data: str, ip: int):
        self.data = data
        self.ip = ip

    def __repr__(self):
        return self.data


class Server:
    def __init__(self) -> None:
        self.ip_address: int | None = None
        self.buffer: list[Data] = []
        self.router: Router

    def send_data(self, data: Data):
        """Send data for router"""

        self.router.buffer.append(data)

    def get_data(self) -> list[Data]:
        """Get list of received data"""

        return self.buffer

    def get_ip(self) -> int | None:
        """Get server ip address"""

        return self.ip_address


class Router:
    def __init__(self) -> None:
        self.buffer: list[Data] = []
        self.servers: dict[int, Server] = {}

    def link(self, server: Server) -> None:
        """Link server with router"""

        server.ip_address = (
            max((server for server in self.servers), default=0) + 1
        )
        self.servers[server.ip_address] = server
        server.router = self

    def unlink(self, server: Server) -> None:
        """Unlink server on router"""
        if server.ip_address is not None:
            self.servers.pop(server.ip_address)

    def send_data(self) -> None:
        """Send data dor server"""

        for obj in self.buffer:
            self.servers[obj.ip].buffer.append(obj)
        self.buffer = []
