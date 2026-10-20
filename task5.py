pin = 768
count=0
while (count>3):
    entered_pin = input("Enter pin: ")
    count +=1
    if(pin == int(entered_pin)):
        print("Success")
        break
if(int(entered_pin) != pin):
    print("Incorrect pin. Try again.")
