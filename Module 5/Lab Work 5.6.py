my_list = ['ab', 'cd', 'ef', 'gh', 'kl']


def my_decorat(func):
    def wrapper(string):
        with open('config.data', 'r+') as file:
            func(file, string)
    return wrapper


@my_decorat
def write_config(file, string):
    if "Configuration file! Do not modify!" in file.read():
        file.write(f'{string}\n')
    else:
        file.write(f"Configuration file! Do not modify!\n{string}")


for i in my_list:
    write_config(i)

