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
print_slow(f'Level: {villain_one.villain_one['level']} Health: {villain_one.villain_one['health']}')
print('')

while villain_one.villian_one['health'] !=0:
    print_slow(f'{villain_one.villian_one['name']} HAS ATTACKED {my_hero.hero['name']} with ' + random {villain_one.villain_one['attacks'][]}'!!')
    print('')
    print_slow('\033[1;31;40m'+ {villain_one.villian_one['name']}':' + random {villain_one.villain_one['challenges']})
    print('')
    print_slow(f'{my_hero.hero['name']} has {my_hero.hero['health']-villain_one.villain_one['attacks'][3][1]} remaining.')
    print('')
    print_slow('\033[1;35;40m'+ {my_hero.hero['name']}':' + random {my_hero.hero['pleas']})
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
    
    print_slow('\033[1;35;40m'+ {my_hero.hero['name']}':' + random {my_hero.hero['challenges']})
    print('')
    if user_attack == 0:
        print_slow(f'{my_hero.hero['name']} has attacked {villain_one.villain_one['name']} with {my_hero.hero['attacks'][0][0]} and caused {my_hero.hero['attacks'][0][1]} damage!!')
        print_slow(f'{villain_one.villian_one['name']} has {villain_one.villain_one['health']-my_hero.hero['attacks'][0][1]} remaining.')
    if user_attack == 1:
        print_slow(f'{my_hero.hero['name']} has attacked {villain_one.villain_one['name']} with {my_hero.hero['attacks'][1][0]} and caused {my_hero.hero['attacks'][1][1]} damage!!')
        print_slow(f'{villain_one.villian_one['name']} has {villain_one.villain_one['health']-my_hero.hero['attacks'][1][1]} remaining.')
    if user_attack == 2:
        print_slow(f'{my_hero.hero['name']} has attacked {villain_one.villain_one['name']} with {my_hero.hero['attacks'][2][0]} and caused {my_hero.hero['attacks'][2][1]} damage!!')
        print_slow(f'{villain_one.villian_one['name']} has {villain_one.villain_one['health']-my_hero.hero['attacks'][2][1]} remaining.')
    if user_attack == 3:
        print_slow(f'{my_hero.hero['name']} has attacked {villain_one.villain_one['name']} with {my_hero.hero['attacks'][3][0]} and caused {my_hero.hero['attacks'][3][1]} damage!!')    
        print_slow(f'{villain_one.villian_one['name']} has {villain_one.villain_one['health']-my_hero.hero['attacks'][3][1]} remaining.')
    if user_attack == 4:
        print_slow(f'{my_hero.hero['name']} has attacked {villain_one.villain_one['name']} with {my_hero.hero['attacks'][4][0]} and caused {my_hero.hero['attacks'][1][1]} damage!!')
        print_slow(f'{villain_one.villian_one['name']} has {villain_one.villain_one['health']-my_hero.hero['attacks'][4][1]} remaining.')
    if user_attack == 5:
        print_slow(f'{my_hero.hero['name']} has attacked {villain_one.villain_one['name']} with {my_hero.hero['attacks'][5][0]} and caused {my_hero.hero['attacks'][2][1]} damage!!')
        print_slow(f'{villain_one.villian_one['name']} has {villain_one.villain_one['health']-my_hero.hero['attacks'][5][1]} remaining.')
    if user_attack == 6:
        print_slow(f'{my_hero.hero['name']} has attacked {villain_one.villain_one['name']} with {my_hero.hero['attacks'][6][0]} and caused {my_hero.hero['attacks'][3][1]} damage!!')    
        print_slow(f'{villain_one.villian_one['name']} has {villain_one.villain_one['health']-my_hero.hero['attacks'][6][1]} remaining.')
    if my_hero.hero['health'] ==0:
        print_slow(f'{my_hero.hero['name']} HAS BEEN DEFEATED BY {villain_one.villain_one['name']}!! GAME OVER!!!')
    if villain_one.villian_one['health'] ==0:
        print_slow('\033[1;31;40m'+ {villain_one.villian_one['name']}':' + random {villain_one.villain_one['pleas']})
        print('')
        print_slow(f'{my_hero.hero['name']} HAS DEFEATED {villain_one.villain_one['name']}!! TIME TO LEVEL UP!')
        print('')
        print_slow(f'\033[1;33;40m + Looted {villain_one.villian_one['coins']['copper']} copper coins!')
        print_slow(f'\033[1;33;40m + Looted {villain_one.villian_one['coins']['silver']} silver coins!')
        print_slow(f'\033[1;33;40m + Looted {villain_one.villian_one['coins']['gold']} gold coins!')
        print('')
        my_hero.hero['coins'] = my_hero.hero['coins']['copper']['silver']['gold']+villain_one.villian_one['coins']['copper']['silver']['gold']
        print_slow(f'{my_hero.hero['name']} now has {myhero.hero['coins']['copper']',' +my_hero.hero['coins']['silver']} silver, and' +my_hero.hero['coins']['gold']} 'gold coins.')
        print('')
        my_hero.hero['equipment'] = my_hero.hero['equipment'] + villain_one.villian_one['equipment']
        print_slow(f'\033[1;33;40m + Added {villain_one.villian_one['equipment']} equipment!')
        print('')
        my_hero.hero['level'] = my_hero.hero['level']+1
        print_slow(f'{my_hero.hero['name']} has leveled up to level {my_hero.hero['level']}!')
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
print_slow(f'{my_hero.hero['name']} has encountered {villain_two.villain_two['name']}!!')
print_slow(f'Level: {villain_two.villain_two['level']} Health: {villain_two.villain_two['health']}')
print('')

while villain_two.villian_two['health'] !=0:
    print_slow(f'{villain_two.villian_two['name']} HAS ATTACKED {my_hero.hero['name']} with ' + random {villain_two.villain_two['attacks'][]}'!!')
    print('')
    print_slow('\033[1;31;40m'+ {villain_two.villian_two['name']}':' + random {villain_two.villain_two['challenges']})
    print('')
    print_slow(f'{my_hero.hero['name']} has {my_hero.hero['health']-villain_two.villain_two['attacks'][3][1]} remaining.')
    print('')
    print_slow('\033[1;35;40m'+ {my_hero.hero['name']}':' + random {my_hero.hero['pleas']})
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
    
    print_slow('\033[1;35;40m'+ {my_hero.hero['name']}':' + random {my_hero.hero['challenges']})
    print('')
    if user_attack == 0:
        print_slow(f'{my_hero.hero['name']} has attacked {villain_two.villain_two['name']} with {my_hero.hero['attacks'][0][0]} and caused {my_hero.hero['attacks'][0][1]} damage!!')
        print_slow(f'{villain_two.villian_two['name']} has {villain_two.villain_two['health']-my_hero.hero['attacks'][0][1]} remaining.')
    if user_attack == 1:
        print_slow(f'{my_hero.hero['name']} has attacked {villain_two.villain_two['name']} with {my_hero.hero['attacks'][1][0]} and caused {my_hero.hero['attacks'][1][1]} damage!!')
        print_slow(f'{villain_two.villian_two['name']} has {villain_two.villain_two['health']-my_hero.hero['attacks'][1][1]} remaining.')
    if user_attack == 2:
        print_slow(f'{my_hero.hero['name']} has attacked {villain_two.villain_two['name']} with {my_hero.hero['attacks'][2][0]} and caused {my_hero.hero['attacks'][2][1]} damage!!')
        print_slow(f'{villain_two.villian_two['name']} has {villain_two.villain_two['health']-my_hero.hero['attacks'][2][1]} remaining.')
    if user_attack == 3:
        print_slow(f'{my_hero.hero['name']} has attacked {villain_two.villain_two['name']} with {my_hero.hero['attacks'][3][0]} and caused {my_hero.hero['attacks'][3][1]} damage!!')    
        print_slow(f'{villain_two.villian_two['name']} has {villain_two.villain_two['health']-my_hero.hero['attacks'][3][1]} remaining.')
    if user_attack == 4:
        print_slow(f'{my_hero.hero['name']} has attacked {villain_two.villain_two['name']} with {my_hero.hero['attacks'][4][0]} and caused {my_hero.hero['attacks'][1][1]} damage!!')
        print_slow(f'{villain_two.villian_two['name']} has {villain_two.villain_two['health']-my_hero.hero['attacks'][4][1]} remaining.')
    if user_attack == 5:
        print_slow(f'{my_hero.hero['name']} has attacked {villain_two.villain_two['name']} with {my_hero.hero['attacks'][5][0]} and caused {my_hero.hero['attacks'][2][1]} damage!!')
        print_slow(f'{villain_two.villian_two['name']} has {villain_two.villain_two['health']-my_hero.hero['attacks'][5][1]} remaining.')
    if user_attack == 6:
        print_slow(f'{my_hero.hero['name']} has attacked {villain_two.villain_two['name']} with {my_hero.hero['attacks'][6][0]} and caused {my_hero.hero['attacks'][3][1]} damage!!')    
        print_slow(f'{villain_two.villian_two['name']} has {villain_two.villain_two['health']-my_hero.hero['attacks'][6][1]} remaining.')
    if my_hero.hero['health'] ==0:
        print_slow(f'{my_hero.hero['name']} HAS BEEN DEFEATED BY {villain_two.villain_two['name']}!! GAME OVER!!!')
    if villain_two.villian_two['health'] ==0:
        print_slow('\033[1;31;40m'+ {villain_two.villian_two['name']}':' + random {villain_two.villain_two['pleas']})
        print('')
        print_slow(f'{my_hero.hero['name']} HAS DEFEATED {villain_two.villain_two['name']}!! TIME TO LEVEL UP!')
        print('')
        print_slow(f'\033[1;33;40m + Looted {villain_two.villian_two['coins']['copper']} copper coins!')
        print_slow(f'\033[1;33;40m + Looted {villain_two.villian_two['coins']['silver']} silver coins!')
        print_slow(f'\033[1;33;40m + Looted {villain_two.villian_two['coins']['gold']} gold coins!')
        print('')
        my_hero.hero['coins'] = my_hero.hero['coins']['copper']['silver']['gold']+villain_two.villian_two['coins']['copper']['silver']['gold']
        print_slow(f'{my_hero.hero['name']} now has {myhero.hero['coins']['copper']',' +my_hero.hero['coins']['silver']} silver, and' +my_hero.hero['coins']['gold']} 'gold coins.')
        print('')
        my_hero.hero['equipment'] = my_hero.hero['equipment'] + villain_two.villian_two['equipment']
        print_slow(f'\033[1;33;40m + Added {villain_two.villian_two['equipment']} equipment!')
        print('')
        my_hero.hero['level'] = my_hero.hero['level']+1
        print_slow(f'{my_hero.hero['name']} has leveled up to level {my_hero.hero['level']}!')
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
print_slow(f'{my_hero.hero['name']}, your final test: {villain_two.villain_two['name']}!!')
print_slow(f'Level: {villain_three.villain_three['level']} Health: {villain_three.villain_three['health']}')
print('')

while villain_three.villian_three['health'] !=0:
    print_slow(f'{villain_three.villian_three['name']} HAS ATTACKED {my_hero.hero['name']} with ' + random {villain_three.villain_three['attacks'][]}'!!')
    print('')
    print_slow('\033[1;31;40m'+ {villain_three.villian_three['name']}':' + random {villain_three.villain_three['challenges']})
    print('')
    print_slow(f'{my_hero.hero['name']} has {my_hero.hero['health']-villain_three.villain_three['attacks'][3][1]} remaining.')
    print('')
    print_slow('\033[1;35;40m'+ {my_hero.hero['name']}':' + random {my_hero.hero['pleas']})
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
    
    print_slow('\033[1;35;40m'+ {my_hero.hero['name']}':' + random {my_hero.hero['challenges']})
    print('')
    if user_attack == 0:
        print_slow(f'{my_hero.hero['name']} has attacked {villain_three.villain_three['name']} with {my_hero.hero['attacks'][0][0]} and caused {my_hero.hero['attacks'][0][1]} damage!!')
        print_slow(f'{villain_three.villian_three['name']} has {villain_three.villain_three['health']-my_hero.hero['attacks'][0][1]} remaining.')
    if user_attack == 1:
        print_slow(f'{my_hero.hero['name']} has attacked {villain_three.villain_three['name']} with {my_hero.hero['attacks'][1][0]} and caused {my_hero.hero['attacks'][1][1]} damage!!')
        print_slow(f'{villain_three.villian_three['name']} has {villain_three.villain_three['health']-my_hero.hero['attacks'][1][1]} remaining.')
    if user_attack == 2:
        print_slow(f'{my_hero.hero['name']} has attacked {villain_three.villain_three['name']} with {my_hero.hero['attacks'][2][0]} and caused {my_hero.hero['attacks'][2][1]} damage!!')
        print_slow(f'{villain_three.villian_three['name']} has {villain_three.villain_three['health']-my_hero.hero['attacks'][2][1]} remaining.')
    if user_attack == 3:
        print_slow(f'{my_hero.hero['name']} has attacked {villain_three.villain_three['name']} with {my_hero.hero['attacks'][3][0]} and caused {my_hero.hero['attacks'][3][1]} damage!!')    
        print_slow(f'{villain_three.villian_three['name']} has {villain_three.villain_three['health']-my_hero.hero['attacks'][3][1]} remaining.')
    if user_attack == 4:
        print_slow(f'{my_hero.hero['name']} has attacked {villain_three.villain_three['name']} with {my_hero.hero['attacks'][4][0]} and caused {my_hero.hero['attacks'][1][1]} damage!!')
        print_slow(f'{villain_three.villian_three['name']} has {villain_three.villain_three['health']-my_hero.hero['attacks'][4][1]} remaining.')
    if user_attack == 5:
        print_slow(f'{my_hero.hero['name']} has attacked {villain_three.villain_three['name']} with {my_hero.hero['attacks'][5][0]} and caused {my_hero.hero['attacks'][2][1]} damage!!')
        print_slow(f'{villain_three.villian_three['name']} has {villain_three.villain_three['health']-my_hero.hero['attacks'][5][1]} remaining.')
    if user_attack == 6:
        print_slow(f'{my_hero.hero['name']} has attacked {villain_three.villain_three['name']} with {my_hero.hero['attacks'][6][0]} and caused {my_hero.hero['attacks'][3][1]} damage!!')    
        print_slow(f'{villain_three.villian_three['name']} has {villain_three.villain_three['health']-my_hero.hero['attacks'][6][1]} remaining.')
    if my_hero.hero['health'] ==0:
        print_slow(f'{my_hero.hero['name']} HAS BEEN DEFEATED BY {villain_three.villain_three['name']}!! GAME OVER!!!')
    if villain_three.villian_three['health'] ==0:
        print_slow('\033[1;31;40m'+ {villain_three.villian_three['name']}':' + random {villain_three.villain_three['pleas']})
        print('')
        print_slow(f'{my_hero.hero['name']} HAS DEFEATED {villain_three.villain_three['name']}!!'+{my_hero.hero['name']}' HAS BECOME A SUPREME SUPER HERO! CONGRATULATIONS!')
        print('')
        print_slow(f'\033[1;33;40m + Looted {villain_three.villian_three['coins']['copper']} copper coins!')
        print_slow(f'\033[1;33;40m + Looted {villain_three.villian_three['coins']['silver']} silver coins!')
        print_slow(f'\033[1;33;40m + Looted {villain_three.villian_three['coins']['gold']} gold coins!')
        print('')
         my_hero.hero['coins'] = my_hero.hero['coins']['copper']['silver']['gold']+villain_three.villian_three['coins']['copper']['silver']['gold']
        print_slow(f'{my_hero.hero['name']} now has {myhero.hero['coins']['copper']',' +my_hero.hero['coins']['silver'] 'silver, and ' +my_hero.hero['coins']['gold'] 'gold coins.')
        print('')
        my_hero.hero['equipment'] = my_hero.hero['equipment'] + villain_three.villian_three['equipment']
        print_slow(f'\033[1;33;40m + Added {villain_three.villian_three['equipment']} equipment!')
        print('')
        my_hero.hero['level'] = my_hero.hero['level']+1
        print_slow(f'{my_hero.hero['name']} has leveled up to level {my_hero.hero['level']}!')
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
print('')
print('')

