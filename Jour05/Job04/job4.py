
def tapis (n):
    print("+"+(n)*"-"+"+")
    
    y=1
    for i in range(n):
        y=y+1
        print("|"+(n-i-1)*"#"+" "+(i)*"#"+"|") 


    print("+"+(n)*"-"+"+")

tapis(10)