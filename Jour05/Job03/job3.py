height=5
print(" "*(5)+"/"+"\\")
y=1
for i in range (height-2):
    y=y+1
    print(" "*(5-i-1)+ "/"+(y+i)*" "+"\\")

print(" "+"/"+(5+i+1)*"_"+"\\")