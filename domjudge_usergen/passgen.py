import random
import sys

override_defaults = False

if len(sys.argv) == 2 or len(sys.argv) == 3:
    override_defaults = True
elif len(sys.argv) != 1:
    print("Invalid amount of argument")
    exit(1)

chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"

pass_amt = int(sys.argv[1]) if override_defaults else 100
pass_len = int(sys.argv[2]) if override_defaults and len(sys.argv) == 3 else 12

filename = "pass.txt"

pass_out_file = open(filename, "w")

for i in range(pass_amt):
    choosing = [chars[i] for i in random.sample(population=range(len(chars)), k=pass_len)]
    pass_out_file.write(f"{'\n' if i != 0 else ''}{''.join(choosing)}")

pass_out_file.close()