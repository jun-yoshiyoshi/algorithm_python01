# 後判定
def euclid_cal1(a, b):
    if b > a:
        a, b = b, a

    r = a % b

    while r != 0:
        a, b = b, r
        r = a % b

    if r == 0:
        print(f"最大公約数は{b}")


euclid_cal1(120, 1050)

# 前判定＋後判定


def euclid_cal2(a, b):
    r = 0
    if b > a:
        a, b = b, a

    r = a % b
    if r == 0:
        print(f"最大公約数は{b}")

    else:
        while r != 0:
            a, b = b, r
            r = a % b

    if r == 0:
        print(f"最大公約数は{b}")


euclid_cal2(1050, 120)
