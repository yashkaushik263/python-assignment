from temperature.celsius import c_to_f, c_to_k
from temperature.fahrenheit import f_to_c
from temperature.kelvin import k_to_c

def main():
    print("Temperature conversion options")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to celsius")
    print("3. Celsius to kelvin")

    choice = int(input("Enter your choice (1/2/3):"))

    if choice == 1:
        celsius = float(input("Enter temperature in celsius"))
        print(f"{celsius} C = {c_to_f(celsius)}")

    elif choice == 2:
        fahrenheit = float(input("Enter temperature is Fahreneit"))
        print(f"{fahrenheit}F = {f_to_c (fahrenheit)} C")

    elif choice == 3:
        celsius = float(input("Enter the temperature in celsius"))
        print(f"{celsius} C = {c_to_k(celsius)} k")

    else:
        print("Invalid choice")

main()