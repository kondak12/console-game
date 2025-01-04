import act_2

import act_3

import characters_stats

import functions



functions.beginning_actions()


while characters_stats.game_status != 0 and characters_stats.act_2_trigger != 1:

    act_2_trigger = functions.choose_action()


if characters_stats.act_2_trigger == 1:

    act_2.act_2_actions()


if characters_stats.game_status != 0:

    act_3.act_3_actions()



if __name__ == "main":
    functions.beginning_actions()