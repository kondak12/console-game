from source import characters_stats
from source import rep_library
from source import functions


def use_seller():
    input(functions.typing_effect(rep_library.seller_page))

    seller_items = [f"{rep_library.seller_medvejevika[0]}", f"{rep_library.seller_pechenierka[0]}", f"{rep_library.seller_sword[0]}",
                    f"{rep_library.seller_cell_of_body_2[0]}", "\nУ вас " f"{characters_stats.character_coins}" " монет(ы)."]

    seller_keyword_list = ["1", "2", "3", "4", "уйти", "справка"]

    seller_choose = ""


    while seller_choose not in seller_keyword_list:
        for i in seller_items:
            print(i)



        print("\nВведите 'уйти' чтобы уйти")

        seller_choose = input("Введите номер товара для его покупки -> ")
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


    if seller_choose == "1":

        functions.seller_choice(rep_library.seller_medvejevika[-1], rep_library.seller_medvejevika[1],
                                rep_library.seller_medvejevika[2], rep_library.seller_medvejevika[3])


    if seller_choose == "2":
        functions.seller_choice(rep_library.seller_pechenierka[-1], rep_library.seller_pechenierka[1],
                                rep_library.seller_pechenierka[2], rep_library.seller_pechenierka[3])


    if seller_choose == "3":

        if characters_stats.seller_triggers[0] == 1:

            functions.seller_choice(rep_library.seller_sword[-1], rep_library.seller_sword[1],
                                    rep_library.seller_sword[2], rep_library.seller_sword[3])

            print(rep_library.bought_seller_sword, "  Базовый урон:   Мин. -> 12  /  Макс. -> 16\n")

            characters_stats.character_default_damage = [12, 16]

            characters_stats.character_sword = rep_library.sword_2

            rep_library.seller_sword[0] = "Железный меч -> ПРОДАНО"

            characters_stats.seller_triggers[0] = 0

        else:
            print("Такого меча я уже не сделаю, парень...\n")


    if seller_choose == "4":

        if characters_stats.seller_triggers[1] == 1:
            functions.seller_choice(rep_library.seller_cell_of_body_2[-1], rep_library.seller_cell_of_body_2[1],
                                    rep_library.seller_cell_of_body_2[2], rep_library.seller_cell_of_body_2[3])

            print(rep_library.bought_cell_of_body_2, "  Макс. здоровье -> 130\n")

            characters_stats.character_default_health = 130
            characters_stats.character_health = 130

            characters_stats.character_cell_of_body = rep_library.cell_of_body_2

            rep_library.seller_cell_of_body_2[0] = "Ячейка крепкости 2 -> ПРОДАНО"

            characters_stats.seller_triggers[1] = 0

        else:
            print("Медальон был только один.\n")