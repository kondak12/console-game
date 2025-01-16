from source import rep_library
from source import functions
from source import characters_stats
from source import fight


def act_3_actions():
    print(input(rep_library.act_3_beginning))

    act_3_action_1_num = rep_library.act_3_action_1()


    if act_3_action_1_num == "1":

        rep_library.act_3_action_1_choose_1()
        fight.fighting(2)


    if act_3_action_1_num == "2":

        characters_stats.character_sword = "Платиновый меч"
        characters_stats.character_default_damage = [16, 20]
        rep_library.act_3_action_1_choose_2(characters_stats.character_dmg()[0], characters_stats.character_dmg()[1])



    act_3_action_2_choose = rep_library.act_3_action_2()

    if act_3_action_2_choose == "1":

        rep_library.act_3_action_2_choose_1_phase_1(functions.characters_stats.character_name)

        fight.fighting(3)

        act_3_action_2_choose = rep_library.act_3_action_2_choose_1_phase_2()


        if act_3_action_2_choose == "1":
            rep_library.act_3_action_2_choose_1_phase_2_1()

            fight.fighting(4)

            if characters_stats.game_status == 0:
                rep_library.bad_ending_1(characters_stats.character_name)