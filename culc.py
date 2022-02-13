from tkinter import * #get, Tk, title, geometry, Label, grid, Entry, focus, mainloop
from copy import deepcopy
from math import log
from math import trunc
from matplotlib import pyplot as plt


tusk = None


def clicked():
    global tusk
    tusk = txt.get()

    dict_of_param = dop = {"CO2": [-393.51, 213.6, 37.13],
                           "CaCO3": [-1206, 92.9, 81.85],
                           "CaO": [-635.1, 39.77, 42.83],
                           "FeCO3": [-738.644, 95.5, 83.3],
                           "FeO": [-265.0, 60.79, 49.95],
                           "MnCO3": [-882.247, 109.61, 94.87],
                           "MnO": [-385.35, 61.55, 44.13],
                           "BaCO3": [-1217.1, 112.2, 85.41],
                           "BaO": [-553.9, 70.46, 47.81],
                           "Na2CO3": [-1131.525, 138.889, 111.076],
                           "Na2O": [-418.261, 75.09, 69.149],
                           "CaMg(CO3)2": [-2316.1, 155.29, 157.63],
                           "K2CO3": [-1150.951, 155.623, 114.513],
                           "K2O": [-363.414, 94.203, 83.736],
                           "MgO": [-602.1, 26.96, 37.18],
                           "Ca(OH)2": [-986, 83.44, 87.55],          #delta H must be rewrite and next 3 str
                           "SiO2": [-911.5, 41.87, 44.46],
                           "Ca2SiO4": [-3203, 143, 166.8],
                           "H2O": [-241.9, 188.8, 33.6]
                           }

    left = (tusk.split("=")[0]).split("+")
    right = (tusk.split("=")[1]).split("+")
    d_H_0_298 = 0
    d_S_0_298 = 0
    d_Cp_0_298 = 0
    for i in range(len(right)):
        if dop.get(right[i]):
            d_H_0_298 += (dop.get(right[i])[0])
            d_S_0_298 += (dop.get(right[i])[1])
            d_Cp_0_298 += (dop.get(right[i])[2])
        else:
            if right[i][0].isdigit() and int(right[i][0]) != 0:
                d_H_0_298 += (dop.get(right[i][1:])[0]) * int(right[i][0])
                d_S_0_298 += (dop.get(right[i][1:])[1]) * int(right[i][0])
                d_Cp_0_298 += (dop.get(right[i][1:])[2]) * int(right[i][0])
            elif bool(right[i][3].isdigit()) == False:
                d_H_0_298 += ((dop.get(right[i][3:])[0]) * float(right[i][0:3]))
                d_S_0_298 += ((dop.get(right[i][3:])[1]) * float(right[i][0:3]))
                d_Cp_0_298 += ((dop.get(right[i][3:])[2]) * float(right[i][0:3]))
            elif bool(right[i][4].isdigit()) == True:
                d_H_0_298 += ((dop.get(right[i][3:])[0]) * float(right[i][0:4]))
                d_S_0_298 += ((dop.get(right[i][3:])[1]) * float(right[i][0:4]))
                d_Cp_0_298 += ((dop.get(right[i][3:])[2]) * float(right[i][0:4]))

    for i in range(len(left)):
        if dop.get(left[i]):
            d_H_0_298 -= (dop.get(left[i])[0])
            d_S_0_298 -= (dop.get(left[i])[1])
            d_Cp_0_298 -= (dop.get(left[i])[2])
        else:
            if left[i][0].isdigit() and int(left[i][0]) != 0:
                d_H_0_298 -= (dop.get(left[i][1:])[0]) * int(left[i][0])
                d_S_0_298 -= (dop.get(left[i][1:])[1]) * int(left[i][0])
                d_Cp_0_298 -= (dop.get(left[i][1:])[2]) * int(left[i][0])
            elif bool(left[i][3].isdigit()) == False:
                d_H_0_298 -= ((dop.get(left[i][3:])[0]) * float(left[i][0:3]))
                d_S_0_298 -= ((dop.get(left[i][3:])[1]) * float(left[i][0:3]))
                d_Cp_0_298 -= ((dop.get(left[i][3:])[2]) * float(left[i][0:3]))
            elif bool(left[i][4].isdigit()) == True:
                d_H_0_298 -= ((dop.get(left[i][3:])[0]) * float(left[i][0:4]))
                d_S_0_298 -= ((dop.get(left[i][3:])[1]) * float(left[i][0:4]))
                d_Cp_0_298 -= ((dop.get(left[i][3:])[2]) * float(left[i][0:4]))
    print(d_H_0_298)
    print(d_S_0_298)
    print(d_Cp_0_298)
    d_G_0_298 = (d_H_0_298 * 1000) - (298 * d_S_0_298)
    print(d_G_0_298)
    d_G_n = deepcopy(d_G_0_298)
    list_of_dG = []
    list_of_dT = []
    list_of_dG.append(d_G_n)
    temperature = 300
    t = temperature
    list_of_dT.append(t)
    if d_G_0_298 > 0:
        while d_G_n > 0:
            t += 200
            d_G_n = (d_H_0_298 * 1000) - (t * d_S_0_298) - (d_Cp_0_298 * (t - 298.16)) + (
                    d_Cp_0_298 * t * log(t / 298.16))
            list_of_dG.append(d_G_n)
            list_of_dT.append(t)
        t += 200
        d_G_n = (d_H_0_298 * 1000) - (t * d_S_0_298) - (d_Cp_0_298 * (t - 298.16)) + (
                d_Cp_0_298 * t * log(t / 298.16))
        list_of_dG.append(d_G_n)
        list_of_dT.append(t)
    elif d_G_0_298 < 0:
        while d_G_n < 0:
            t -= 200
            d_G_n = (d_H_0_298 * 1000) - (t * d_S_0_298) - (d_Cp_0_298 * (t - 298.16)) + (d_Cp_0_298 * t * log(t / 298.16))
            list_of_dG.append(d_G_n)
            list_of_dT.append(t)
        t -= 200
        d_G_n = (d_H_0_298 * 1000) - (t * d_S_0_298) - (d_Cp_0_298 * (t - 298.16)) + (d_Cp_0_298 * t * log(t / 298.16))
        list_of_dG.append(d_G_n)
        list_of_dT.append(t)
    print(list_of_dG)

    x1_1, y1_1 = list_of_dT[-3], list_of_dG[-3]
    x1_2, y1_2 = list_of_dT[-1], list_of_dG[-1]
    x2_1, y2_1 = list_of_dT[-3], int(0)
    x2_2, y2_2 = list_of_dT[-1], int(0)
    A1 = y1_1 - y1_2
    B1 = x1_2 - x1_1
    C1 = x1_1 * y1_2 - x1_2 * y1_1
    A2 = y2_1 - y2_2
    B2 = x2_2 - x2_1
    C2 = x2_1 * y2_2 - x2_2 * y2_1
    if B1 * A2 - B2 * A1 != 0:
        y = (C2 * A1 - C1 * A2) / (B1 * A2 - B2 * A1)
        x = (-C1 - B1 * y) / A1
    if B1 * A2 - B2 * A1 == 0: print('Error')
    x_round = trunc(x * 10) / 10
    plt.title("График зависимости изменения энергии Гиббса от температуры")  # заголовок
    plt.xlabel("Температура, К")  # ось абсцисс
    plt.ylabel("Изменение энергии Гиббса, ΔGт, Дж/моль")
    plt.plot(list_of_dT, list_of_dG, 'o-r', alpha=0.7, label="ΔGт(T)", lw=3, mec='b', mew=1, ms=7)
    plt.text(x + 3, y, ('Приблизительно', x_round), color='0.7')

    plt.legend()

    plt.grid(True)

    plt.show()

window = Tk()
window.title("Калькулятор температуры начала самопроизвольного протекания процесса")
window.geometry('660x75')

lbl = Label(window, text="Введите уравнение химической реакции:")
lbl.grid(column=0, row=0)
txt = Entry(window, width=50)
txt.focus()
txt.grid(column=1, row=0)
btn = Button(window, text="Посчитать", command=clicked)
btn.grid(column=2, row=0)

lbl1 = Label(window, text="Например: CaCO3=CaO+CO2")
lbl1.grid(column=1, row=2)

lbl3 = Label(window, text="или CaMg(CO3)2=CaO+MgO")

lbl3.grid(column=1, row=3)

window.mainloop()
