#UNIT CALCULATOR

#Conversion dictionary
units = {       
            'Area':                   {
                                        'sqkm'   : 0.001,
                                        'sqm'    : 1,
                                        'sqmile' : 1000,
                                        'sqyard' : 1000000,
                                        'sqfoot' : 1000000000,
                                        'sqinch' : 8,
                                        'ha'     : 8000,
                                        'ac'     : 8000000,
                                      },
            'Digital transfer rate':  {
                                        'bit/s'  : 0.001,
                                        'kbit/s' : 1,
                                        'mbit/s' : 1000,
                                        'gbit/s' : 1000000,
                                        'tbit/s' : 1000000000,
                                        'kb/s'   : 8,
                                        'mb/s'   : 8000,
                                        'gb/s'   : 8000000,
                                        'tb/s'   : 8000000000
                                     },
            'Digital storage':       {
                                       'bit'    : 0.125,
                                       'kbit'   : 125,
                                       'mbit'   : 125000,
                                       'gbit'   : 125000000,
                                       'tbit'   : 125000000000,
                                       'byte'   : 1,
                                       'kbyte'  : 1000,
                                       'mbyte'  : 1000000,
                                       'gbyte'  : 1000000000,
                                       'tbyte'  : 1000000000000
                                     },
            'Energy':                {
                                       'j'     : 0.001,
                                       'kj'    : 1,
                                       'gcal'  : 0.004184,
                                       'kcal'  : 4.184,
                                       'wh'    : 3.6,
                                       'kwh'   : 3600,
                                     },
            'Frequency':             {
                                       'khz'   : 1000,
                                       'hz'    : 1,
                                       'mhz'   : 0.000001,
                                       'ghz'   : 0.000000001
                                     },
            'Length':                {
                                       'km'    : 1000,
                                       'm'     : 1,
                                       'cm'    : 0.01,
                                       'mm'    : 0.001,
                                       'μ'     : 0.000001,
                                       'n'     : 0.000000001,
                                       'mile'  : 1609.34,
                                       'yard'  : 0.9144,
                                       'foot'  : 0.3048
                                     },
            'Mass':                  {
                                       'tonne' : 1,
                                       'kg'    : 1,
                                       'g'     : 0.001,
                                       'mg'    : 0.000001,
                                       'stone' : 6.35029,
                                       'lb'    : 0.453592,
                                       'ounce' : 0.0283495
                                     },
            'Pressure':              {
                                       'bar'   : 100000,
                                       'pa'    : 1,
                                       'atm'   : 101325,
                                       'torr'  : 133.322
                                     },   
            'Speed':                 {
                                       'mph'   : 0.44704,
                                       'ft/s'  : 0.3048,
                                       'm/s'   : 1,
                                       'km/h'  : 0.277778,
                                       'knot'  : 0.514444855556
                                     },
            'Time':                  {
                                       'ns'    : 0.0000016667,
                                       'μs'    : 0.00016667,
                                       'ms'    : 0.16667,
                                       's'     : 0.0166667,
                                       'm'     : 1,
                                       'hr'    : 60,
                                       'day'   : 1440,
                                       'week'  : 10080,
                                       'month' : 43800,
                                       'year'  : 525599.42184,                                                
                                     },
            'Volume':                {
                                       'gallon': 3.78541,
                                       'quart' : 0.946353,
                                       'pint'  : 0.473176,
                                       'cup'   : 0.24,
                                       'ounce' : 0.0295735,
                                       'tbsp'  : 0.0147868,
                                       'tsp'   : 0.00492892,
                                       'l'     : 1,
                                       'ml'    : 0.001,
                                     },
         }

#Unit Converting Function
def converter(category, unit_from, unit_to, value):
    u_from    =units[category][unit_from]
    u_to      =units[category][unit_to]
    new_value =value*(u_from/u_to) 
    return str(new_value)


#Main
print ("UNIT CONVERTER")
print("-----------------------------------\n")
print("Categories:")
print("-----------------------------------")
print("\n".join(units.keys()))
while (1):
    category=input("\nPlease select a unit category from the list:\n").capitalize()
    if category not in units.keys():
        print("Invalid input")       
    else:
        print("\nUnits of "+ category)
        print("-----------------------------------")
        print("\n".join(units[category].keys()))
        while (1):
            unit_from=input("Which unit would you like to convert from?\n").lower()
            if  unit_from not in units[category].keys():
                print("Invalid input")
            else:
                while (1):
                    unit_to=input("Which unit would you like to convert to?\n").lower()
                    if unit_to not in units[category].keys():
                        print("Invalid input")
                    else:
                        while (1):
                            value=input("Enter your value:\n")
                            try:
                                val = int(value) 
                                print("\nConverted Value: " +converter(category, unit_from, unit_to, val)+ " " +unit_to)
                                print("-----------------------------------")
                                break
                            except ValueError:
                                print("Invalid Input")
                        break
                break
        break
        
        
        
       
        
        







