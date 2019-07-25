#0w0?

choice = input("Would you like to convert your text? (Y/N) ")

if choice.lower() == "y":
    passage = open(input("Enter the location of your text here: "))
    owo = passage.read()

    def owoconvert(text):
        text = text.replace('L', 'W').replace('l', 'w')
        text = text.replace('R', 'W').replace('r', 'w')
        print ('\n' + text)

    owoconvert(owo)

else:
    print ("(´・ω・\`)")
