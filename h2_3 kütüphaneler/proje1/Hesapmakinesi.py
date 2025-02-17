1

def topla(x, y):
    return x + y


def cikar(x, y):
    return x - y


def carp(x, y):
    return x * y


def bol(x, y):
    return x / y


print("Select operation.")
print("1.topla")
print("2.cıkarma")
print("3.carp")
print("4.bol")

while True:
    
    secim = input("secim girin(1topla/2cikar/3carp/4bol): ")

    
    if secim in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if secim == '1':
            print(num1, "+", num2, "=", topla(num1, num2))

        elif secim == '2':
            print(num1, "-", num2, "=", cikar(num1, num2))

        elif secim == '3':
            print(num1, "*", num2, "=", carp(num1, num2))

        elif secim == '4':
            print(num1, "/", num2, "=", bol(num1, num2))

        next_calculation = input("yeni islem ? (evet/hayır):")
        if next_calculation == "hayır":
          break
    else:
        print("Invalid Input")