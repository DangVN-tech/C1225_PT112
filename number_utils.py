def is_even(n):
    n%2==0
    print("True")
    return
def is_odd(n):
    n%2!=0
    print("True")
    return
def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            print("Khong la so nguyen ")
            break
    else:
        print("Day la so nguyen to")