import os
import datetime
from coleta_impressao.monocromatica import coletar_impressao_monocromatica
from coleta_impressao.colorida import coletar_impressao_colorida
from coleta_impressao.toner_preto import verificar_toner_preto
from coleta_impressao.toner_colorido import verificar_toner_colorido
from coleta_impressao.manutencao import verificar_kit_manutencao
#from utils import formatar_data_hora

# Define uma lista de endereços IP da impressora e as credenciais SNMP
ips = ['10.44.74.37', '10.44.74.28', '10.44.74.26', '10.44.74.30', '10.44.74.32', '10.44.74.38', '10.44.74.45']
comunidade = 'public'

# Obtém a data e hora atual
data_atual = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

# Define o nome do arquivo de texto
nome_arquivo = f'resultado_{data_atual}.txt'

# Abre o arquivo de texto para escrita
arquivo = open(nome_arquivo, "w")

# Loop através dos endereços IP e obter as informações de cada impressora
for ip in ips:
    # Coleta informações de impressões monocromáticas
    paginas_monocromaticas = coletar_impressao_monocromatica(ip, comunidade)

    # Coleta informações de impressões coloridas
    paginas_coloridas = coletar_impressao_colorida(ip, comunidade)

    # Verifica a porcentagem do toner preto
    porcentagem_toner_preto = verificar_toner_preto(ip, comunidade)

    # Verifica a porcentagem dos toners coloridos, se a impressora possuir toners coloridos
    porcentagem_toner_colorido = verificar_toner_colorido(ip, comunidade)

    # Verifica a porcentagem do kit de manutenção
    porcentagem_kit_manutencao = verificar_kit_manutencao(ip, comunidade)

    # Escreve as informações no arquivo de texto
    resultado = f'Impressora {ip}: Número de páginas impressas monocromáticas: {paginas_monocromaticas} | Número de páginas impressas coloridas: {paginas_coloridas} | Porcentagem do toner preto: {porcentagem_toner_preto}%'

    if porcentagem_toner_colorido is not None:
        resultado += f' | Porcentagem do toner colorido: {porcentagem_toner_colorido}%'

    resultado += f' | Porcentagem do kit de manutenção: {porcentagem_kit_manutencao}%'

    arquivo.write(resultado + '\n')

# Fecha o arquivo de texto
arquivo.close()

# Renomeia o arquivo para a data atual
os.rename(nome_arquivo, f'resultado_{data_atual}.txt')
