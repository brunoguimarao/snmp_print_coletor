import os
import datetime
from pysnmp.hlapi import *

# Define uma lista de endereços IP da impressora e as credenciais SNMP
ips = ['10.44.74.37', '10.44.74.28', '10.44.74.26', '10.44.74.30', '10.44.74.32', '10.44.74.38', '10.44.74.45']
comunidade = 'public'

# Define o OID para o contador de páginas
oid_monocromatica = '1.3.6.1.2.1.43.10.2.1.4.1.1'

# Obtém a data e hora atual
data_atual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Define o nome do arquivo de texto
nome_arquivo = f'resultado_{data_atual}.txt'

# Abre o arquivo de texto para escrita
arquivo = open(nome_arquivo, "w")

# Loop através dos endereços IP e obter o número de páginas impressas de cada impressora
for ip in ips:
    # Cria uma sessão SNMP com a impressora para o contador de páginas
    iterator = getCmd(SnmpEngine(),
                      CommunityData(comunidade),
                      UdpTransportTarget((ip, 161)),
                      ContextData(),
                      ObjectType(ObjectIdentity(oid_monocromatica)))

    # Obtém o valor do contador de páginas
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
    if errorIndication:
        resultado = f'Impressora {ip}: Erro ao obter o contador de páginas: {errorIndication}'
    else:
        for varBind in varBinds:
            resultado = f'Impressora {ip}: Número de páginas impressas: {varBind[1]}'

    # Escreve o resultado no arquivo de texto
    arquivo.write(resultado + '\n')

# Fecha o arquivo de texto
arquivo.close()
