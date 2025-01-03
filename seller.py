import characters_stats

import rep_library

import functions

import time


def use_seller():
    print(rep_library.seller_page)

    seller_items = [f"{rep_library.seller_medvejevika[0]}", f"{rep_library.seller_pechenierka[0]}", f"{rep_library.seller_sword_1[0]}",
                    f"{rep_library.seller_cell_of_body_2[0]}", "\nУ вас " f"{characters_stats.character_coins}" " монет(ы)."]

    seller_keyword_list = ["медвежевика", "мед", "печеньерка", "печ", "уйти", "инвентарь", "инв", "железный меч", "ячейка крепкости 2", "справка"]

    seller_choose = ""
    seller_choose = seller_choose.lower()


    while seller_choose not in seller_keyword_list:
        for i in seller_items:
            print(i)

        time.sleep(3)


        print("\nВведите 'уйти' чтобы уйти")

        seller_choose = input("Введите название товара для его покупки -> ")
        seller_choose = seller_choose.lower()

        while seller_choose not in seller_keyword_list:
            print("\nВведите 'уйти' чтобы уйти")
            seller_choose = input("Не совсем тебя понял, парень. Что? -> ")
            seller_choose = seller_choose.lower()



    if seller_choose == "справка":
        # справка
        functions.reference()



    if seller_choose == "инвентарь" or seller_choose == "инв":

        functions.use_inventory()



    if seller_choose == "медвежевика" or seller_choose == "мед":

        functions.seller_choise(rep_library.seller_medvejevika[-1], rep_library.seller_medvejevika[1],
                                rep_library.seller_medvejevika[2], rep_library.seller_medvejevika[3])


    if seller_choose == "печеньерка" or seller_choose == "печ":
        functions.seller_choise(rep_library.seller_pechenierka[-1], rep_library.seller_pechenierka[1],
                                rep_library.seller_pechenierka[2], rep_library.seller_pechenierka[3])


    if seller_choose == "железный меч":

        if "железный меч" not in characters_stats.character_key_inventory:

            functions.seller_choise(rep_library.seller_sword_1[-1], rep_library.seller_sword_1[1],
                                    rep_library.seller_sword_1[2], rep_library.seller_sword_1[3])

            characters_stats.character_key_inventory.append("железный меч")

            print(rep_library.bought_seller_sword_1, "  Базовый урон -> от 12 до 16\n")

            characters_stats.character_damage[0] += 5
            characters_stats.character_damage[1] += 5

            characters_stats.character_sword = "Железный меч"

            rep_library.seller_sword_1[0] = "Железный меч -> ПРОДАНО"

        else:
            print("Такого меча я уже не сделаю, парень...\n")



    if seller_choose == "ячейка крепкости 2":

        if "ячейка крепкости 2" not in characters_stats.character_key_inventory:
            functions.seller_choise(rep_library.seller_cell_of_body_2[-1], rep_library.seller_cell_of_body_2[1],
                                    rep_library.seller_cell_of_body_2[2], rep_library.seller_cell_of_body_2[3])

            characters_stats.character_key_inventory.append("ячейка крепкости 2")

            print(rep_library.bought_cell_of_body_2, "  Макс. здоровье -> 130\n")

            characters_stats.character_default_health = 130
            characters_stats.character_health = 130

            characters_stats.character_cell_of_body = "Ячейка крепкости тела 2"

            rep_library.seller_cell_of_body_2[0] = "Ячейка крепкости 2 -> ПРОДАНО"

        else:
            print("Медальон был только один.\n")
