import os
from pysnmp.hlapi import *

# Define uma lista de endereços IP da impressora e as credenciais SNMP
ips = ['10.44.74.37', '10.44.74.28']
comunidade = 'public'

# Define os OIDs para os contadores de páginas monocromáticas e coloridas
oid_monocromatica = '1.3.6.1.2.1.43.10.2.1.4.1.1'

# Loop através dos endereços IP e obter o número de páginas impressas de cada impressora
for ip in ips:
    # Cria uma sessão SNMP com a impressora para o contador de páginas monocromáticas
    iterator = getCmd(SnmpEngine(),
                      CommunityData(comunidade),
                      UdpTransportTarget((ip, 161)),
                      ContextData(),
                      ObjectType(ObjectIdentity(oid_monocromatica)))

    # Obtém o valor do contador de páginas monocromáticas
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
    if errorIndication:
        print('Erro:', errorIndication)
    else:
        for varBind in varBinds:
            print(f'Impressora {ip}: Número de páginas monocromáticas impressas:', varBind[1])
