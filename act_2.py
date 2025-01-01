import time

import rep_library

import functions

import characters_stats


def act_2_actions():
    print(input(rep_library.act_2))
    print(input(rep_library.act_2_action_1))
    rep_library.act_2_action_2(functions.char_name)

    act_2_choose = ""
    act_2_choose = input()
    act_2_choose = act_2_choose.lower()

    while act_2_choose != "стоять" and act_2_choose != "бежать":
        act_2_choose = input("Ну же " + functions.char_name + ", думай! -> ")
        act_2_choose = act_2_choose.lower()



    if act_2_choose == "стоять": # стоять
        rep_library.act_2_choose_stay()

        time.sleep(1.5)

        act_2_choose_1or2 = input("Что ответить? -> ")

        while act_2_choose_1or2 != "1" and act_2_choose_1or2 != "2":
            act_2_choose_1or2 = input("Что же ответить? -> ")


        if act_2_choose_1or2 == "1":
            rep_library.eye_answer_1()
            print(rep_library.eye_question_1)

            time.sleep(1.5)

            act_2_choose_hp_dmg = input("Что выбрать? -> ")

            while act_2_choose_hp_dmg != "1" and act_2_choose_hp_dmg != "2" and act_2_choose_hp_dmg != "3":
                act_2_choose_hp_dmg = input("Что же выбрать? -> ")


            if act_2_choose_hp_dmg == "1":
                characters_stats.character_default_health -= 30
                characters_stats.character_health = characters_stats.character_default_health

                characters_stats.character_damage[0] += 6
                characters_stats.character_damage[1] += 6

                rep_library.eye_question_choose_dmg(characters_stats.character_default_health, characters_stats.character_damage[0],
                                                    characters_stats.character_damage[1])


            if act_2_choose_hp_dmg == "2":
                characters_stats.character_default_health += 30
                characters_stats.character_health = characters_stats.character_default_health

                characters_stats.character_damage[0] -= 6
                characters_stats.character_damage[1] -= 6

                rep_library.eye_question_choose_hp(characters_stats.character_default_health,characters_stats.character_damage[0],
                                                    characters_stats.character_damage[1])


            if act_2_choose_hp_dmg == "3":
                rep_library.eye_question_choose_quit()

                characters_stats.character_inventory.append("медвежевика")
                characters_stats.character_inventory.append("медвежевика")
                characters_stats.character_inventory.append("медвежевика")

                functions.use_inventory()



        if act_2_choose_1or2 == "2":
            rep_library.eye_answer_2()