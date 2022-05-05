def save(b1: int, b2: int, b3: int, b4: int, a1: int, a2: int, a3: int, a4: int,
         lvl: int, lvle: int, exp: int, tk: int, p: int, sp: int, cc: int, ac: int):
    saves = [b1, b2, b3, b4, a1, a2, a3, a4, lvl, lvle, exp, tk, p, sp, cc, ac]
    file = open("save.txt", "w")
    for i in saves:
        file.write(str(i) + ' ')
    file.close()


def load():
    file = open("save.txt", "r")
    saves = file.read().split()
    for i in range(len(saves)):
        saves[i] = int(saves[i])
    file.close()
    return saves
