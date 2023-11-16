from EX1.wurfel import Wurfel

def main():
    w = Wurfel(6)


    while True:
        
        v = w.werfen()
        print(v)

        if v == 6:
            break



main()
