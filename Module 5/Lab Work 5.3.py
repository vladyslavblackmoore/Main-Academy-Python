word = 'Found name: '
ids = {'name': 'Daun na zadanii', 'age': 20}


def func(word1, name, *args, age=None):
    print(word1, name)
    print('Age: ', age)
    print(args)


func(word, **ids)
func(word, ids['name'], *list(range(10)))
