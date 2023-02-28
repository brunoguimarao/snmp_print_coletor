from pysnmp.hlapi import *

# Define o OID para a porcentagem do kit de manutenção
OID_KIT_MANUTENCAO = '1.3.6.1.2.1.43.13.1.1.10.1'

def verificar_kit_manutencao(ip, comunidade):
    # Cria uma sessão SNMP com a impressora para a porcentagem do kit de manutenção
    iterator = getCmd(SnmpEngine(),
                      CommunityData(comunidade),
                      UdpTransportTarget((ip, 161)),
                      ContextData(),
                      ObjectType(ObjectIdentity(OID_KIT_MANUTENCAO)))

    # Obtém a porcentagem do kit de manutenção
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
    if errorIndication:
        return f'Erro ao obter a porcentagem do kit de manutenção da impressora {ip}: {errorIndication}'
    else:
        for varBind in varBinds:
            return varBind[1]
