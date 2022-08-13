import my_hero
import villain_one
import villain_two
import villain_three

import random

import sys,time


def print_slow(string_to_slow_print):
        for letter in string_to_slow_print:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.05)
            print('')
      
print_slow('LETS PLAY!!')
print('')
print_slow('MAY THE ODDS FOREVER BE IN YOUR FAVOR.')
print('')
print('')
print_slow(f'{my_hero.hero['name']} is being attacked by {villain_one.villain_one['name']}!!')
print_slow(f'Level: {villain_one.villain_one['level']} Health: {villain_one.villain_one ['health']}')
print('')

while villain_one.villian_one['health'] !=0:
    print_slow(f'{villain_one.villian_one['name']} HAS ATTACKED {my_hero.hero['name']} with ' + random {villain_one.villain_one['attacks'][]}'!!')
    print('')
    print_slow(f'{my_hero.hero['name']} has {my_hero.hero['health']-villain_one.villain_one['attacks'][3][1]} remaining.')
    print('')
    print_slow('CHOOSE YOUR ATTACK:')
    print('')
    print_slow(f'PRESS 0 TO SELECT {my_hero.hero['attacks'][0][0]} ({my_hero.hero['attacks'][0][1]} DAMAGE)')
    print_slow(f'PRESS 1 TO SELECT {my_hero.hero['attacks'][1][0]} ({my_hero.hero['attacks'][1][1]} DAMAGE)')
    print_slow(f'PRESS 2 TO SELECT {my_hero.hero['attacks'][2][0]} ({my_hero.hero['attacks'][2][1]} DAMAGE)')
    print_slow(f'PRESS 3 TO SELECT {my_hero.hero['attacks'][3][0]} ({my_hero.hero['attacks'][3][1]} DAMAGE)')
    print_slow(f'PRESS 4 TO SELECT {my_hero.hero['attacks'][4][0]} ({my_hero.hero['attacks'][4][1]} DAMAGE)')
    print_slow(f'PRESS 5 TO SELECT {my_hero.hero['attacks'][5][0]} ({my_hero.hero['attacks'][5][1]} DAMAGE)')
    print_slow(f'PRESS 6 TO SELECT {my_hero.hero['attacks'][6][0]} ({my_hero.hero['attacks'][6][1]} DAMAGE)')
    print('')
    user_attack =input('SELECT YOUR ATTACK: ')
    
    print_slow('\033[1;35;40m'+ random {my_hero.hero['challenges']})
    print('')
    if user_attack == 0:
        print_slow(f'{my_hero.hero['name']} has attacked {villain_one.villain_one['name']} with {my_hero.hero['attacks'][0][0]} and caused {my_hero.hero['attacks'][0][1]} damage!!')
        print_slow(f'{villain_one.villian_one['name']} has {my_hero.hero['attacks'][0][1] - villain_one.villain_one['health']} remaining.')
    if user_attack == 1:
        print_slow(f'{my_hero.hero['name']} has attacked {villain_one.villain_one['name']} with {my_hero.hero['attacks'][1][0]} and caused {my_hero.hero['attacks'][1][1]} damage!!')
        print_slow(f'{villain_one.villian_one['name']} has {my_hero.hero['attacks'][1][1] - villain_one.villain_one['health']} remaining.')
    if user_attack == 2:
        print_slow(f'{my_hero.hero['name']} has attacked {villain_one.villain_one['name']} with {my_hero.hero['attacks'][2][0]} and caused {my_hero.hero['attacks'][2][1]} damage!!')
        print_slow(f'{villain_one.villian_one['name']} has {my_hero.hero['attacks'][2][1] - villain_one.villain_one['health']} remaining.')
    if user_attack == 3:
        print_slow(f'{my_hero.hero['name']} has attacked {villain_one.villain_one['name']} with {my_hero.hero['attacks'][3][0]} and caused {my_hero.hero['attacks'][3][1]} damage!!')    
        print_slow(f'{villain_one.villian_one['name']} has {my_hero.hero['attacks'][3][1] - villain_one.villain_one['health']} remaining.')
    if my_hero.hero['health'] ==0:
        print_slow(f'{my_hero.hero['name']} HAS BEEN DEFEATED BY {villain_one.villain_one['name']}!! GAME OVER!!!')
    if villain_one.villian_one['health'] ==0:
        print_slow(f'{my_hero.hero['name']} HAS DEFEATED {villain_one.villain_one['name']}!! TIME TO LEVEL UP!')
        print('')
        print_slow(f'\033[1;33;40m + Looted {villain_one.villian_one['coins']['copper']} copper coins!')
        print_slow(f'\033[1;33;40m + Looted {villain_one.villian_one['coins']['silver']} silver coins!')
        print_slow(f'\033[1;33;40m + Looted {villain_one.villian_one['coins']['gold']} gold coins!')
        print('')
        print_slow(f'{my_hero.hero['name']} now has {villain_one.villain_one['coins']['copper']+ my_hero.hero['coins']['copper']} copper, {villain_one.villain_one['coins']['silver']+ my_hero.hero['coins']['silver']} silver, and {villain_one.villain_one['coins']['gold']+ my_hero.hero['coins']['gold']} gold coins.')
        print('')
        print_slow(f'\033[1;33;40m + Added {villain_one.villian_one['equipment']} equipment!')
        print('')
        print_slow(f'{my_hero.hero['name']} has leveled up to level {my_hero.hero['level']+1}!')
        print('')
        print_slow(f'{my_hero.hero['name']} has gained a new attack!')
        user_new_attack = input('Please enter new attack: ')
        print('')
        print(f'Added{user_new_attack} to {my_hero.hero['attacks']} with 100 damage.')  
        my_converted_attack_tuple = list(my_hero.hero['attacks'])
        my_converted_attack_tuple.append = user_new_attack, 100
        my_hero.hero['attacks'] = tuple(my_converted_attack_tuple)
        print('')
print('')
print('')










print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')

