import sys

if len(sys.argv) != 4:
    print(f"Invalid arguments: {sys.argv}")
    exit(1)

yaml = open("problem.yaml", "w", encoding="utf8")
ini = open("domjudge-problem.ini", "w", encoding="utf8")

yaml.write(f"name: '{sys.argv[1].replace("\'", "\'\'")}'\n")
yaml.write("limits:\n")
yaml.write(f"    memory: {sys.argv[2]}\n")
yaml.close()

ini.write(f"timelimit='{sys.argv[3]}'\n")
ini.close()