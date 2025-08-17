"""Loops."""

# 1
while (string := input()) != "Три!":
    print("Режим ожидания...")
print("Ёлочка, гори!")

# +
# 2

counter: int = 0
while (string := input()) != "Приехали!":
    if "зайка" in string:
        counter += 1
print(counter)

# +
# 3

start: int = int(input())
end: int = int(input())

for i in range(start, end + 1):
    print(i, end=" ")

# +
# 4

begin: int = int(input())
finish: int = int(input())

step = 1
if finish < begin:
    step = -1
else:
    step = 1

for i in range(begin, end + step, step):
    print(i, end=" ")

# +
# 5

total_price: float = 0

while (price := float(input())) != 0:
    if price >= 500:
        total_price += price - price * 1 / 10
    else:
        total_price += price
print(total_price)

# +
# 6

a_val = int(input())
b_val = int(input())

while b_val:
    a_val, b_val = b_val, a_val % b_val
print(a_val)

# +
# 7

c_val = int(input())
b_val = int(input())

a_orig, b_orig = c_val, b_val

while b_val:
    c_val, b_val = b_val, c_val % b_val

gcd = c_val

lcm: int = int(abs(a_orig * b_orig) / gcd)

print(lcm)

# +
# 8

information: str = input()
times: int = int(input())

for i in range(times):
    print(information)

# +
# 9

number_1: int = int(input())
factorial: int = 1

for i in range(2, number_1 + 1):
    factorial *= i
print(factorial)

# +
# 10

x_val, y_val = 0, 0

while True:
    direction = input()
    if direction == "СТОП":
        break
    steps = int(input())

    if direction == "СЕВЕР":
        y_val += steps
    elif direction == "ЮГ":
        y_val -= steps
    elif direction == "ВОСТОК":
        x_val += steps
    elif direction == "ЗАПАД":
        x_val -= steps

print(y_val, x_val, sep="\n")

# +
# 11

number_2: int = int(input())

total_sum: int = 0
current_number = number_2

while current_number != 0:
    remainder = current_number % 10
    total_sum += remainder
    current_number = current_number // 10

print(total_sum)

# +
# 12

number_3: int = int(input())

current_number = number_3

max_number: int = 0

while current_number != 0:
    remainder = current_number % 10
    max_number = max(max_number, remainder)
    current_number = current_number // 10

print(max_number)

# +
# 13

number_4: int = int(input())
first_gamer: str = input()

for i in range(number_4 - 1):
    name: str = input()
    first_gamer = min(first_gamer, name)
print(first_gamer)

# +
# 14

a1 = int(input())

for i1 in range(1, int(a1**0.5) + 1):
    if i1 != 1 and (a1 % i) == 0:
        print("NO")
        break
else:
    if a1 == 1:
        print("NO")
    else:
        print("YES")
# -

# 15
x1 = int(input())
count = 0
for i2 in range(x1):
    line = input()
    if "зайка" in line:
        count += 1
print(count)

# +
# 16

number_6: int = int(input())

original_number = number_6

output_number: int = 0

while number_6 > 0:
    remainder = number_6 % 10
    output_number = output_number * 10 + remainder
    number_6 //= 10

print("YES" if output_number == original_number else "NO")

# +
# 17

number_7: int = int(input())

result_1: int = 0
multiplier: int = 1

while number_7 > 0:
    digit = number_7 % 10
    if digit % 2 != 0:
        result_1 = result_1 + digit * multiplier
        multiplier *= 10
    number_7 //= 10

print(result_1 if result_1 != 0 else 0)

# +
# 18

number_8 = int(input())

factor = 2
result_2: list[int] = []

while number_8 > 1:
    while number_8 % factor == 0:
        result_2.append(factor)
        number_8 //= factor
    factor += 1

print(*result_2, sep=" * ")

# +
# 19

low, high = 1, 1000
attempts = 0

while attempts < 10:
    guess = (low + high) // 2
    print(guess)
    response = input().strip()

    if response == "Угадал!":
        break
    if response == "Больше":
        low = guess + 1
    elif response == "Меньше":
        high = guess - 1

    attempts += 1

# +
# 20

count = int(input())

prev_hash = 0

for i in range(count):
    b_n = int(input())

    h_n = b_n % 256
    r_n = (b_n // 256) % 256
    m_n = b_n // (256**2)

    correct_hash = (37 * (m_n + r_n + prev_hash)) % 256

    if h_n >= 100 or h_n != correct_hash:
        print(i)
        break

    prev_hash = h_n
else:
    print(-1)
