import sys

override_defaults = False

if len(sys.argv) == 4:
    override_defaults = True
elif len(sys.argv) != 1:
    print("Invalid amount of argument")
    exit(1)

# ---------- SETUP ---------

team_out_file = open("teams.json", "w", encoding="utf8")
acc_out_file = open("accounts.yaml", "w", encoding="utf8")

full_name_file = open("users.txt", "r", encoding="utf8")
pass_file = open("pass.txt", "r", encoding="utf8")

user_prefix = sys.argv[1] if override_defaults else "user" # Change if neccessary

fname = full_name_file.readlines()
plist = pass_file.readlines()

full_name_file.close()
pass_file.close()

team_offset = int(sys.argv[2]) if override_defaults else 0 # Offset to not collide with existing teams

# ---------- TEAMS ----------
team_out_file.write("[")
for i, v in enumerate(fname):
    team_out_file.write("{\n" if i == 0 else ", {\n")
    team_out_file.write(f'  "id": "{team_offset + i}",\n')
    team_out_file.write(f'  "group_ids": ["{int(sys.argv[3]) if override_defaults else 7}"],\n') # Defaults to 7
    team_out_file.write(f'  "name": "{v.strip()}",\n')
    team_out_file.write(f'  "organization_id": ""\n')
    team_out_file.write("}")

team_out_file.write("]")
team_out_file.close()

# ---------- ACCOUNTS ----------
for i, v in enumerate(fname):
    acc_out_file.write(f"""- id: {user_prefix}{i + 1:02d}
  username: {user_prefix}{i + 1:02d}
  password: {plist[i].strip()}
  type: team
  team_id: {team_offset + i}
  name: {fname[i].strip()}\n\n""")
acc_out_file.close()