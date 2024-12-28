import characters_stats

import code_library


def use_seller():
    medvejevika = ["Медвежевика -> 'обычная ягода' -> лечит персонажа на 10 hp -> 3 золотых", 3]
    sword_1 = ["Железный меч -> 'выкован руками торговца' -> увеличивает урон персонажа на 4 -> 8 золотых", 8]

    seller_items = [f"{medvejevika[0]}", f"{sword_1[0]}"]
    seller_keyword_list = ["медвежевика", "железный меч", "уйти"]

    seller_choose = ""
    seller_choose = seller_choose.lower()


    while seller_choose not in seller_keyword_list:
        for i in seller_items:
            print(i)

        print("\nВведите 'уйти' чтобы уйти")
        seller_choose = input("Введите название товара для его покупки -> ")
        seller_choose = seller_choose.lower()

        while seller_choose not in seller_keyword_list:
            print("\nВведите 'уйти' чтобы уйти")
            seller_choose = input("НЕ СОВСЕМ ТЕбя понял, парень. ЧТОО? -> ")
            seller_choose = seller_choose.lower()


    if seller_choose == "медвежевика":
        print("\nЗАХОТЕЛОСЬ МЕДВЕжевики?\n")

        if characters_stats.character_coins >= medvejevika[1]:
            characters_stats.character_backpack.append("медвежевика")
            characters_stats.character_coins -= medvejevika[1]
            print("СПЕРВА 3 ЗОЛОТЫХ! ТЕПерь забирай...")

        elif characters_stats.character_coins < medvejevika[1]:
            print(code_library.no_coins)