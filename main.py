# import my_hero
# import villain_one

# print(my_hero.hero['name'])

# os.chdir(r'C:\\Users\\anben\\Desktop\\DevCodeCamp\\RPG-1\\python')
# file = open('my_hero.py')
#dir = r'C:\\Users\\anben\\Desktop\\DevCodeCamp\\RPG\\python'

import sys,time


def print_slow(string_to_slow_print):
        for letter in string_to_slow_print:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.05)
            print('')
      
print_slow('LETS PLAY!!!!')