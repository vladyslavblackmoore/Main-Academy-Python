from datetime import datetime

with open('/Users/vladyslavblackmoore/Downloads/log.txt', 'r') as file, open('/Users/vladyslavblackmoore/Downloads/nlog.txt', 'w') as nfile:
    for line in file:
        if line.split(', ')[1] == '503 Unavailable':
            dt = datetime.strptime(line.split(', ')[0], '%Y-%m-%d %H:%M:%S.%f')
            nfile.write(f'Date && time: {str(dt)}')
            nfile.write(f'\nClient: {line.split(", ")[2]}')
            break
