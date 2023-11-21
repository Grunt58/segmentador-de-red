import ipaddress

class Segments:
    total_segments: int = 0

    def __init__(self, init_ip: str, hosts: list) -> None:
        self.init_ip = ipaddress.IPv4Address(init_ip)
        self.hosts = hosts
        self.bits = []

    @classmethod
    def total_segments(cls) -> int:
        return cls.total_segments

    @classmethod
    def add_segment(cls) -> None:
        cls.total_segments += 1

    def next_segment(self) -> None:
        pass

    def host_bits(self, mask: int) -> list:
        # limpia los bits de la lista para el siguiente segmento
        self.bits.clear()
        # Cqntidad de bits activos por segmento
        active_bits = 8 - (32 - mask)
        # Agrege los bits activos '1' y los inactivos '0'
        for _ in range(8):
            if active_bits > 0:
                self.bits.append(1)
                active_bits -= 1
            else:
                self.bits.append(0)
        return self.bits

    def get_network_info(self) -> None:
        pass