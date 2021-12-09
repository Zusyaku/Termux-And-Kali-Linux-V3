import sys

serial = []
with open(".add_account/serial_no") as file:
    for line in file: 
        line = line.strip()
        serial.append(line)

serial.pop()

for i in range(len(serial)):
 print serial[i]
