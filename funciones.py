def OnOf(parametros, calefacciones, OnOf, err):
    ids = []
    for calefaccion in calefacciones:
        ids.append(calefaccion.id)
    connect = True
    i = 0
    s = ''
    if parametros == ['']:
        connect = onOfAllElements(OnOf, calefacciones, connect, i)
    else:
        while i < len(calefacciones) and connect == True:
            for parametro in parametros:
                if parametro[0:].isdigit() and checkId(parametro,ids):
                    if parametro == calefacciones[i].id:
                        calefacciones[i].status = OnOf
                        connect=calefacciones[i].connect()
                else:
                    s = "-4"
            i = i + 1
    if not connect or s=="-4":
        s = err
    else:
        s="+"
    return s


def onOfAllElements(OnOf, calefacciones, connect, i):
    while i < len(calefacciones) and connect:
        connect = calefacciones[i].connect()
        calefacciones[i].status = OnOf
        i = i + 1
    return connect

def checkId(id,calIds):
    if id in calIds:
        return True
    else:
        return False