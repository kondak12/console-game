import rep_library

import functions

import time

def use_seller():
    print(rep_library.seller_page)

    seller_items = [f"{rep_library.seller_medvejevika[0]}", f"{rep_library.seller_sword_1[0]}"]
    seller_keyword_list = ["медвежевика", "мед", "железный меч", "уйти", "инвентарь", "инв"]

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


    if seller_choose == "инвентарь" or seller_choose == "инв":

        functions.use_inventory()


    if seller_choose == "медвежевика" or seller_choose == "мед":

        functions.seller_choise(rep_library.seller_medvejevika[-1], rep_library.seller_medvejevika[1],
                                rep_library.seller_medvejevika[2], rep_library.seller_medvejevika[3])