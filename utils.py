import datetime

def formatar_data_hora():
    # Obtém a data e hora atual formatada
    return datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
