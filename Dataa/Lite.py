import sqlite3
db = sqlite3.connect("app.db")
cr = db.cursor()

def commint_and_close():
    db.commit()
    db.close()
    print("Connection To Database IS Closed")


uid = 1

input_message = """
What Do You Want T o DO ?
"s" => Show All Skills
"a" => Add New Skills
"d" => Delete A Skills
"u" => Update Skills Progress
"q" => Quit The App
Choose Option: 
"""
user_input = input(input_message).strip().lower()
cammands_list = ["s", "a", "d", "u", "q"]

def show_skills():
    print('Show Skills')
    commint_and_close()

def add_skills():
    sk = input("Write Skill Name: ").strip().capitalize()
    prog = input("Write Skill Progress: ").strip()
    cr.execute(f"insert into skills(name, progress, user_id) values('{sk}', '{prog}', '{uid}')")
    commint_and_close()
 
def delete_skills():
    sk = input("Write Skill Name: ").strip().capitalize()
    cr.execute(f"delete from skills where name = {sk} ")
    commint_and_close()

def update_skills():
    print('Update Skill')
    commint_and_close()

if user_input in cammands_list:
    print(f'Command Found {user_input}')
    if user_input == "s":
        show_skills()

    elif user_input == "a":
        add_skills()

    elif user_input == "d":
        delete_skills()

    elif user_input == "u":
        update_skills()
    else:
        print("App Is Closed")
else:
    print(f'Sorry This Command {user_input} Is Not Found')
