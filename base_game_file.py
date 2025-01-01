import act_2

import characters_stats

import functions


act_2_trigger = 0


functions.beginning_actions()


while characters_stats.game_status != 0 and act_2_trigger != 1:

    act_2_trigger = functions.choose_action()


if act_2_trigger == 1:
    act_2.act_2_actions()