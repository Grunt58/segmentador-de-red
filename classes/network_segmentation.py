import ipaddress

class Segments:
    total_segments: int = 0

    def __init__(self, init_ip: str, hosts: list) -> None:
        self.init_ip = ipaddress.IPv4Address(init_ip)
        self.hosts = hosts
        self.bits = []
        self.segment = {
            'Host solicitados': None,
            'Host encontrados': None,
            'Dirección de red': None,
            'Máscara digital': None,
            'Máscara decimal': None,
            'Primera Ip utilizable': None,
            'Última Ip utilizable': None,
            'Dirección de BR': None
        }

    @classmethod
    def total_segments(cls) -> int:
        return cls.total_segments

    @classmethod
    def add_segment(cls) -> None:
        cls.total_segments += 1

    def next_segment(self, mask: int) -> None:
        # Dirección de red del segmento
        network = ipaddress.IPv4Network((self.init_ip, mask), strict=False)
        self.segment.update({'Dirección de red': network})
        self.segment.update({'Máscara decimal': network.netmask})

        # Dirección Broadcast
        br_address = network.broadcast_address
        self.segment.update({'Dirección de BR': br_address})

        # Primera y última IP ultilizable
        first_ip = network.network_address + 1
        self.segment.update({'Primera Ip utilizable': first_ip})
        last_ip = br_address - 1
        self.segment.update({'Última Ip utilizable': last_ip})

        self.init_ip += 2**(32 - mask)
        return

    def set_mask(self, host: int) -> int:
        # Máscara de subred
        host_bits = host.bit_length() # Número de bits para representarse así mismo en binario
        mask = 32 - host_bits
        # host disponibles dentro del segmento
        usable_hosts = 2**(32 - mask) - 2
        # Asegura que los host solicitados no superen a los disponibles
        if usable_hosts < host:
            mask -= 1
            usable_hosts = 2**(32 - mask) - 2

        self.segment.update({'Host solicitados': host})
        self.segment.update({'Host encontrados': usable_hosts})
        return mask

    def host_bits(self, mask: int) -> None:
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

        digital_mask = ''.join(map(str,self.bits)) + "=/" + str(mask)
        self.segment.update({'Máscara digital': digital_mask})
        return

    def get_network_info(self) -> None:
        for key, value in self.segment.items():
            print(f"{key:.<30}{value}")

    def export_network_info(self) -> list:
        return list(map(str, self.segment.values()))