import time

for i in range(1, 11):
	if i % 2 != 0:
		print(i, end="")

print("\n")

for i in range(1, 11, 2):
	print(i, end="")

print("\n")

x = 1
while x <11:
	if x % 2 != 0:
		print(x, end="")
	x += 1
print("\n")

#Can make a countdown with the for loop:
for i in range(3, 0, -1):
	if i >= 1:
		print(f"Rebooting in {i} seconds")
		time.sleep(0.5)
		continue

print("Rebooting now...")
time.sleep(1)

print("\n")

for ch in "john.smith@pythoninstitute.org":
	if ch == "@":
		break
	else: print(ch, end="")

print("\n")

print("Updating the system. Prepare thy anus, the breach is imminent!")

spinner = ["|", "/", "-", "\\"]

count = 0
while count < 20:

	frame = spinner[count % 4]

	print(f"\rLoading... {frame}", end="")

	time.sleep(0.15)
	count += 1

print("\rDone muthafoxxa! Now get back to werk!")
print("\n")

for digit in "0165031806510":
	if digit == "0":
		print("x", end="")
		continue
	print(digit, end="")

print("\n")

n = 3

while n >0:
	print(n + 1, end="")
	n -= 1
else:
	print(n, end="")

print("\n")

