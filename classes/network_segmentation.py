import ipaddress

class segments:
    total_segments: int = 0

    def __init__(self) -> None:
        pass

    @classmethod
    def total_segments(cls) -> int:
        return cls.total_segments
    
    @classmethod
    def add_segment(cls) -> None:
        cls.total_segments += 1