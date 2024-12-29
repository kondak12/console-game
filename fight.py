import random

import characters_stats

import code_library

import time


def forest_fight(reps):
    forest_action_choose = ""
    forest_action_choose = forest_action_choose.lower()


    forest_fighter_1 = [30, [8, 12]] # статы гаргульи: 0 - хп; 1 - диапазон урона

    forest_fighter_2 = [20, [4, 10]] # статы кабана

    forest_fighter_3 = [5, [1, 8]] # статы гриба


    forest_fighter = random.choice([forest_fighter_1, forest_fighter_2, forest_fighter_3])
    in_forest_fighter = forest_fighter



    if forest_fighter == forest_fighter_1:
        print(reps[0])
        print("Здоровье существа -> 30\n")

        time.sleep(2)


    if forest_fighter == forest_fighter_2:
        print(reps[1])
        print("Здоровье существа -> 20\n")

        time.sleep(2)


    if forest_fighter == forest_fighter_3:
        print(reps[2])
        print("Здоровье существа -> 5\n")

        time.sleep(2)



    while characters_stats.character_health > 0 and forest_action_choose != "бег" and in_forest_fighter[0] > 0:

        forest_action_choose = input(code_library.fight_choose)
        forest_action_choose = forest_action_choose.lower()


        while forest_action_choose != "удар" and forest_action_choose != "бег":
            forest_action_choose = input("Сейчас не время тормозить!\n" + code_library.fight_choose)
            forest_action_choose = forest_action_choose.lower()


        if forest_action_choose == "удар":
            forest_character_damage = random.randint(characters_stats.character_damage[0], characters_stats.character_damage[1])

            in_forest_fighter[0] -= forest_character_damage

            if in_forest_fighter[0] < 0:
                in_forest_fighter[0] = 0

            print("Вы нанесли", forest_character_damage,"урона врагу...  Здоровье врага ->", in_forest_fighter[0])

            time.sleep(2)


        enemy_damage = random.randint(forest_fighter[1][0], forest_fighter[1][1])

        print("Враг ударил вас. Он нанёс", enemy_damage,"урона.\n")
        characters_stats.character_health -= enemy_damage
        print("Здоровье персонажа  ->", characters_stats.character_health, "\n")

        time.sleep(2)



    if in_forest_fighter[0] < 1 and in_forest_fighter == forest_fighter_1:
        print(code_library.rep_forest_fight_end_1)
        characters_stats.character_lvl += 0.6


    if in_forest_fighter[0] < 1 and in_forest_fighter == forest_fighter_2:
        print(code_library.rep_forest_fight_end_2)
        characters_stats.character_lvl += 0.4
        characters_stats.character_health += 10


    if in_forest_fighter[0] < 1 and in_forest_fighter == forest_fighter_3:
        print(code_library.rep_forest_fight_end_3)
        characters_stats.character_lvl += 0.2


    if forest_action_choose == "бег":
        print(code_library.rep_run)
        characters_stats.character_lvl -= 0.3


    forest_fighter_1[0] = 30

    forest_fighter_2[0] = 20

    forest_fighter_3[0] = 5


    if characters_stats.character_health > 0:
        print("Здоровье персонажа  -> ", characters_stats.character_health)
        print("lvl  -> ", characters_stats.character_lvl,"\n")

        time.sleep(3)


    if characters_stats.character_health < 1:
        print("Враг оказался сильнее... \nВы програли!\n")
        characters_stats.game_status = 0

        time.sleep(5)