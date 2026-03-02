print("")
print("Site with license:\nhttps://github.com/1j2n3k4m5g7-betaDev/logic-gates-in-python3.13/tree/main")
print("")
print("")

def nand(a:bool,b:bool):
    return not(a and b)
def nor(a:bool,b:bool):
    return not(a or b)
def xor(a:bool,b:bool):
    c = a or b
    d = nand(a,b)
    return c and d
def xnor(a:bool,b:bool):
    return not(xor(a,b))
class logicInt():
    def nand(self,a:int,b:int):
        a=bool(a)
        b=bool(b)
        return int(nand(a,b))
    def nor(self,a:int,b:int):
        a=bool(a)
        b=bool(b)
        return int(nor(a,b))
    def xor(self,a:int,b:int):
        a=bool(a)
        b=bool(b)
        return int(xor(a,b))
    def xnor(self,a:int,b:int):
        a=bool(a)
        b=bool(b)
        return int(xnor(a,b))