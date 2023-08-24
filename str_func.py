def str_upper(user_line):
    return user_line.upper()


def str_capitalize(user_line):
    '''функция, которая делает заглавными первые буквы каждого
     слова в строке, поступившей на вход функции'''
    words = user_line.split(' ')
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)
