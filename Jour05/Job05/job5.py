import string

message="ou se cache l'ennemie?"
decalage=3
lettre=string.ascii_letters

#conversion message
def msg(y, z):
    conversion= str.maketrans(lettre, lettre[z:] + lettre[:z])
    code= y.translate(conversion)
    return code

print(f"message original: {message}")
code = msg(message, decalage)
print (f"message code: {code}")