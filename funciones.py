def OnOf(parametros, calefacciones, OnOf, err):
    connect = True
    print(parametros)
    i = 0
    s = ''
    if parametros == ['']:
        connect = onOfAllElements(OnOf, calefacciones, connect, i)
    else:
        while i < len(calefacciones) and connect == True:
            for parametro in parametros:
                if parametro[0:].isdigit():
                    if parametro == calefacciones[i].id:
                        calefacciones[i].status = OnOf
                        connect=calefacciones[i].connect()
                else:
                    s = "-4"
            i = i + 1
    if not connect:
        s = err
    for calefaccion in calefacciones:
        print(calefaccion.status)
    return s


def onOfAllElements(OnOf, calefacciones, connect, i):
    while i < len(calefacciones) and connect:
        connect = calefacciones[i].connect()
        calefacciones[i].status = OnOf
        i = i + 1
    return connect