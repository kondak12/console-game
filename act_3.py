import time

import rep_library

import functions

import characters_stats

import fight


def act_3_actions():
    print(input(rep_library.act_3_beginning))

    act_3_action_1_num = rep_library.act_3_action_1()

    if act_3_action_1_num == "1":

        rep_library.act_3_action_1_choose_1()
        fight.fighting(2)