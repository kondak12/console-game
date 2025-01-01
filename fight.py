import random

import characters_stats

import functions

import rep_library

import time


def fighting(fight_mode_ex):
    if fight_mode_ex == 0:
        print(rep_library.forest_page)


    forest_action_choose = None

    in_forest_fighter = None

    forest_fighter_1 = None

    forest_fighter_2 = None

    forest_fighter_3 = None

    fighter_eye = None


    if fight_mode_ex == 0:
        forest_fighter_1 = [30, [8, 12]]   # статы гаргульи: 0 - хп; 1 - диапазон урона

        forest_fighter_2 = [20, [4, 10]]   # статы кабана

        forest_fighter_3 = [10, [1, 8]]   # статы гриба


        forest_fighter = random.choice([forest_fighter_1, forest_fighter_2, forest_fighter_3])
        in_forest_fighter = forest_fighter


        functions.choose_fighter_rep(forest_fighter, forest_fighter_1, rep_library.reps[0], "Здоровье существа -> 30\n")

        functions.choose_fighter_rep(forest_fighter, forest_fighter_2, rep_library.reps[1], "Здоровье существа -> 20\n")

        functions.choose_fighter_rep(forest_fighter, forest_fighter_3, rep_library.reps[2], "Здоровье существа -> 10\n")


    elif fight_mode_ex == 1:
        fighter_eye = [100, [15, 20]]   # статы Глаза

        forest_fighter = fighter_eye
        in_forest_fighter = fighter_eye

    time.sleep(2)



    while characters_stats.character_health > 0 and forest_action_choose != "бег" and in_forest_fighter[0] > 0:

        forest_action_choose = input(rep_library.fight_choose)
        forest_action_choose = forest_action_choose.lower()

        forest_action_choose_list = ["бег", "инвентарь", "инв", "удар"]

        while forest_action_choose not in forest_action_choose_list:
            forest_action_choose = input("Сейчас не время тормозить!\n" + rep_library.fight_choose)
            forest_action_choose = forest_action_choose.lower()

        if forest_action_choose == "инвентарь" or forest_action_choose == "инв":
            functions.use_inventory()

        if forest_action_choose == "удар":
            forest_character_damage = random.randint(characters_stats.character_damage[0], characters_stats.character_damage[1])

            in_forest_fighter[0] -= forest_character_damage

            if in_forest_fighter[0] < 0:
                in_forest_fighter[0] = 0

            print("Вы нанесли", forest_character_damage, "урона врагу...  Здоровье врага ->", in_forest_fighter[0])

            time.sleep(2)

        if in_forest_fighter[0] != 0:
            enemy_damage = random.randint(in_forest_fighter[1][0], in_forest_fighter[1][1])

            print("Враг ударил вас. Он нанёс", enemy_damage,"урона.\n")
            characters_stats.character_health -= enemy_damage
            print("Здоровье персонажа  ->", characters_stats.character_health, "\n")

            time.sleep(2)



    if fight_mode_ex == 0:   # бой в лесу

        if in_forest_fighter[0] < 1 and in_forest_fighter == forest_fighter_1:
            print(rep_library.rep_forest_fight_end_1)
            characters_stats.character_default_lvl += 0.6

            if functions.chance(27):
                print(rep_library.rep_forest_fight_coins_1)
                characters_stats.character_coins += 3


        if in_forest_fighter[0] < 1 and in_forest_fighter == forest_fighter_2:
            print(rep_library.rep_forest_fight_end_2)
            characters_stats.character_default_lvl += 0.4
            characters_stats.character_health += 10

            if characters_stats.character_health > characters_stats.character_default_health:
                characters_stats.character_health = characters_stats.character_default_health

            if functions.chance(35):
                print(rep_library.rep_forest_fight_coins_2)
                characters_stats.character_coins += 2


        if in_forest_fighter[0] < 1 and in_forest_fighter == forest_fighter_3:
            print(rep_library.rep_forest_fight_end_3)
            characters_stats.character_default_lvl += 0.2

            if functions.chance(40):
                print(rep_library.rep_forest_fight_coins_3)
                characters_stats.character_coins += 1


        if forest_action_choose == "бег":
            print(rep_library.rep_run)
            characters_stats.character_default_lvl -= 0.3


        forest_fighter_1[0] = 30

        forest_fighter_2[0] = 20

        forest_fighter_3[0] = 5


    elif fight_mode_ex == 1:

        if in_forest_fighter[0] < 1:
            characters_stats.character_default_health = 150
            characters_stats.character_health = 150
            characters_stats.character_cell_of_body = "Ячейка крепкости тела 3"
            rep_library.rep_forest_fight_end_eye()
            characters_stats.character_default_lvl += 3



    if characters_stats.character_health > 0:
        print("Здоровье персонажа  -> ", characters_stats.character_health)
        print("lvl  -> ", characters_stats.character_default_lvl,"\n")

        time.sleep(3)


    if characters_stats.character_health < 1:
        print("Враг оказался сильнее... \nВы програли!\n")
        characters_stats.game_status = 0

        time.sleep(5)