# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


from random import randint

p = "papier"
k = "kamien"
n = "nozyce"

hand = [p, k, n];
winning = [[p, k], [k, n], [n, p]];

for z in range(3):
    gamer = input("podaj swój wybór (papier, kamien, nozyce):");
    print("twój wybór:"+ gamer);


    i = randint(0, 2);
    pc = hand[i];

    res = [gamer,pc]

    print("wybór komputera:" + pc)
    if pc == gamer:
        print("remis")
    elif res in winning:
        print("wygrana")
    else:
        print("przegrana")
