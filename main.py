# Snowed-in-or-school-open
#function that will determine whether a school is closed based on the weather and temperature
#Returns True if temperature is below freezing or if weather is snowy, otherwise returns false

def snowed_in(temperature, weather, is_celcius = True):
    if (weather == "snowy"):
        return True
    elif (is_celcius == True) and (temperature <=0): #freezing temperature is below or equal to 0 if scale is celcius
        return False
    elif (is_celcius == True) and (temperature >0):
        return False
    elif (is_celcius == "False") and (temperature <=32): #freezing temperature is below or equal to 32 if scale is farenheit
        return True
    else:
        return False
    
         

temperature_1 = int(input("enter temperature: "))
weather_1 = input("enter either 'sunny' or 'snowy': ")
is_celcius_1 = input("Is degree(s) in celcius? Enter 'False' or 'True': ")


results = snowed_in(temperature_1, weather_1, is_celcius_1)
if results == True:
    print("snowed in!")
else:
    print("school open!")

