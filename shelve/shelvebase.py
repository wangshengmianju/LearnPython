#shelvebase.py
'''
store person's name,age and phone numbers in simple db with 'shelve' module
'''
import sys, shelve
    
def store_person(db):
    '''
    input data, and store them in shelve object
    '''
    pid = input('Enter unique ID number: ')
    person = {}
    person['name'] = input('Enter name: ')
    person['age'] = input('Enter age: ')
    person['phone'] = input('Enter phone: ')
    db[pid] = person 

def lookup_person(db):
    ''' 
    input ID and key to get info
    '''
    pid = input('Enter ID number: ')
    field = input('What would you like to know? (name, age, phone)')
    field = field.strip().lower()
    print(field.capitalize() + ': ' + db[pid][field])

def delete_person():
    pass

def print_help():
    print('The available commands are:')
    print('"store": Stores information about a person')
    print('"lookup": Looks up a person from ID number or name')
    print('"delete": delete a person from ID number or name ')
    print('"quit": Save changes and exit')
    print('" ? ": Prints this message')

def enter_command():
    ''' 
    prepare the income command
    '''
    cmd = input('Enter command(? for help): ')
    cmd = cmd.strip().lower()
    return cmd

def main():
    shelvebase = shelve.open('SFbase')      #open file and load the shelvebase
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_person(shelvebase)
            elif cmd == 'lookup':
                lookup_person(shelvebase)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
    finally:
        print('The shelvebase is closed.')
        shelvebase.close()

if __name__ == '__main__': main()



