"""
Funções de selecionar o valor valido
"""
def get_int_op(msg, min, max):
    while True:
        try:
            value = int(input(msg))
            if value < min or value > max:
                print(f"Selecione um item válido ({min}-{max})")
                continue
            return value
        except:
            print("Valor inválido")


#exibe as funcionalidades da lista de itens --> o main que estiver dentro da lista
def mostrar_menu(items:list):
    mensagem = "Funcionalidades"
    print(f"\n{"-"* 10}{mensagem}{"-"* 10}")
    for i, item in enumerate(items):
        print (f"{i+1}. {item}")
