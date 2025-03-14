import time
import msvcrt


def typing_effect(text, delay=0.02):
    for char in text:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b"r":
                break
        print(char, end = "",flush=True)
        time.sleep(delay)
    return ""



def beginning_scene_in_game(charname):
    input(typing_effect(f"\033[33mВы - {charname}\033[0m, отважный незнакомец, искатель приключений, который желает\n"
                                     "завоевать сердце прекрасной принцессы, придётся заморать руки, чтобы сделать это, ведь...\n"
                                     "\033[31mУжасный странно-череповатый дракон\033[0m хочет сжечь \033[35mпринцессу \033[31mдо тла, чтобы получить золото всего королевства!\n"
                                     "Больше нет времени, нужно выдвигаться в путь...\033[0m"))

art = ("\033[33m░█▀▀▄ █▀▀█ █▀▀█ █─█    ░█▀▀▄ █▀▀█ █▀▀█ █▀▀▀ █▀▀█ █▀▀▄\n"
         "░█─░█ █▄▄█ █▄▄▀ █▀▄    ░█─░█ █▄▄▀ █▄▄█ █─▀█ █──█ █──█\n"
         "░█▄▄▀ ▀──▀ ▀─▀▀ ▀─▀    ░█▄▄▀ ▀─▀▀ ▀──▀ ▀▀▀▀ ▀▀▀▀ ▀──▀\n\n"
         " \033[35m       █▀▀ █▀▀█ █▀▀▄ ▀▀█▀▀ █▀▀█ █▀▀ █──█\n"
         "        █▀▀ █▄▄█ █──█  ─█─  █▄▄█ ▀▀█ █▄▄█\n"
         "        ▀   ▀  ▀ ▀  ▀   ▀   ▀  ▀ ▀▀▀ ▄▄▄█\033[0m")

beginning = ("\nПриветствую тебя незнакомец,\n"
             "эта игра создана специально для \033[31mтебя\033[0m. \n"
             "Для полного погружения в мою игру, \n"
             "советую тебе включить на фон плейлист Dark Fantasy. \n"
             "Приятной игры...  \033[32m(Нажмите 'Enter')\033[33m")

recomendation = "Чтобы пройти 1 акт игры достаточно получить 3 уровень персонажа и уйти из деревни."

next_page = "\033[33mСправка: чтобы переходить к следующему диалогу, просто нажмите 'Enter'\033[0m"

reference_in_beginning = ("\033[31mРЕКОМЕНДУЕТСЯ: \033[33mЧтобы открыть справку, введите команду 'Справка' в любой момент кроме диалогов.\n"
                          "\033[31mРЕКОМЕНДУЕТСЯ: \033[33mВ меню справки много полезной информации по игре.\033[0m")

act_1 = ("Вы вышли из дома, с этого момента и началось ваше путешествие...\n"
         "\033[35mАкт 1: Рождение воина\033[0m")

def act_2_beginning():
    input(typing_effect("\nВы ни в чём не сомневаясь покинули город, ступив на встречу своему страху и цели."))
    print(input("\033[35mАкт 2: Навстречу страху.\033[0m"))

act_2_action_1 = ("Шагая вперёд, с каждым шагом всё больше слышались крики ужаса из города.\n"
                  "С каждым новым шагом вы всё лучше видели как \033[31mдракон\033[0m уже кружит вокруг башни принцессы,\n"
                  "иногда пуская огненные шарики в лучников.")

def act_2_action_2(name):
    input(typing_effect("\033[36mНу же, " + name + ", соберись!\033[0m Кто остановит это, если не такой смелый идиот как т.."))
    input(typing_effect("В ночи повиднелся огромный глаз, с подобием ведьмачьей шляпы на нём."))
    input(typing_effect("Что за чёрт..?"))
    input(typing_effect("\033[34mГлаз..\033[0m Огромный глаз в шляпе..."))
    input(typing_effect("\033[31mВ миг глаз уставился на меня\033[0m"))
    print("1 \033[31mБежать\033[0m / 2 \033[34mСтоять\033[0m")

def act_2_choose_run():
    input(typing_effect("Вы кинулись прочь от глаза, проговаривая про себя..."))
    input(typing_effect("я не трус"))
    input(typing_effect("\033[31mЯ НЕ\033[0m трус"))
    input(typing_effect("\033[31mЯ НЕ ТРУС\033[0m"))
    input(typing_effect("В момент перед вами оказался глаз, огромный глаз!"))
    input(typing_effect("Вы упили на землю от вида невиданного ранее создания..."))
    input(typing_effect("'Человек! \033[36mИспугался?\033[0m Куда так рванул от меня?'"))
    print("Выберите номер ответа:\n"
          "1. \033[34mОставь меня, глаз!\033[0m\n"
          "2. \033[31mКакое тебе дело? Хочешь сразиться?!\033[0m\n")

def act_2_choose_run_2(max_hp, min_dmg, max_dmg):
    input(typing_effect("'Боишься, человек?'"))
    input(typing_effect("'Пару сотен лет назад я был таким же как ты..'"))
    input(typing_effect("'Я просил о помощи, но мне никто не помогал'"))
    input(typing_effect("'Я был так жалок...'"))
    input(typing_effect("'Прими силы чести от меня!'"))
    input(typing_effect("Честь глаза стала наполнять ваше тело силой!"))
    input(typing_effect("Через пару секунд глаз исчез!"))
    input(typing_effect("Вы остались один со своим рюкзаком, который в придачу стал тяжелее!"))
    input(typing_effect("В рюкзаке вы обнаружили две печеньерки. Какая щедрость!"))
    input(typing_effect("\033[32mМакс. здоровье - " + f"{max_hp}" + "   Урон - от " + f"{min_dmg}" + "  до " + f"{max_dmg}\033[0m"))
    input(typing_effect("Спасибо тебе, глаз. Я этого не забуду!"))

def act_2_choose_stay():
    input(typing_effect("Глаз медленно подлетел и, осмотрев меня со всех сторон, сказал:"))
    input(typing_effect("'Человек, вижу ты спешишь, к чему такая спешка?'"))
    print("Выберите номер ответа:\n"
     "1. \033[34mПривет глаз. Спешу вон в ту башню, где кружит дракон.\033[0m\n"
     "2. \033[31mКакое тебе дело? Хочешь сразиться?!\033[31m\n")

def eye_answer_1():
    input(typing_effect("В ту башню.. Я погляжу, ты смелый малый."))
    input(typing_effect("Как раз для смельчаков вроде тебя у меня есть предложение..."))
    input(typing_effect("Я заберу у тебя здоровье, но дам тебе силы...\n"
                "Или же наоборот, возьму силы и дам здоровья, м?"))

eye_question_1 = ("1. \033[31m-30 от макс. здоровья\033[0m / \033[32m+6 к урону\033[0m\n"
                  "2. \033[31m-6 урона\033[0m / \033[32m+30 к макс. здоровью\033[0m\n"
                  "3. \033[34mПрекратить сделку и идти дальше.\033[0m")

def eye_question_choose_dmg(max_hp, min_dmg, max_dmg):
    input(typing_effect("\n'Сделка заключена, \033[31mПО ГЛАЗАМ!\033[0m'"))
    input(typing_effect("Засияв, глаз мнгновенно исчез, оставив меня одного."))
    input(typing_effect("Чувствую небольшую слабость в теле, но прилив сил к рукам!"))
    input(typing_effect("\033[32mМакс. здоровье - " + f"{max_hp}" + "   Урон - от " + f"{min_dmg}" + "  до " + f"{max_dmg}\033[0m"))

def eye_question_choose_hp(max_hp, min_dmg, max_dmg):
    input(typing_effect("\n'Сделка заключена, \033[31mПО ГЛАЗАМ!\033[0m'"))
    input(typing_effect("Засияв, глаз мнгновенно исчез, оставив меня одного."))
    input(typing_effect("Чувствую небольшую слабость в руках, но прилив сил к телу!"))
    input(typing_effect("\033[32mМакс. здоровье - " + f"{max_hp}" + "   Урон - от " + f"{min_dmg}" + "  до " + f"{max_dmg}\033[0m"))

def eye_question_choose_quit():
    input(typing_effect("\n'Эй! Как ты смеешь вот так уходить?'"))
    input(typing_effect("Посмотрев назад вы видете, что глаз исчез"))
    input(typing_effect("Рюкзак потяжелел..."))
    input(typing_effect("'Что за чёрт?'"))
    input(typing_effect("Открыв рюкзак вы видите из ниоткуда появившиеся ягоды медвежевики."))
    input(typing_effect("'Видимо глаз был хорошим парнем...'"))
    input(typing_effect("\033[32mСпасибо тебе.\033[0m"))


def eye_answer_2():
    input(typing_effect("'Сразиться? Тебе? Со мной?'"))
    input(typing_effect("'Не смеши мои каппиляры, идиот!'"))
    input(typing_effect("\033[31mЯ ТЕБЯ ИСПЕПЕЛЮ!\033[0m"))
    input(typing_effect("\033[33m* Если одержу победу над этим гляделой, тогда заполучу ячейку крепкости 3... *\033[0m"))

def eye_fight_run():
    input(typing_effect("Вы развили скорость подобную скорости бегущей лошади..."))
    input(typing_effect("\033[31mВы сбежали от глаза!\033[0m"))
    input(typing_effect("'БЕГИ, БЕГИ!'"))
    input(typing_effect("\033[31m'ТРУС!'\033[0m"))
    input(typing_effect("\033[32mСАМ ТРУС!\033[0m"))
    input(typing_effect("Вы ругались с глазом ещё 2 минуты, пока он не пропал из вида."))
    input(typing_effect("Я не трус.."))
    input(typing_effect("\033[35mЯ НЕ ТРУС!\033[0m"))



home_page = "\nВы вошли в свой дом. \033[32m'Здравствуй, дом!'\033[0m."

seller_page = "\n\033[33mВы прибыли к торговцу.\033[0m Он осмотрел вас со словами: \033[33m'Да, выглядишь не очень... Есть парочка товаров которые могут исправить это!'.\033[0m\n"

forest_page = "\n\033[32mВы прибыли в лес.\033[0m"

def act_2_recomendations():
    input(typing_effect("\n\033[33mВы уверены что хотите идти к замку?\033[0m\n\033[32mРЕКОМЕНДОВАННЫЙ\033[0m уровень персонажа -> 5"))
    print("1 \033[32mИдти\033[0m / 2 \033[35mОстаться\033[0m")

def act_2_end(name):
    input(typing_effect("\nВы прошли это чёртово место."))
    input(typing_effect("Вы обрели решимость, которой будет достаточно, чтобы зайти в замок."))
    input(typing_effect("Вы идёте под ливнем думая о том, что скоро всё кончится."))
    input(typing_effect("\033[31mВПЕРЁД, " + name + ", ВПЕРЁД, К СВОЕЙ ЦЕЛИ!\033[0m"))



fight_choose = "Выберите действие: \033[32m1 удар\033[0m / \033[36m2 инвентарь\033[0m / \033[31m3 бег\033[0m\n"

# гаргулья
rep_forest_fight_1 = "\nКажется там что-то в кустах... \033[33m'на вас вылетела огромная гаргулья!'\033[0m \nВ доле секунды вы думаете что сделать..."
rep_forest_fight_end_1 = "Вы сражались с гаргулией и страхом одновременно. \033[33mВы оказались сильнее\033[0m, враг повержен...\n*lvl + 0.6*\n"
rep_forest_fight_coins_1 = "\nИз пасти гаргульи выпало \033[33m3 монеты\033[0m, да уж, удачи тебе не занимать.\n \033[32m+ 3 монеты\033[0m"

# кабан
rep_forest_fight_2 = "\n\033[33mВы видите как на вашу тропинку вышел большой твердолобый кабан.\033[0m \nНадо принять решение..."
rep_forest_fight_end_2 = "Вы убили кабана. Теперь можно и поживиться...\n\033[32m*lvl + 0.4* \n*hp + 10*\033[0m\n"
rep_forest_fight_coins_2 = "\nИз раны кабана выпали \033[33mдве монетки\033[0m. Наверное он их когда-то съел...\n \033[33m+ 2 монеты\033[0m"

# грибочек
rep_forest_fight_3 = "\nВы хотели пойти собрать грибов, \033[33mкак вдруг из под земли вылез разумный грибочек.\033[0m \nВыглядит не очень то и опасным..."
rep_forest_fight_end_3 = "\n\033[33mВы случайно убили гриб\033[0m, наступив на него. А он мог бы стать добрым малым... \n\033[32m*lvl + 0.2*\033[0m\n"
rep_forest_fight_coins_3 = "\nПод шляпкой гриба виднеется \033[33mзолотая монета\033[0m. Где он её нашёл?\n\033[32m+ 1 монета\033[0m"

rep_forest_fight_begin_eye = "\n\033[32m'НАЧНЁМ ЖЕ!'\033[0m"

def rep_forest_fight_end_eye():
    input(typing_effect("\033[32m'ИДИОТ!'\033[0m"))
    input(typing_effect("'ты'"))
    input(typing_effect("'пожалеешь...'"))
    input(typing_effect("..."))
    input(typing_effect("Покойся с тишиной."))
    input(typing_effect("\033[33mВы одолели глаз!\033[0m Его оболочка испарилась превратившись в пепел."))
    input(typing_effect("\033[32mТеперь вы обладатель Ячейки Крепкости Тела 3.\033[0m"))


rep_run = "Вы бежали с такой скоростью, что ни один великан бы не догнал вас!\n\033[33mВы убежали с поля боя!\033[0m \n\033[31m*lvl - 0.3*\033[33m\n"   # побег


reps = [rep_forest_fight_1, rep_forest_fight_2, rep_forest_fight_3]



seller_medvejevika = ["1 \033[32mМедвежевика\033[0m -> 'обычная ягода' -> лечит персонажа на 15 hp -> 3 золотых", "медвежевика",
                      "Сначала 3 золотых, парень.", "\nХм? медвежевика? Не проблема.\n", 3]

seller_pechenierka = ["2 \033[32mПеченьерка\033[0m -> 'хлебобулочное изделие' -> лечит персонажа на 30 hp -> 5 золотых", "печеньерка",
                      "Сначала 5 золотых, парень.", "\nЗахотелось моих печеньерок?\n", 5]

seller_sword = ["3 \033[36mЖелезный меч\033[0m -> 'выкован руками торговца' -> увеличивает урон персонажа на 5 -> 8 золотых", "железный меч",
                  "Сперва 8 золотых!", "\nНужна обновка? Сейчас сделаю!\n", 8]

seller_cell_of_body_2 = ["4 \033[36mЯчейка крепкости тела 2\033[0m -> 'медальон в виде сердца' -> увеличивает здоровье персонажа на 30 -> 10 золотых'", "ячейка крепкости тела 2",
                         "Сперва 10 золотых!", "\nАа, приглянулся медальончик?\n", 10]

bought_seller_sword = "Взяв меч в руки, ты чувствуешь его тяжесть, чувствуешь что \033[33mон - твой новый товарищ.\033[0m"

bought_cell_of_body_2 = ("Вы прикладываете ячейку к груди.. Через миг она исчезает.\n"
                            "\033[33mВы чувствуете твёрдость тела, которой не было раньше.\033[0m")

seller_no_coins = "\033[33mЗдесь кажется не хватает, приходи как накопишь, парень...\033[0m\n"



home_choose = "1 \033[32mОтдохнуть\033[0m / 2 \033[36mСнаряжение\033[0m / 3 \033[31mУйти\033[0m"

reference_list = ["1", "2", "3", "4", "5", "6", "7"]

call_reference = ("\n\033[32mСправка:\033[0m\n"
                  "1 Сюжет / 2 Уровень / 3 Инвентарь / 4 Управление / 5 Диалоги / 6 \033[33mСовет\033[0m /// 7 Выйти\n")

call_reference_suj = ("\033[33mСюжет\033[0m: В игре всего _ концовки.\n"
                      "Чтобы выйти за пределы родного города - достигните 3 уровня персонажа и введите 'тропа' во время выбора пути.")

call_reference_lvl = ("\033[33mУровень\033[0m: Уровень можно получать убивая существ в лесу.\n"
                      "За каждые 2 уровня урон персонажа увеличивается на 1.")

call_reference_inventory = ("\033[33mИнвентарь\033[0m: Инвентарь можно использовать в любом месте кроме диалогов.\n"
                            "При использовании инвентаря в бою, существо не будет атаковать вас.\n"
                            "В инвентарь попадают все вещи кроме предметов экипировки.")

call_reference_refs = ("\033[33mУправление\033[0m: Управлять персонажем \033[31mВ ОСНОВНОМ\033[0m нужно с помощью ввода номеров команд с клавиатуры.\n"
                       "\033[31mВНИМАНИЕ\033[0m: Существуют сокращения НЕКОТОРЫХ команд.\n"
                       "Пример: Медвежевика -> мед; Печеньерка -> печ; И т. п.")

call_reference_dialogues = "\033[33mДиалоги\033[0m: Перемещение к след. диалогу осуществляется нажатием 'Enter', либо игрой самостоятельно."

call_reference_advice = "\033[33mСовет\033[0m: Перед походом на Тропу, запаситесь выпечкой и ягодами у торговца."



act_3_beginning = "\n\033[35mАкт 3: Судьба Незнакомца.\033[0m"

def act_3_action_1():
    input(typing_effect("Шаг за шагом."))
    input(typing_effect("Крик за криком."))
    input(typing_effect("Вы уже стоите у входа в башню."))
    input(typing_effect("На входе вас встретил перепуганный но с виду мощный охранник."))
    input(typing_effect("Его глаза уставились на вас."))
    input(typing_effect("\033[36m'С-стой.. Куд-да прёшь?'\033[0m"))
    print("Введите номер ответа:\n1. \033[32mЯ тебе не враг\033[0m, мне нужно к дракону!\n"
          "2. Если не освободишь дорогу - \033[31mУБЬЮ...\033[0m")
    inp = input("Что выбрать? >> ")

    while inp != "1" and inp != "2":
        inp = input("Что же выбрать? >> ")

    return inp

def act_3_action_1_choose_1():
    input(typing_effect("\033[31m'АГА! Я-Я ВИЖУ Т-ТВОИ ЗМЕИНЫЕ ГЛАЗА!'\033[31m"))
    input(typing_effect("'ТЫ ПРЕСПЕШНИК ЭТОГО Д-ДРАКОНА, Д-ДА?!'"))
    input(typing_effect("Вот чёрт. Парень то с ума сошёл..."))
    input(typing_effect("\033[31m'Д-ДАВАЙ, НАПАДАЙ!\033[0m Я ОТРУБЛЮ ТВОЮ З-ЗМЕИНУЮ ГОЛОВУ!'"))
    input(typing_effect("Ну что ж, ничего не поделаешь \033[33m:)\033[0m"))
    input(typing_effect("\033[31m'ДАВАЙ!'\033[0m\n"))

def act_3_action_1_choose_1_end():
    input(typing_effect("Вы победили стражника."))
    input(typing_effect("'ты...'"))
    input(typing_effect("'обычный парень..'"))
    input(typing_effect("\033[32m'никакой не змей...'\033[0m"))
    input(typing_effect("'защити..'"))
    input(typing_effect("'нашу...'"))
    input(typing_effect("'принцессу...'"))
    input(typing_effect("'...'"))
    input(typing_effect("Его смерть на моих руках.."))
    input(typing_effect("Он сам виноват."))
    input(typing_effect("..."))
    input(typing_effect("\033[32mПокойся с миром.\033[0m"))

def act_3_action_1_choose_1_run():
    input(typing_effect("\033[32m'УБЕГАЕШЬ, ДА?'\033[0m"))
    input(typing_effect("\033[32m'СТОЙ'\033[0m"))
    input(typing_effect("\033[32m'Я СНЕСУ ТЕБЕ ГОЛ...\033[0m'"))
    input(typing_effect("\033[32m...\033[0m"))
    input(typing_effect("..."))
    input(typing_effect("Обернувшись, вы видете картину:"))
    input(typing_effect("Стражника сожгло шальным снарядом дракона!"))
    input(typing_effect("Да уж, не завидую я тебе..."))
    input(typing_effect("..."))
    input(typing_effect("\033[32mПокойся с миром.\033[0m"))

def act_3_action_1_choose_2(min_dmg, max_dmg):
    input(typing_effect("\033[34m'НЕ ПОДХОДИ!'\033[0m"))
    input(typing_effect("'НЕ ТРОГАЙ МЕНЯ!'"))
    input(typing_effect("\033[32m'ПОЩАДИ'\033[0m"))
    input(typing_effect("Стражник так перепугался, что упал на колени."))
    input(typing_effect("Да-да, пропусти меня, ты.. жалкий.. червь?"))
    input(typing_effect("'П-ПРОХОДИТЕ...'"))
    input(typing_effect("И вообще, отдай мне свои меч!"))
    input(typing_effect("\033[32m'З-ЗАБИРАЙТЕ...'\033[0m"))
    input(typing_effect("\033[33mТеперь вы обладатель Платинового меча\033[0m"))
    input(typing_effect("Он всё равно ему не пригодится, раз уж он такой \033[34mтрусливый\033[0m."))
    input(typing_effect("\033[32mБазовый урон:   Мин. -> 16  /  Макс. -> 20\033[0m"))
    input(typing_effect("\033[33mУрон персонажа:   Мин. -> " + f"{min_dmg}" + "  /  Макс. -> " + f"{max_dmg}\033[0m"))

def act_3_action_2():
    input(typing_effect("Ступень за ступенью"))
    input(typing_effect("Наверху уже слышно, как дракон, разгромив верхушку замка, сел на лапы..."))
    input(typing_effect("Ужасный хриплый голос проговорил:"))
    input(typing_effect("\033[31m'Прр-ринцес-са, договорр-римс-ся же по мирр-рному?'\033[0m"))
    input(typing_effect("Принцесса таила молчание, будто, ожидала спасения.."))
    input(typing_effect("\033[31m'Не бойсс-ся, ты ведь такая нежж-жная.'\033[0m"))
    input(typing_effect("\033[31m'Подобным тебе девушш-шкам нельзя нерр-рвничать.'\033[0m"))
    input(typing_effect("Вы выбегаете на разгромленную крышу и видите огромного изумрудного дракона."))
    input(typing_effect("Он настолько огромен, что сравнялся бы с 1/3 от размера замка."))
    input(typing_effect("Боже..."))
    input(typing_effect("Как же ты огромен.."))
    input(typing_effect("Как я вообще буду с тобой биться?"))
    input(typing_effect("Дракон повернул голову в вашу сторону..."))
    input(typing_effect("\033[31m'Ты...'\033[0m"))
    input(typing_effect("\033[31m'Мелочч-чь...'\033[0m"))
    input(typing_effect("\033[31m'Играешш-шь в героя?'\033[0m"))
    print("1. \033[31mЧешуйчатый, почему бы тебе не отпустить ту даму и сразиться со мной без лиШ-ШШних слов?\033[0m\n"
          "2. \033[32mНет, я пришёл объеденить с тобой силы.\033[0m")
    inp = input("Что выбрать? >> ")

    while inp != "1" and inp != "2":
        inp = input("Что же выбрать? >> ")

    return inp

def act_3_action_2_choose_1_phase_1(name):
    input(typing_effect("\033[31m'ММ-МЕЛОЧЧ-ЧЬ!'\033[0m"))
    input(typing_effect("\033[31m'Я ЗНАЮ ТВОЁ ИМЯ, " + f"{name}" + "'\033[0m"))
    input(typing_effect("\033[31m'СС-СОЖГУ ДО ТЛА!'\033[0m"))
    input(typing_effect("\033[31m'ИСС-СПЕПЕЛЮ ДО КОСС-СТЕЙ!'\033[0m"))
    input(typing_effect("Давай, змей..."))
    input(typing_effect("\033[33mНАПАДАЙ!\033[0m"))

princess_help_phrase = ("\033[32mВы видете как к вам подкатились 3 медвежевики.\033[0m\n"
                        "Посмотрев за дракона, вы видете, что их кинула вам \033[35mпринцесса\033[0m.\n"
                        "* шёпотом *   \033[33mспасибо!\033[0m")

def dragon_phrase_1(dmg):
    r = "Дракон кружит над вами и швыряет в вас огненный шарик. \033[31mОн нанёс " + f"{dmg}" + " урона\033[0m."
    return f"{r}"

def dragon_phrase_2(dmg):
    r = "Дракон ударил вас когтем.\033[31m Он нанёс " +  f"{dmg}" +  " урона\033[0m."
    return f"{r}"

def dragon_phrase_3(dmg):
    r = "Дракон смахнул вас крылом в обломки крыши.\033[31m Он нанёс " + f"{dmg}" + " урона\033[0m."
    return f"{r}"

def act_3_action_2_choose_1_phase_2_1():
    input(typing_effect("\033[31m'МммММ-МЕЛОЧчЧЧ-ЧЬ!'\033[0m"))
    input(typing_effect("\033[34m'Арр-ргх...'\033[0m"))
    input(typing_effect("\033[34m'Подобные тебе вв-воины, что сс-смогли одолеть меня нужж-жны мне.'\033[0m"))
    input(typing_effect("\033[34m'Осс-ставь меня и я сс-сделаю для тебя вс-сё что зз-захочешш-шь!'\033[0m"))
    choose = input("1. \033[32mПрисоединиться к дракону\033[0m\n"
                   "2. \033[31mУбить дракона\033[0m\n"
                   "Введите номер ответа -> ")
    while choose != "1" and choose != "2":
        choose = input("Повторите ввод -> ")

    return choose

def act_3_action_2_choose_1_phase_2_2():
    input(typing_effect("\033[31m'ГР-РР-РЯЗЗ-ЗЬ!'\033[0m"))
    input(typing_effect("\033[31m'Я ПРр-РИКОНЧУ ТЕБЯ!'\033[0m"))
    input(typing_effect("Дракон поменял свой оттенок и стал \033[31mчёрного цвета\033[0m.."))
    input(typing_effect("Чёрт, не к добру это.."))
    input(typing_effect("\033[31m'НАПАДАЙ МЕЛОЧЧ-ЧЬ'\033[0m"))


def win_dragon():
    input(typing_effect("\033[31m'АРГХ-ХХхх...'\033[0m", 0.05))
    input(typing_effect("\033[31m'ТЫыы...'\033[0m", 0.07))
    input(typing_effect("\033[31m'Мелоч-чь..'\033[0m", 0.07))
    input(typing_effect("\033[31m'победил..'\033[0m", 0.07))
    input(typing_effect("\033[31m'не смей дажж-же думать о моей с-ссмерти...'\033[0m", 0.07))
    input(typing_effect("Окрававленный дракон встал на задние лапы."))
    input(typing_effect("Взмахнул крыльями!"))
    input(typing_effect("И полетел!"))
    input(typing_effect("\033[31m.....\033[0m", 0.08))
    input(typing_effect("Но упал вниз, крича:"))
    input(typing_effect("\033[31m'ЖЖ-ЖИВИ СВОЮ Ж-ЖАЛКУЮ ЖИЗНЬ!'\033[0m", 0.07))
    input(typing_effect("\033[31m'ЦЦ-ЦЕПЛЯЯСЬ ЗА КАЖЖ-ЖДУЮ ПЕСЧ-ЧЧИНКУ!'\033[0m", 0.07))
    input(typing_effect(".....", 0.08))
    input(typing_effect("Дракон умер, потому что не смог взететь."))
    input(typing_effect("\033[32mВы победили!\033[0m", 0.07))
    input(typing_effect(".....", 0.07))
    input(typing_effect("После этого дня, всё королевство знало ваше имя."))
    input(typing_effect("А вы с принцессой стали парой на всю оставшуюся жизнь."))
    input(typing_effect("Эту историю вы ещё долго рассказывали своим детям."))
    input(typing_effect("Потом внукам."))
    input(typing_effect("Так и прожив счастливую жинь."))
    input(typing_effect("\033[32mКонец\033[0m!", 0.08))

def mid_ending(name):
    input(typing_effect("\033[31m'Не уж-жж то действительно ты пришёл сюда з-за этим?'\033[0m"))
    input(typing_effect(f"\033[31m'Ты будешш-шь моим любимчч-чиком, {name}'\033[0m"))
    input(typing_effect(f"\033[36m'НЕТ, {name}! КАК ТЫ МОЖЕШЬ!'\033[0m"))
    input(typing_effect("\033[36m'ЗА ЧТО ТЫ ПРЕДАЛ ВСЕХ ЛЮДЕЙ КОРОЛЕВСТВА?'\033[0m"))
    input(typing_effect("\033[36m'они все надеялись на тебя...'\033[0m"))
    input(typing_effect(f"\033[31m'Да ужж-ж, {name}, ты станешь королём рабов в моём подзз-земелье!'\033[0m"))
    input(typing_effect("\033[31m'Навсс-сегда.'\033[0m"))
    input(typing_effect("После вашей резкой измены, дракон \033[31mсожрал\033[0m принцессу."))
    input(typing_effect("\033[31mСпалил всё королевство.\033[0m"))
    input(typing_effect("А вы до конца своих человеческих дней были главой рабов в его пещере."))
    input(typing_effect("Когда вам исполнилось 97 лет, вы начали покрываться чешуёй и через ещё 68 лет стали драконоподобным."))
    input(typing_effect("Ушли от дракона."))
    input(typing_effect("И остальные 400 лет жизни жили в горах."))
    input(typing_effect("\033[33mКонец.\033[0m"))


def death_ending(name):
    input(typing_effect("\033[31m'ТЫ УМЕРР-Р И О ТЕБЕ НИКТО НЕ ВСС-СПОМНИТ'\033[0m"))
    input(typing_effect("\033[31m'ТЫ ВСЁ ТА ЖЖ-ЖЕ МЕЛОЧЧ-ЧЬ!'\033[0m"))
    input(typing_effect("\033[31m'ПЕРЕДАЙ ПРИВВ-ВЕТ МОИМ ВРАГАМ!'\033[0m"))
    input(typing_effect(f"\033[33m{name}, ты действительно умер.\033[0m"))
    input(typing_effect("Стража сдалась сразу"))
    input(typing_effect("\033[31mДракон испепелил весь город, забрал все богатства и принцессу в горы\033[0m"))
    input(typing_effect("\033[31mЭто конец.\033[0m"))

sword_1 = "деревянный меч"
sword_2 = "железный меч"
sword_3 = "платиновый меч"

cell_of_body_1 = "ячейка крепкости тела 1"
cell_of_body_2 = "ячейка крепкости тела 2"
cell_of_body_3 = "ячейка крепкости тела 3"