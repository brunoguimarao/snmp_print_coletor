from pysnmp.hlapi import *

# Define o OID para o contador de páginas monocromáticas
OID_MONOCROMATICA = '1.3.6.1.2.1.43.10.2.1.4.1.1'

def coletar_impressao_monocromatica(ip, comunidade):
    # Cria uma sessão SNMP com a impressora para o contador de páginas monocromáticas
    iterator = getCmd(SnmpEngine(),
                      CommunityData(comunidade),
                      UdpTransportTarget((ip, 161)),
                      ContextData(),
                      ObjectType(ObjectIdentity(OID_MONOCROMATICA)))

    # Obtém o valor do contador de páginas monocromáticas
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
    if errorIndication:
        return f'Erro ao obter o contador de páginas monocromáticas da impressora {ip}: {errorIndication}'
    else:
        for varBind in varBinds:
            return varBind[1]
