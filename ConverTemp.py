# Please modify the following program to now convert from input Fahrenheit
# to Celsius

def doConversion():
    tempInFAsString = input('Enter the temperature in Fahrenheit: ')
    tempInF = int( tempInFAsString )
    tempInC = round(((tempInF - 32) * 5/9),1)
    print('The temperature in Celsius is', tempInC, 'degrees')

for conversionCount in range( 3 ):
    doConversion()

