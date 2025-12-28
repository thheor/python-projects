import mysql.connector

def connectDB():
    try:
        cnx = mysql.connector.connect(
            user= 'root',
            password= '',
            host= '127.0.0.1',
            database= 'todo'
        )
        print('connection success')
    
    except mysql.connector.Error as err:
        print(err)

    return cnx

def getData(cursor, id):
    cursor.execute(f'SELECT item FROM list WHERE user_id = {id}')

    data = []
    for fields in cursor:
        print(f'{cursor.rowcount}. {fields[0]}')
        data.append(fields[0])
    
    return data

def login(cursor):
    print('---LOGIN---')
    while True:
        username = str(input('Username: '))

        cursor.execute(f'SELECT id FROM user WHERE name = \'{username}\'')
        rows = cursor.fetchall()
        if(not rows):
            print('there is no matching username')
        else:
            for row in rows[0]:
                id = row
                print(f'Your id: {id}')

            return id

if __name__ == '__main__':
    cnx = connectDB()
    cursor = cnx.cursor()

    id = login(cursor)

    while True:
        print('---TODO APP---')
        print('1. Add List')
        print('2. Read List')
        print('3. Update List')
        print('4. Delete List')
        print('5. Exit')
        choice = int(input('Enter your choice: '))

        match choice:
            case 1:
                print('---ADD LIST---')
                while True:
                    item = str(input('Enter new list: '))
                    cursor.execute(f'INSERT INTO list (item, user_id) VALUES (\'{item}\', {id})')
                    cnx.commit()
                    repeat = input('Add new list again? \n[Y/n]: ')
                    if repeat == 'n' or repeat == 'N':
                        break

            case 2:
                print('---READ LIST---')
                getData(cursor, id)
                gotoMenu = input('Go back to Main Menu?\n[Y/n]: ')
                if gotoMenu == 'n' or gotoMenu == 'N':
                    break
            case 3:
                print('---UPDATE LIST---')
                while True:
                    data = getData(cursor, id)
                    numList = int(input('Enter list\'s number do you want to update: '))
                    updateList = input('Enter update list: ')

                    cursor.execute(f'UPDATE list SET item = \'{updateList}\' WHERE user_id = {id} AND item = \'{data[numList - 1]}\'')
                    cnx.commit()

                    gotoMenu = input('Go back to Main Menu?\n[Y/n]: ')
                    if gotoMenu == 'Y' or gotoMenu == 'y':
                        break
            case 4:
                print('---DELETE LIST---')
                data = getData(cursor, id)
                numList = int(input('Enter list\'s number do you want to delete: '))
                try:
                    cursor.execute(f'DELETE FROM list WHERE item = \'{data[numList - 1]}\' and user_id = {id}')
                    print('Delete record successfull')
                except mysql.connector.Error as err:
                    print(f'Delete record ERROR: {err}')
            case 5:
                print('Bye')
                break
            case _:
                print('Invalid Input!')
    
    cursor.close()
    cnx.close()