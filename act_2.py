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
        act_2_choose_1or2 = act_2_choose_1or2.lower()

        while act_2_choose != "1" and act_2_choose_1or2 != "2":
            act_2_choose_1or2 = input("Что же ответить? -> ")
            act_2_choose_1or2 = act_2_choose_1or2.lower()


        if act_2_choose_1or2 == "1":
            pass