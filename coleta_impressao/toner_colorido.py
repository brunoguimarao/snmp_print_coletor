from pysnmp.hlapi import *

# Define o OID para a porcentagem dos toners coloridos
OID_TONER_CYAN = '1.3.6.1.2.1.43.11.1.1.9.1.2.1'
OID_TONER_MAGENTA = '1.3.6.1.2.1.43.11.1.1.9.1.2.2'
OID_TONER_YELLOW = '1.3.6.1.2.1.43.11.1.1.9.1.2.3'

def verificar_toner_colorido(ip, comunidade):
    # Cria sessões SNMP com a impressora para a porcentagem dos toners coloridos
    iterator_cyan = getCmd(SnmpEngine(),
                           CommunityData(comunidade),
                           UdpTransportTarget((ip, 161)),
                           ContextData(),
                           ObjectType(ObjectIdentity(OID_TONER_CYAN)))
    iterator_magenta = getCmd(SnmpEngine(),
                              CommunityData(comunidade),
                              UdpTransportTarget((ip, 161)),
                              ContextData(),
                              ObjectType(ObjectIdentity(OID_TONER_MAGENTA)))
    iterator_yellow = getCmd(SnmpEngine(),
                             CommunityData(comunidade),
                             UdpTransportTarget((ip, 161)),
                             ContextData(),
                             ObjectType(ObjectIdentity(OID_TONER_YELLOW)))

    # Obtém a porcentagem dos toners coloridos
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator_cyan)
    if errorIndication:
        return None, None, None
    else:
        cyan = varBinds[0][1]

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator_magenta)
    if errorIndication:
        return None, None, None
    else:
        magenta = varBinds[0][1]

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator_yellow)
    if errorIndication:
        return None, None, None
    else:
        yellow = varBinds[0][1]

    return cyan, magenta, yellow
