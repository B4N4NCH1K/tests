def my_code(magic_info):
    for key,value in magic_info.items():
        print(f'{key}:')
        if type(value) is dict:
            for key_2,value_2 in value.items():
                print(f'  {key_2}:\n    {value_2}')
        else:
            print(f'  {value}')

my_code({
    'first': 'first_value',
    'second': 'second_value'
})

print(' ')

my_code({
    '1': {
        'child': '1/child/value'
    },
    '2': '2/value'
})
