'''create dict with 5 items, where keys will be country name and value - domain name, i.e. {Ukraine:UA}'''
myDictCountry = {'Ukraine': 'UA',
          'USA': 'US',
          'Russia': 'RU',
          'Australia': 'AT',
          'Belarus': 'BY'}

'''create another dict with 5 items, where values of countries will be keys, and values will be the capitals i.e. {'UA': 'Kiev'}'''
myDictCapital = {'UA': 'Kiev',
                 'US': 'Washington',
                 'RU': 'Moscow',
                 'AT': 'Canberra',
                 'BY': 'Minsk'}

'''add one more element to each dict above'''
myDictCountry['Greece'] = 'GR'
myDictCapital['GR'] = 'Athens'

'''print sentence "Domain for COUNTRY is DOMAIN." for each record in
countries with the replace from dicts'''
for key, value in myDictCountry.items():
    print(f'Domain for {key} is {value}.')

'''print sentence "The capital of COUNTRY is CAPITAL" for each record in capitals where COUNTRY and CAPITAL have to be replaced with .format()'''
for key, value in myDictCountry.items():
    print(f'The capital of {key} is {myDictCapital[value]}.')

'''Merge sentences above together with one cycle'''
for key, value in myDictCountry.items():
    print(f'The capital of {key} is {myDictCapital[value]}, domain is {value}')

'''Add to each value of first dict another two domains: COM and GOV'''
for key, value in myDictCountry.items():
    myDictCountry[key] = [value, 'COM', 'GOV']
