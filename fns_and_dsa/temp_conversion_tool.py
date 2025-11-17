
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    tempreture = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return tempreture

def convert_to_fahrenheit(celsius):
    tempreture = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return tempreture

def main():
    tempreture_to_convert = int(input("Enter the temperature to convert: "))
    type_of_tempreture = input("Is this temperature in Celsius or Fahrenheit? (C/F):")

    if type_of_tempreture.lower() == 'c':
        tempreture = convert_to_fahrenheit(tempreture_to_convert)
        tempreture = f'{tempreture_to_convert} is {tempreture}F'

    elif type_of_tempreture.lower() == 'f':
        tempreture = convert_to_celsius(tempreture_to_convert)
        tempreture = f'{tempreture_to_convert} is {tempreture}C'
    else:
        tempreture = 'Invalid temperature. Please enter a numeric value.'
    
    print(tempreture)



if __name__ == "__main__":
    main()