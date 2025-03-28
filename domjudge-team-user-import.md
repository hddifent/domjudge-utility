# Importing teams and users data in DOMjudge using files

This documentation was written using information on [DOMjudge's manual for version 9.0.0DEV on "Adding contest data in bulk"](https://www.domjudge.org/docs/manual/main/import.html).

**Important**: Create a team category beforehand as it is used in team setup.

Importing teams uses a `.json` file while importing users uses a `.yaml` file. (Dunno why.)

Do not use `.tsv` files as they are outdated, might not be supported in later versions, and generally more confusing.

## File formats

### Teams

`teams.json` consists of an array of teams with following fields:

- `id`: The team ID. Must be unique.
- `group_ids`: An array with one element: the category ID this team belongs to.
- `name`: The team name used in web interface.
- `members` (optional): Team's public descriptions.
- `display_name` (optional): The team display name. If provided, will display this instead of the team name in certain places, like the scoreboard.
- `organization_id`: The ID of the team affiliation this team belongs to. Leave empty for no affilation.

Example:

```json
[{
  "id": "1",
  "group_ids": ["7"],
  "name": "John Smith",
  "organization_id": ""
}, {
  "id": "2",
  "group_ids": ["7"],
  "name": "Jane Doe",
  "organization_id": ""
}, {
  .
  .
  .
}, {
  "id": "30",
  "group_ids": ["7"],
  "name": "Bin Benbose",
  "organization_id": ""
}]
```

### Users (Accounts)

`accounts.yaml` consists of an array of accounts with the following fields:

- `id`: The account ID. Must be unique.
- `username`: The account username. Must be unique.
- `password`: The password to use for the account.
- `type`: the user type (`team`, `judge`, `admin` or `balloon`. `jury` will be interpret as `judge`.)
- `team_id`: (optional) The ID of the team this account belongs to.
- `name`: (optional) The full name of the account.
- `ip` (optional): IP address to link to this account.

Example:

```yaml
- id: team001
  username: team001
  password: ABCabc123xyz
  type: team
  team_id: 1
  name: John Smith

- id: team002
  username: team002
  password: verystrongpassword
  type: team
  team_id: 2
  name: Jane Doe

  .
  .
  .
```

## Importing data into DOMjudge

**You should import teams before users.**

1. On the Administrator panel, press *Import / export*.
2. Navigate to *Teams & groups* section. Import the data under *Import JSON / YAML* box.
   - For teams, select `teams` under the type dropdown and browse for `teams.json` file.
   - For users/accounts, select `accounts` under the type dropdown and browse for `accounts.yaml` file.