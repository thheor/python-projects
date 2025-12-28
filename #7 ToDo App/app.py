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

def getListID(cursor, id):
    cursor.execute(f'SELECT id, item FROM list WHERE user_id = {id}')

    data = []
    for fields in cursor:
        print(f'{cursor.rowcount}. {fields[1]}')
        data.append(fields[0])
    
    return data

def login(cnx, cursor):
    print('---LOGIN---')
    while True:
        username = str(input('Username: '))

        cursor.execute(f'SELECT id FROM user WHERE name = \'{username}\'')
        rows = cursor.fetchall()
        if(not rows):
            print('there is no matching username')
            wantsReg = input('Do you want to register?\n[Y/n]: ')
            if wantsReg == 'Y' or wantsReg == 'y':
                register(cnx, cursor)
        else:
            for row in rows[0]:
                id = row

            return id

def register(cnx, cursor):
    print('---REGISTER---')

    username = str(input('Create username: '))

    try:
        cursor.execute(f'INSERT INTO user (name) VALUES (\'{username}\')')
        print('Register successfully!')
        cnx.commit()
        login(cnx, cursor)
    except mysql.connector.Error as err:
        print(f'Ups there is an error: {err}')
        exit()

if __name__ == '__main__':
    cnx = connectDB()
    cursor = cnx.cursor()

    id = login(cnx, cursor)
    print(f'your id is {id}')

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
                getListID(cursor, id)
                gotoMenu = input('Go back to Main Menu?\n[Y/n]: ')
                if gotoMenu == 'n' or gotoMenu == 'N':
                    break
            case 3:
                print('---UPDATE LIST---')
                while True:
                    listId = getListID(cursor, id)
                    numList = int(input('Enter list\'s number do you want to update: '))
                    updateList = input('Enter update list: ')

                    cursor.execute(f'UPDATE list SET item = \'{updateList}\' WHERE id = {listId[numList - 1]}')
                    cnx.commit()

                    gotoMenu = input('Go back to Main Menu?\n[Y/n]: ')
                    if gotoMenu == 'Y' or gotoMenu == 'y':
                        break
            case 4:
                print('---DELETE LIST---')
                listId = getListID(cursor, id)
                numList = int(input('Enter list\'s number do you want to delete: '))
                try:
                    cursor.execute(f'DELETE FROM list WHERE id = {listId[numList - 1]}')
                    print('Delete record successfull')
                    cnx.commit()
                except mysql.connector.Error as err:
                    print(f'Delete record ERROR: {err}')
            case 5:
                print('Bye')
                break
            case _:
                print('Invalid Input!')
    
    cursor.close()
    cnx.close()