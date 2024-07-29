def set_mini(a):
    b = min(a)
    for i in a:
        if i < b:
            b = i
            return b
            
def set_max(a):
    c = max(a)
    for i in a:
        if i > c:
            c = i
            return c
def main():
    a = [4, 9, 6, 5, 2, 3]
    print("maximum number :",set_max)
    print("minimum number :",set_mini)

    


        



