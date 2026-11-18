def hanoi(n):
    if n== 0:
        return 0
    return 2 * hanoi (n-1) + 1

n = int(input("Enter the number of disks: "))
guess = int(input(f"What will be the total steps for hanoi {n}: "))
print(f"Hanoi({n}) = {hanoi(n)}, your guess: {guess}")

if guess == hanoi(n):
    print("Your guess was correct")
else:
    print("Your guess was wrong")