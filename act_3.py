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
        fight.fighting(1.5)


    if act_3_action_1_num == "2":

        characters_stats.character_sword = "Платиновый меч"
        characters_stats.character_key_inventory.append("платиновый меч")
        characters_stats.character_default_damage = [16, 20]
        rep_library.act_3_action_1_choose_2(characters_stats.character_dmg()[0], characters_stats.character_dmg()[1])