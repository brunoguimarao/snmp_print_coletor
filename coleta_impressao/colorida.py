from pysnmp.hlapi import *

# Define o OID para o contador de páginas coloridas
OID_COLORIDA = '1.3.6.1.2.1.43.10.2.1.4.1.2'

def coletar_impressao_colorida(ip, comunidade):
    # Cria uma sessão SNMP com a impressora para o contador de páginas coloridas
    iterator = getCmd(SnmpEngine(),
                      CommunityData(comunidade),
                      UdpTransportTarget((ip, 161)),
                      ContextData(),
                      ObjectType(ObjectIdentity(OID_COLORIDA)))

    # Obtém o valor do contador de páginas coloridas
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
    if errorIndication:
        return f'Erro ao obter o contador de páginas coloridas da impressora {ip}: {errorIndication}'
    else:
        for varBind in varBinds:
            return varBind[1]
