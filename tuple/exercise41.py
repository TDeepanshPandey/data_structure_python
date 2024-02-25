def generate_code(name):
    if not len(name) > 2:
        raise ValueError('The name must be longer than 2 characters.')
    code = name[:3] + '-' + name[-3:][::-1]
    code = code.upper()
    return name, len(name), code

result = generate_code('Volvo')
print(result)