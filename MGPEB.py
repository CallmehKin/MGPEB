modulos = [
    {"nome": "M1", "combustivel": 30, "prioridade": 3},
    {"nome": "M2", "combustivel": 80, "prioridade": 3},
    {"nome": "M3", "combustivel": 50, "prioridade": 2},
    {"nome": "M4", "combustivel": 20, "prioridade": 3}
]

pousados = []
alerta = []

clima_ok = True

def verificar_pouso(modulo):
    if modulo["combustivel"] > 25 and clima_ok:
        return True
    else:
        return False

modulos.sort(key=lambda x: x["prioridade"], reverse=True)

for modulo in modulos:
    if verificar_pouso(modulo):
        print(modulo["nome"], "POUSO AUTORIZADO")
        pousados.append(modulo)
    else:
        print(modulo["nome"], "DECOLAGEM ABORTADA")
        alerta.append(modulo)
