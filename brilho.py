def aumentar():
    import wmi, time
    geral = wmi.WMI(namespace='wmi')
    funções = geral.WmiMonitorBrightnessMethods()[0]
    for _ in range(0, 100+1, 20):
        funções.WmiSetBrightness(_, 0)
        time.sleep(.1)

def diminuir():
    import wmi, time
    geral = wmi.WMI(namespace='wmi')
    funções = geral.WmiMonitorBrightnessMethods()[0]
    for _ in range(100, -1, -20):
        funções.WmiSetBrightness(_, 0)
        time.sleep(.1)