import pack1_factorial.factorial
import pack2_exp_root.exponentiation
import pack2_exp_root.root
import pack3_logarithm.logarithm
def main():
    def check(x):
        x1=input(f'Enter {x} - ')
        try :
            x1=float(x1)
            if x1>0:
                return x1
            else:
                print(f'Error. It must be > 0.')
                return check(x)
        except:
            print('Error.')
            return check(x)
    def check2(x):
        x1=input(f'Enter {x} - ')
        try :
            x1=float(x1)
            return x1
        except:
            print('Error.')
            return check2(x)
    print('-'*20)
    ok=False
    while not ok:
        choice=input('Choose funtion :\n1-factorial()\n2-exp2()\n3-exp3()\n4-root2()\n5-root3()\n6-log()\n7-ln()\n8-lg()\nEnter a number - ')
        try:
            choice=int(choice)
            if 0<choice<9:
                ok=True
            else:
                print('Error. Choose number again.')
                print('-'*20)
        except:
            print('Error.Enter again.')
            print('-'*20)
    print('-'*20)
    if choice==1:
        n='a number in order to calculate factorial'
        n=check(n)
        factorial=pack1_factorial.factorial.fact(n)
        print('-'*20)
        print(f'Factorial {n} - ',factorial)
    elif choice==2:
        n='a number in order to square the number'
        n=check2(n)
        e=pack2_exp_root.exponentiation.exp2(n)
        print('-'*20)
        print(f'The square of the entered number {n} - ',e)
    elif choice==3:
        n='a number in order to raise the number to the third power'
        n=check2(n)
        e2=pack2_exp_root.exponentiation.exp3(n)
        print('-'*20)
        print(f'Result - ',e2)
    elif choice==4:
        n='a number in order to find root 2 degree'
        n=check(n)
        r=pack2_exp_root.root.root2(n)
        print('-'*20)
        print(f'Root - ',r)
    elif choice==5:
        n='a number in order to find root 3 degree'
        n=check2(n)
        r2=pack2_exp_root.root.root3(n)
        print('-'*20)
        print(f'Root - ',r2)
    elif choice==6:
        aa='base'
        b='value of logarithm'
        a=check(aa)
        while a==1:
            print('Error. a can not be 1.')
            a=check(aa)
        b=check(b)
        l=pack3_logarithm.logarithm.log(a,b)
        print('-'*20)
        print(f'Logarithm with base {a} and value {b} - ',l)
    elif choice==7:
        b='value of logarithm'
        b=check(b)
        l=pack3_logarithm.logarithm.ln(b)
        print('-'*20)
        print(f'Logarithm with base e and value {b} - ',l)
    elif choice==8:
        b='value of logarithm'
        b=check(b)
        l=pack3_logarithm.logarithm.lg(b)
        print('-'*20)
        print(f'Logarithm with base 10 and value {b} - ',l)
if __name__ == '__main__':
    main()        

