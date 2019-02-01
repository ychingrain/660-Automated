# Please modify the following program to now convert from input Fahrenheit
# to Celsius

def doConversion():
    tempInFAsString = input('Enter the temperature in Fahrenheit: ')
    tempInF = int( tempInFAsString )
    tempInC = round(((tempInF - 32) * 5/9),1)
    print("The temperature in Celsius is %f degrees." %(tempInC))

yesplease = 1
response = ""
while yesplease:
    doConversion()
    response = raw_input('Do you want to convert another temperature (y/n)? ')
#    print("Response = %s" % format(response))
    while response != "y" and response != "n": 
        response = raw_input('Do you want to convert another temperature (y/n)?')
    if response == "y":
        yesplease = 1
    else:
        print("Bye!")
        yesplease = 0



