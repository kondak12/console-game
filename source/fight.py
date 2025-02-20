import random
import time
from source import characters_stats
from source import functions
from source import rep_library


def fighting(fight_mode_ex):

    in_forest_fighter = None

    forest_fighter_1 = None

    forest_fighter_2 = None

    forest_fighter_3 = None

    count_run = 0

    princess_help = 0


    if fight_mode_ex == 0:

        functions.typing_effect(rep_library.forest_page, 0.01)


        forest_fighter_1 = [30, [8, 12]]   # статы гаргульи: 0 - хп; 1 - диапазон урона

        forest_fighter_2 = [20, [4, 10]]   # статы кабана

        forest_fighter_3 = [10, [1, 8]]   # статы гриба


        forest_fighter = random.choice([forest_fighter_1, forest_fighter_2, forest_fighter_3])
        in_forest_fighter = forest_fighter


        functions.choose_fighter_rep(forest_fighter, forest_fighter_1, rep_library.reps[0], "\033[31mЗдоровье существа -> 30\033[0m\n")

        functions.choose_fighter_rep(forest_fighter, forest_fighter_2, rep_library.reps[1], "\033[31mЗдоровье существа -> 20\033[0m\n")

        functions.choose_fighter_rep(forest_fighter, forest_fighter_3, rep_library.reps[2], "\033[31mЗдоровье существа -> 10\033[0m\n")


        time.sleep(1.5)


    elif fight_mode_ex == 1:
        in_forest_fighter = [75, [15, 20]]   # статы Глаза


    elif fight_mode_ex == 2:
        in_forest_fighter = [50, [13, 15]]    # статы Стражника


    elif fight_mode_ex == 3:
        in_forest_fighter = [100, [15, 20]]    # статы Дракона 1 фаза


    elif fight_mode_ex == 4:
        in_forest_fighter = [75,[22, 27]]     # статы Дракона 2 фаза



    while int(characters_stats.character_health) > 0 and count_run != 3 and in_forest_fighter[0] > 0:

        forest_action_choose = input(functions.typing_effect(rep_library.fight_choose, 0.01))
        forest_action_choose = forest_action_choose.lower()

        forest_action_choose_list = ["1", "2", "3", "справка"]

        while forest_action_choose not in forest_action_choose_list:
            forest_action_choose = input("Сейчас не время тормозить!\n" + rep_library.fight_choose)
            forest_action_choose = forest_action_choose.lower()


        if forest_action_choose == "справка":  # справка
            functions.reference()
            continue


        if forest_action_choose == "2":
            functions.use_inventory()
            continue


        if forest_action_choose == "1":
            forest_character_damage = random.randint(characters_stats.character_dmg()[0], characters_stats.character_dmg()[1])

            in_forest_fighter[0] -= forest_character_damage

            if in_forest_fighter[0] < 0:
                in_forest_fighter[0] = 0

            print("\033[32mВы нанесли", forest_character_damage, "урона врагу...  Здоровье врага ->", in_forest_fighter[0], "\033[0m")

            time.sleep(1.5)


        if fight_mode_ex == 1 and forest_action_choose == "3" and count_run != 3:
                count_run += 1
                if count_run != 3:
                    print("Нужно пробовать убежать от него.\n"
                        "\033[33mНужно бежать ещё", 3 - count_run, "раз!\n\033[0m")

                    time.sleep(3)



        if fight_mode_ex == 2 and forest_action_choose == "3" and count_run != 3:
            count_run += 1.5
            if count_run != 3:
                print("Нужно пробовать убежать от него.\n"
                      "\033[33mНужно бежать ещё 1 раз!\n\033[0m")

                time.sleep(3)


        if (fight_mode_ex == 3 or fight_mode_ex == 4) and forest_action_choose == "3":   # бой с Драконом
            print("\033[31mВыход завалило обломками!\n"
                  "Бежать бесполезно...\n\033[0m")

            time.sleep(3)



        if in_forest_fighter[0] != 0:
            enemy_damage = random.randint(in_forest_fighter[1][0], in_forest_fighter[1][1])


            if fight_mode_ex != 3 and fight_mode_ex != 4:
                print("\033[0mВраг ударил вас. Он нанёс", enemy_damage,"урона.\n\033[0m")

                characters_stats.character_health -= enemy_damage

                print("\033[33mЗдоровье персонажа  ->", characters_stats.character_health, "\n\033[0m")


            if fight_mode_ex == 3 or fight_mode_ex == 4:   # бой с Драконом
                dragon_phrase = random.choice([f"{rep_library.dragon_phrase_1(enemy_damage)}", f"{rep_library.dragon_phrase_2(enemy_damage)}",
                                               f"{rep_library.dragon_phrase_3(enemy_damage)}"])

                print()
                functions.typing_effect(f"{dragon_phrase}", 0.01)
                time.sleep(1)
                print()

                characters_stats.character_health -= enemy_damage
                print("\033[32mЗдоровье персонажа ->", characters_stats.character_health, "\n\033[0m")

                if princess_help != 1 and characters_stats.character_health < 30:
                    princess_help += 1

                    print(rep_library.princess_help_phrase)

                    characters_stats.character_inventory.append("медвежевика")
                    characters_stats.character_inventory.append("медвежевика")
                    characters_stats.character_inventory.append("медвежевика")

                    time.sleep(3)

            time.sleep(1.5)


        if forest_action_choose == "3" and fight_mode_ex == 0 and count_run != 3:
            count_run += 3
            print(rep_library.rep_run)
            characters_stats.character_default_lvl -= 0.3



    if fight_mode_ex == 0:   # бой в лесу

        if in_forest_fighter[0] < 1 and in_forest_fighter == forest_fighter_1:
            print(rep_library.rep_forest_fight_end_1)
            characters_stats.character_default_lvl += 0.6

            if functions.chance(40):
                print(rep_library.rep_forest_fight_coins_1)
                characters_stats.character_coins += 3


        if in_forest_fighter[0] < 1 and in_forest_fighter == forest_fighter_2:
            print(rep_library.rep_forest_fight_end_2)
            characters_stats.character_default_lvl += 0.4
            characters_stats.character_health += 10

            if characters_stats.character_health > characters_stats.character_default_health:
                characters_stats.character_health = characters_stats.character_default_health

            if functions.chance(50):
                print(rep_library.rep_forest_fight_coins_2)
                characters_stats.character_coins += 2


        if in_forest_fighter[0] < 1 and in_forest_fighter == forest_fighter_3:
            print(rep_library.rep_forest_fight_end_3)
            characters_stats.character_default_lvl += 0.2

            if functions.chance(60):
                print(rep_library.rep_forest_fight_coins_3)
                characters_stats.character_coins += 1


        forest_fighter_1[0] = 30

        forest_fighter_2[0] = 20

        forest_fighter_3[0] = 5


    elif fight_mode_ex == 1:   # бой с Глазом

        if in_forest_fighter[0] < 1:
            characters_stats.character_default_health = 150
            characters_stats.character_health = 150
            characters_stats.character_cell_of_body = rep_library.cell_of_body_3
            rep_library.rep_forest_fight_end_eye()
            characters_stats.character_default_lvl += 3


        if count_run == 3:
            rep_library.eye_fight_run()


    elif fight_mode_ex == 2:

        if in_forest_fighter[0] < 1:
            rep_library.act_3_action_1_choose_1_end()
            characters_stats.character_health += 25
            characters_stats.character_default_lvl += 2


        if count_run == 3:
            rep_library.act_3_action_1_choose_1_run()


    if count_run == 3 and fight_mode_ex == 1:
        characters_stats.character_default_lvl -= 0.6
        print("\033[31mlvl: - 0,6\n\033[0m")

        time.sleep(1.5)


    if count_run == 3 and fight_mode_ex == 2:
        characters_stats.character_default_lvl -= 0.4
        print("\033[31mlvl: - 0,4\n\033[0m")

        time.sleep(1.5)


    if characters_stats.character_health > 0:
        print("\033[32mЗдоровье персонажа  -> ", characters_stats.character_health, "\033[0m")
        print("\033[32mlvl  -> ", characters_stats.character_default_lvl,"\n\033[0m")

        time.sleep(1.5)


    if characters_stats.character_health < 1:
        characters_stats.game_status = 0

        if fight_mode_ex != 4:
            print("\033[31mВраг оказался сильнее... \nВы програли!\n\033[0m")

            time.sleep(3)