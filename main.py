import os
from pysnmp.hlapi import *

# Define o endereço IP da impressora e as credenciais SNMP
ip = '10.44.74.37'
comunidade = 'public'

# Define os OIDs para os contadores de páginas monocromáticas e coloridas
oid_monocromatica = '1.3.6.1.2.1.43.10.2.1.4.1.1'

# Cria uma sessão SNMP com a impressora para o contador de páginas monocromáticas
iterator = getCmd(SnmpEngine(),
                  CommunityData(comunidade),
                  UdpTransportTarget((ip, 161)),
                  ContextData(),
                  ObjectType(ObjectIdentity(oid_monocromatica)))

# Obtém o valor do contador de páginas monocromáticas
errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
if errorIndication:
    print(errorIndication)
else:
    for varBind in varBinds:
        print('Número de páginas monocromáticas impressas:', varBind[1])
