# https://www.acmicpc.net/problem/9506

while True:
    try:
        n = int(input())

        if n == -1:
            break

        divisors = []

        for i in range(1, n):
            if n % i == 0:
                divisors.append(i)

        if sum(divisors) == n:
            print(f"{n} = ", end="")

            for i in range(len(divisors)):
                print(f"{divisors[i]}", end="")

                if i != len(divisors) - 1:
                    print(" + ", end="")

            print()

        else:
            print(f"{n} is NOT perfect.")

    except:
        break
