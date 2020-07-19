import getpass

dataDict = {
    'Admin': 'pass',
    'User': 'q123'
}

try:
    checkUser = input('Enter your login: ')
    checkPass = getpass.getpass('Enter your password: ')

    if dataDict[checkUser] == checkPass:
        print('Access Granted')
    else:
        print('Error Pass')

except KeyError:
    print('Keksik')
