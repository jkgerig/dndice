# package imports
import random

# define basic dice types

def d20(rolls=1, mod=0):
    final_result = []
    for roll in range(rolls):
        final_result.append(random.randint(1, 20) + mod)
    return sum(final_result)

def d2(rolls=1, mod=0):
    final_result = []
    for roll in range(rolls):
        final_result.append(random.randint(1, 2) + mod)
    return sum(final_result)

def d4(rolls=1, mod=0):
    final_result = []
    for roll in range(rolls):
        final_result.append(random.randint(1, 4) + mod)
    return sum(final_result)

def d6(rolls=1, mod=0):
    final_result = []
    for roll in range(rolls):
        final_result.append(random.randint(1, 6) + mod)
    return sum(final_result)

def d8(rolls=1, mod=0):
    final_result = []
    for roll in range(rolls):
        final_result.append(random.randint(1, 8) + mod)
    return sum(final_result)

def d10(rolls=1, mod=0):
    final_result = []
    for roll in range(rolls):
        final_result.append(random.randint(1, 10) + mod)
    return sum(final_result)

def d12(rolls=1, mod=0):
    final_result = []
    for roll in range(rolls):
        final_result.append(random.randint(1, 12) + mod)
    return sum(final_result)

def d100(rolls=1, mod=0):
    final_result = []
    for roll in range(rolls):
        final_result.append(random.randint(1, 100) + mod)
    return sum(final_result)


# Ability Rolls

def strength():
    result = d20(mod=1)
    return result
    
def dexterity():
    result = d20(mod=0)
    return result

def constitution():
    result = d20(mod=2)
    return result

def intelligence():
    result = d20(mod=2)
    return result

def wisdom():
    result = d20(mod=-1)
    return result

def charisma():
    result = d20(mod=3)
    return result


# Other Rolls and Skills

def initiative():
    result = d20(mod=0)
    return result

def acrobatics():
    result = d20(mod=0)
    return result

def animal_handling():
    result = d20(mod=-1)
    return result

def arcana():
    result = d20(mod=4)
    return result

def athletics():
    result = d20(mod=1)
    return result

def deception():
    result = d20(mod=5)
    return result

def history():
    result = d20(mod=2)
    return result

def insight():
    result = d20(mod=-1)
    return result

def intimidation():
    result = d20(mod=3)
    return result

def investigation():
    result = d20(mod=4)
    return result

def medicine():
    result = d20(mod=-1)
    return result

def nature():
    result = d20(mod=2)
    return result

def perception():
    result = d20(mod=-1)
    return result

def performance():
    result = d20(mod=3)
    return result

def persuasion():
    result = d20(mod=5)
    return result

def religion():
    result = d20(mod=2)
    return result

def sleight_of_hand():
    result = d20(mod=0)
    return result

def stealth():
    result = d20(mod=0)
    return result

def survival():
    result = d20(mod=-1)
    return result


# Spells

def earth_tremor(level=1):
    damage = d6(rolls=level)
    return damage

def magic_missile(level=1):
    damage = d4(rolls=(2 + level), mod=1)
    return damage


