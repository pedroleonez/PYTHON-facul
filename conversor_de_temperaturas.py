def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def convert_temperature(temp_input):
    temp_value, temp_unit = temp_input.split()
    temp_value = float(temp_value)
    
    if temp_unit.upper() == 'C':
        celsius = temp_value
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
    elif temp_unit.upper() == 'F':
        fahrenheit = temp_value
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
    elif temp_unit.upper() == 'K':
        kelvin = temp_value
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
    else:
        raise ValueError("Unidade de temperatura inválida. Use 'C', 'F' ou 'K'.")
    
    print(f"Temperatura em Celsius: {celsius:.2f} °C")
    print(f"Temperatura em Fahrenheit: {fahrenheit:.2f} °F")
    print(f"Temperatura em Kelvin: {kelvin:.2f} K")

# Exemplo de uso
entrada = input()
convert_temperature(entrada)