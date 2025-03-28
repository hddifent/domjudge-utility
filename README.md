# DOMjudge Accounts, Teams, and Problem Archives generation

Contents are split into 2 parts: `domjudge_usergen` and `domjudge_problem`. Scripts are made to be used in the command line.

___

## Accounts and Teams generation

1. Go to *usergen* folder and copy the text file including the team names into the folder, separated by new line characters.
2. Run `domjudge_usergen.sh` with the following options:
  - `-f`: Team names file.
  - `-c` (optional): Team's category ID. (default is `7`)
  - `-l` (optional): Account's password length. (default is `12`)
  - `-p` (optional): Username prefix for used generation. e.g. **user**01, **user**02, **user**03, etc. (default is `user`)
  - `-o` (optional): Team ID offset. This is used to avoid collisions with existing teams on the server. (default is `0`)

Outputs are generated in a folder named `usergen_<date>_<time>`. The contents are as follow:
- `accounts.yaml`: This file can be used to import **account** data into DOMjudge server.
- `teams.json`: This file can be used to import **team** data into DOMjudge server.
- `users.txt`: The copy of team names file. (`-f` argument)
- `pass.txt`: A text file containing each account's password. Each line corresponds to each account.
- `metadata.txt`: Metadata of `domjudge_usergen.sh` execution.

### Example usage

```bash
./domjudge_usergen.sh -f all_user.txt -c 10 -l 12 -p participant_ -o 40
```

___


## Problem Archives generation

1. Go to `problem` folder and copy the problem text (PDF file) into the folder.
2. Run `domjudge_problem.sh` with the following arguments:
  - `<problem_name>`: Full name of the problem. e.g. `Bribery on the Nth Street`
  - `<mem_limit>`: Problem's memory limit. (in MB)
  - `<time_limit>`: Problem's time limit. (in seconds)
  - `<problem_text>`: Problem text file. (PDF only)
  - `<short_name>` (optional): Problem's short name, used to name the output folder. e.g. `Bribery` (default is `problem_date_time`)

The output generates a blank problem archive with **no testcases**. Those have to be added manually. The testcases must be added to the following folders:
- `/data/sample`: Add all testcases used as a sample. *These will be given out to contest participants.*
- `/data/secret`: Add all remaining testcases here. This folder should have the majority of testcases.

Compress the folder into a `.zip` file. The archive can then be uploaded into DOMjudge server.

### Example usage

```bash
./domjudge_problem.sh "Bribery on the Nth Street" 4 1 bribery_text.pdf Bribery
```