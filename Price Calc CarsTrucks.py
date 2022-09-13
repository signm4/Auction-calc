while 1 == 1:
    x = input("How much is the price? $")
    y = int(x)
    sales = y*.0625
    num = y + sales + 33 + 5 + 60 + 69 + 15
    z = 0
    if y >= 900 and y <= 1099:
        z = num + 155
    elif y >= 1100 and y <= 1299:
        z = num + 165
    elif y >= 1300 and y <= 1499:
        z = num + 175
    elif y >= 1500 and y <= 1699:
        z = num + 185
    elif y >= 1700 and y <= 1899:
        z = num + 205
    elif y >= 1900 and y <= 2099:
        z = num + 225
    elif y >= 2100 and y <= 2299:
        z = num + 235
    elif y >= 2300 and y <= 2499:
        z = num + 245
    elif y >= 2500 and y <= 2699:
        z = num + 255
    elif y >= 2700 and y <= 2899:
        z = num + 265
    elif y >= 2900 and y <= 3099:
        z = num + 275
    elif y >= 3100 and y <= 3299:
        z = num + 285
    elif y >= 3300 and y <= 3499:
        z = num + 295
    elif y >= 3500 and y <= 3699:
        z = num + 310
    elif y >= 3700 and y <= 3899:
        z = num + 320
    elif y >= 3900 and y <= 4099:
        z = num + 330
    elif y >= 4100 and y <= 4299:
        z = num + 340
    elif y >= 4300 and y <= 4499:
        z = num + 350
    elif y >= 4500 and y <= 4799:
        z = num + 360
    elif y >= 4800 and y <= 4999:
        z = num + 370
    elif y >= 5000 and y <= 5499:
        z = num + y*.08
    elif y >= 5500 and y <= 7999:
        z = num + y*.09
    elif y >= 8000:
        z = num + y*.1
    print("this is your Price...$", z, " ")
    print("this is your Price with deposit...$", z-300, " ")
