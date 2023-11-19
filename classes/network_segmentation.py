import ipaddress

class Segments:
    total_segments: int = 0

    def __init__(self, init_ip: str, segments: list) -> None:
        self.init_ip = ipaddress.IPv4Address(init_ip)
        self.segments = segments

    @classmethod
    def total_segments(cls) -> int:
        return cls.total_segments

    @classmethod
    def add_segment(cls) -> None:
        cls.total_segments += 1

    def next_segment(self) -> None:
        pass

    def host_bits(self) -> None:
        pass

    def get_network_info(self) -> None:
        pass