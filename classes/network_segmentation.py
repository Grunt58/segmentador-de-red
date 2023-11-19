import ipaddress

class Segments:
    total_segments: int = 0

    def __init__(self, network: str, segments: list) -> None:
        self.network = ipaddress.IPv4Address(network)
        self.segments = segments

    @classmethod
    def total_segments(cls) -> int:
        return cls.total_segments
    
    @classmethod
    def add_segment(cls) -> None:
        cls.total_segments += 1