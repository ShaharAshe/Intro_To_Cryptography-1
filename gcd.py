def gcd(num_1:int, num_2:int)->int:
    if num_1 == 0:
        return 0
    return num_1 if num_2 == 0 else gcd(num_2, num_1%num_2)


if __name__ == "__main__":
    while True:
        num_1 = input("Enter the first number (or exit): ")
        if num_1 == "exit":
            break
        num_2 = input("Enter the second number (or exit): ")
        if num_2 == "exit":
            break
        print(gcd(int(num_1), int(num_2)))