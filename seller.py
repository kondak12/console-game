import characters_stats

import rep_library

import time

def use_seller():
    print(rep_library.seller_page)

    medvejevika_sell = 3
    sword_1_sell = 8

    seller_items = [f"{rep_library.seller_medvejevika}", f"{rep_library.seller_sword_1}"]
    seller_keyword_list = ["медвежевика", "железный меч", "уйти"]

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
            seller_choose = input("НЕ СОВСЕМ ТЕбя понял, парень. ЧТОО? -> ")
            seller_choose = seller_choose.lower()


    if seller_choose == "медвежевика" or seller_choose == "мед":
        print("\nЗАХОТЕЛОСЬ МЕДВЕжевики?\n")

        time.sleep(3)


        if characters_stats.character_coins >= medvejevika_sell:
            characters_stats.character_backpack.append("медвежевика")
            characters_stats.character_coins -= medvejevika_sell
            print("СПЕРВА 3 ЗОЛОТЫХ!")

            time.sleep(3)

            print("теперь заБИРАЙ...\n")

            time.sleep(2)


        elif characters_stats.character_coins < medvejevika_sell:
            print("СПЕРВА 3 ЗОЛОТЫХ!")

            time.sleep(3)

            print(rep_library.seller_no_coins)

            time.sleep(2)