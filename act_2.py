import time

import rep_library

import functions

import characters_stats

import fight


def act_2_actions():
    rep_library.act_2_beginning()

    print(input(rep_library.act_2_action_1))

    rep_library.act_2_action_2(characters_stats.character_name)

    act_2_choose = input()
    act_2_choose = act_2_choose.lower()

    while act_2_choose != "стоять" and act_2_choose != "бежать":
        act_2_choose = input("Ну же " + characters_stats.character_name + ", думай! -> ")
        act_2_choose = act_2_choose.lower()



    if act_2_choose == "стоять":   # стоять
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

                characters_stats.character_dmg()[0] += 6
                characters_stats.character_dmg()[1] += 6

                rep_library.eye_question_choose_dmg(characters_stats.character_default_health, characters_stats.character_dmg()[0],
                                                    characters_stats.character_dmg()[1])


            if act_2_choose_hp_dmg == "2":
                characters_stats.character_default_health += 30
                characters_stats.character_health = characters_stats.character_default_health

                characters_stats.character_dmg()[0] -= 6
                characters_stats.character_dmg()[1] -= 6

                rep_library.eye_question_choose_hp(characters_stats.character_default_health,characters_stats.character_dmg()[0],
                                                    characters_stats.character_dmg()[1])


            if act_2_choose_hp_dmg == "3":
                rep_library.eye_question_choose_quit()

                characters_stats.character_inventory.append("медвежевика")
                characters_stats.character_inventory.append("медвежевика")
                characters_stats.character_inventory.append("медвежевика")



        if act_2_choose_1or2 == "2":
            rep_library.eye_answer_2()

            print(rep_library.rep_forest_fight_begin_eye)

            fight.fighting(1)



    if act_2_choose == "бежать":
        rep_library.act_2_choose_run()

        time.sleep(1.5)

        act_2_choose_1or2 = input("Что ответить? -> ")

        while act_2_choose_1or2 != "1" and act_2_choose_1or2 != "2":
            act_2_choose_1or2 = input("Что же ответить? -> ")


        if act_2_choose_1or2 == "1":
            characters_stats.character_dmg()[0] += 4
            characters_stats.character_dmg()[1] += 4
            characters_stats.character_default_health += 20
            characters_stats.character_health = characters_stats.character_health

            rep_library.act_2_choose_run_2(characters_stats.character_default_health, characters_stats.character_dmg()[0],
                                           characters_stats.character_dmg()[1])

            characters_stats.character_inventory.append("печеньерка")
            characters_stats.character_inventory.append("печеньерка")


        if act_2_choose_1or2 == "2":
            rep_library.eye_answer_2()
            print(rep_library.rep_forest_fight_begin_eye)

            fight.fighting(1)

    rep_library.act_2_end(functions.characters_stats.character_name)
    characters_stats.save_number = 3
    functions.autosave_question(characters_stats.save_number)