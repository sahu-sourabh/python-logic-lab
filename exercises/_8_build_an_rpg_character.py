full_dot = '●'
empty_dot = '○'

def create_character(character_name, strength, intelligence, charisma):
    if not isinstance(character_name, str):
        return 'The character name should be a string'
    if character_name == '':
        return 'The character should have a name'
    if len(character_name) > 10:
        return 'The character name is too long'
    if ' ' in character_name:
        return 'The character name should not contain spaces'
    
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return 'All stats should be integers'
    if strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    if strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    if strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'
    
    if strength == 1:
        strength_dots = full_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot
    elif strength == 2:
        strength_dots = full_dot + full_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot
    elif strength == 3:
        strength_dots = full_dot + full_dot + full_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot
    elif strength == 4:
        strength_dots = full_dot + full_dot + full_dot + full_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot

    if intelligence == 1:
        intelligence_dots = full_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot
    elif intelligence == 2:
        intelligence_dots = full_dot + full_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot
    elif intelligence == 3:
        intelligence_dots = full_dot + full_dot + full_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot
    elif intelligence == 4:
        intelligence_dots = full_dot + full_dot + full_dot + full_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot

    if charisma == 1:
        charisma_dots = full_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot
    elif charisma == 2:
        charisma_dots = full_dot + full_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot
    elif charisma == 3:
        charisma_dots = full_dot + full_dot + full_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot
    elif charisma == 4:
        charisma_dots = full_dot + full_dot + full_dot + full_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot + empty_dot

    return f'{character_name}\nSTR {strength_dots}\nINT {intelligence_dots}\nCHA {charisma_dots}'

print(create_character(1, 2, 3, 2))
print(create_character('Sourabh', 2, 3, 2))
print(create_character('', 2, 3, 2))
print(create_character('a', 2, 3, 2))
print(create_character('abcdefghijk', 2, 3, 2))
print(create_character('b', 2, 3, 2))
print(create_character(' ', 2, 3, 2))
print(create_character('c', '2', '3', '2'))
print(create_character('c', 2, '3', '2'))
print(create_character('c', '2', 3, '2'))
print(create_character('c', '2', '3', 2))
print(create_character('d', 2, 3, 2))
print(create_character('e', -2, -3, -2))
print(create_character('f', 2, 3, 2))
print(create_character('g', 5, 5, 5))
print(create_character('h', 2, 3, 2))
print(create_character('i', 4, 3, 2))
print(create_character('j', 1, 3, 2))
print(create_character('k', 2, 3, 2))
print(create_character('ren', 4, 2, 1))