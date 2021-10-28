# # # This is a sample Python script.
# #
# # # Press Shift+F10 to execute it or replace it with your code.
# # # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# #
# #
# # def print_hi(name):
# #     # Use a breakpoint in the code line below to debug your script.
# #     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# #
# #
# # # Press the green button in the gutter to run the script.
# # if __name__ == '__main__':
# #     print_hi('PyCharm')
# #
# # # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# #
# #
# # from random import randint
# #
# # p = "papier"
# # k = "kamien"
# # n = "nozyce"
# #
# # hand = (p, k, n)
# # winning = ((p, k), (k, n), (n, p))
# # gamerLicznik = 0;
# # PCLicznik = 0;
# # while True:
# #     gamer = input("podaj swój wybór (papier, kamien, nozyce):")
# #     print("twój wybór:" + gamer)
# #     i = randint(0, 2)
# #     pc = hand[i]
# #     res = [gamer, pc]
# #
# #     print("wybór komputera:" + pc)
# #     if pc == gamer:
# #         print("remis")
# #
# #     elif res in winning:
# #         gamerLicznik += 1
# #
# #     else:
# #         print("przegrana")
# #         PCLicznik += 1
# #     print("Gracz", gamerLicznik)
# #     print("Komputer", PCLicznik)
# #     if gamerLicznik == 3 or PCLicznik == 3:
# #         break
# # from random import randint
# #
# # liczby = [4, 20, 6, 9, 9]
# # print(liczby)
# # liczby.extend([randint(0, 10000), randint(0, 10000), randint(0, 10000), randint(0, 10000), randint(0, 10000)])
# #
# # for i in range(6):
# #     print(liczby[-i])
# #
# # liczby[5] = 11
# # print(liczby)
# #
# # liczby.pop()
# # liczby.pop(3)
# # print(liczby)
# #
# # liczby.extend([20, 15, 10])
# # print(liczby)
# # print(len(liczby))
# #
# # for each in range(len(liczby)):
# #     liczby[each] += 100
# # print(liczby)
#
#
#
# rysowanie geometri

# 1.kwadrat
for i in range(3):
    for j in range(6):
        print('#', end = "")
    print()

# 2. prostokąt 1
print()
for i in range(3):
    for j in range(12):
        print('#', end = "")
    print()

# 3. prostokąt 2
print()
for i in range(6):
    for j in range(6):
        print('#', end = "")
    print()

#4. Prostokąt pusty w środku
print()
for i in range(8):
    if i == 0 or i == 7:
        for n in range(15):
            print('#', end= " ")
        print()
    else:
        print('#', end=" ")
        for j in range(13):
            print(" ", end = " ")
        print('#')



# 5. trójkąt 1
print()
n = 1;
for i in range(5):
    for j in range(n):
        print('#', end = "")
    n = n + 1
    print()

# 6. trójkąt 2
print()
n = 5;
for i in range(5):
    for j in range(n):
        print('#', end = "")
    n = n - 1
    print()

# 7. trójkąt 3
print()
n= 5
y=1
for i in range(5):
    for j in range(n):
        print(' ', end = "")
    n = n - 1
    for x in range(y):
        print("#", end = "")
    y = y+2
    print()

# 8. romb
print()
n= 5
y=1
for i in range(5):
    for j in range(n):
        print(' ', end = "")
    n = n - 1
    for x in range(10):
        print("#", end = "")
    print()

# 9. trapez
print()
n= 5
y=10
for i in range(n):
    for j in range(n):
        print(' ', end = "")
    n = n - 1
    for x in range(y):
        print("#", end = "")
    y= y+2
    print()