from pysnmp.hlapi import *

# Define o OID para a porcentagem do toner preto
OID_TONER_PRETO = '1.3.6.1.2.1.43.11.1.1.9.1.1'

def verificar_toner_preto(ip, comunidade):
    # Cria uma sessão SNMP com a impressora para a porcentagem do toner preto
    iterator = getCmd(SnmpEngine(),
                      CommunityData(comunidade),
                      UdpTransportTarget((ip, 161)),
                      ContextData(),
                      ObjectType(ObjectIdentity(OID_TONER_PRETO)))

    # Obtém a porcentagem do toner preto
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
    if errorIndication:
        return f'Erro ao obter a porcentagem do toner preto da impressora {ip}: {errorIndication}'
    else:
        for varBind in varBinds:
            return varBind[1]
