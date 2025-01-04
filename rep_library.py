def beginning_scene_in_game(charname):
    print(input("Вы - " + charname + " отважный незнакомец, искатель приключений, который желает\n"
                                     "завоевать сердце прекрасной принцессы, придётся заморать руки, чтобы сделать это, ведь...\n"
                                     "Ужасный странно-череповатый дракон хочет сжечь принцессу до тла, чтобы получить золото всего королевства!\n"
                                     "Больше нет времени, нужно выдвигаться в путь..."))

beginning = ("\nПриветствую тебя незнакомец,\n"
             "эта игра создана специально для тебя. \n"
             "Для полного погружения в мою игру, \n"
             "советую тебе включить на фон плейлист Dark Fantasy. \n"
             "Приятной игры...  (Нажмите 'Enter')")

next_page = "Справка: чтобы переходить к следующему диалогу, просто нажмите 'Enter' "

reference_in_beginning = ("Чтобы открыть справку, введите команду 'Справка' в любой момент кроме диалогов.\n"
                          "В меню справки много полезной информации по игре.")

act_1 = ("Вы вышли из дома, с этого момента и началось ваше путешествие...\n"
         "Акт 1: Рождение воина")

def act_2_beginning():
    print(input("\nВы ни в чём не сомневаясь покинули город, ступив на встречу своему страху и цели."))
    print(input("Акт 2: Навстречу страху."))

act_2_action_1 = ("Шагая вперёд, с каждым шагом всё больше слышались крики ужаса из города.\n"
                  "С каждым новым шагом вы всё лучше видели как дракон уже кружит вокруг башни принцессы,\n"
                  "иногда пуская огненные шарики в лучников.")

def act_2_action_2(name):
    print(input("Ну же, " + name + ", соберись! Кто остановит это, если не такой смелый идиот как т.."))
    print(input("В ночи повиднелся огромный глаз, с подобием ведьмачьей шляпы на нём."))
    print(input("Что за чёрт..?"))
    print(input("Глаз.. Огромный глаз в шляпе..."))
    print(input("В миг глаз уставился на меня"))
    print("Бежать / Стоять")

def act_2_choose_run():
    print(input("Вы кинулись прочь от глаза, проговаривая про себя..."))
    print(input("я не трус"))
    print(input("Я НЕ трус"))
    print(input("Я НЕ ТРУС"))
    print(input("В момент перед вами оказался глаз, огромный глаз!"))
    print(input("Вы упили на землю от вида невиданного ранее создания..."))
    print(input("'Человек! Испугался? Куда так рванул от меня?'"))
    print("Выберите номер ответа:\n"
          "1. Оставь меня, глаз!\n"
          "2. Какое тебе дело? Хочешь сразиться?!\n")

def act_2_choose_run_2(max_hp, min_dmg, max_dmg):
    print(input("'Боишься, человек?'"))
    print(input("'Пару сотен лет назад я был таким же как ты..'"))
    print(input("'Я просил о помощи, но мне никто не помогал'"))
    print(input("'Я был так жалок...'"))
    print(input("'Прими силы чести от меня!'"))
    print(input("Честь глаза стала наполнять ваше тело силой!"))
    print(input("Через пару секунд глаз исчез!"))
    print(input("Вы остались один со своим рюкзаком, который в придачу стал тяжелее!"))
    print(input("В рюкзаке вы обнаружили две печеньерки. Какая щедрость!"))
    print(input("Макс. здоровье - " + f"{max_hp}" + "   Урон - от " + f"{min_dmg}" + "  до " + f"{max_dmg}"))
    print(input("Спасибо тебе, глаз. Я этого не забуду!"))

def act_2_choose_stay():
    print(input("Глаз медленно подлетел и, осмотрев меня со всех сторон, сказал:"))
    print(input("'Человек, вижу ты спешишь, к чему такая спешка?'"))
    print("Выберите номер ответа:\n"
     "1. Привет глаз. Спешу вон в ту башню, где кружит дракон.\n"
     "2. Какое тебе дело? Хочешь сразиться?!\n")

def eye_answer_1():
    print(input("В ту башню.. Я погляжу, ты смелый малый."))
    print(input("Как раз для смельчаков вроде тебя у меня есть предложение..."))
    print(input("Я заберу у тебя здоровье, но дам тебе силы...\n"
                "Или же наоборот, возьму силы и дам здоровья, м?"))

eye_question_1 = ("1. -30 от макс. здоровья / +6 к урону\n"
                  "2. -6 урона / +30 к макс. здоровью\n"
                  "3. Прекратить сделку и идти дальше.")

def eye_question_choose_dmg(max_hp, min_dmg, max_dmg):
    print(input("\n'Сделка заключена, ПО ГЛАЗАМ!'"))
    print(input("Засияв, глаз мнгновенно исчез, оставив меня одного."))
    print(input("Чувствую небольшую слабость в теле, но прилив сил к рукам!"))
    print(input("Макс. здоровье - " + f"{max_hp}" + "   Урон - от " + f"{min_dmg}" + "  до " + f"{max_dmg}"))

def eye_question_choose_hp(max_hp, min_dmg, max_dmg):
    print(input("\n'Сделка заключена, ПО ГЛАЗАМ!'"))
    print(input("Засияв, глаз мнгновенно исчез, оставив меня одного."))
    print(input("Чувствую небольшую слабость в руках, но прилив сил к телу!"))
    print(input("Макс. здоровье - " + f"{max_hp}" + "   Урон - от " + f"{min_dmg}" + "  до " + f"{max_dmg}"))

def eye_question_choose_quit():
    print(input("\n'Эй! Как ты смеешь вот так уходить?'"))
    print(input("Посмотрев назад вы видете, что глаз исчез"))
    print(input("Рюкзак потяжелел..."))
    print(input("'Что за чёрт?'"))
    print(input("Открыв рюкзак вы видите из ниоткуда появившиеся ягоды медвежевики."))
    print(input("'Видимо глаз был хорошим парнем...'"))
    print(input("Спасибо тебе."))


def eye_answer_2():
    print(input("'Сразиться? Тебе? Со мной?'"))
    print(input("'Не смеши мои каппиляры, идиот!'"))
    print(input("Я ТЕБЯ ИСПЕПЕЛЮ!"))
    print(input("* Если одержу победу над этим гляделой, тогда заполучу ячейку крепкости 3... *"))

def eye_fight_run():
    print(input("Вы развили скорость подобную скорости бегущей лошади..."))
    print(input("Вы сбежали от глаза!"))
    print(input("'БЕГИ, БЕГИ!'"))
    print(input("'ТРУС!'"))
    print(input("САМ ТРУС!"))
    print(input("Вы ругались с глазом ещё 2 минуты, пока он не пропал из вида."))
    print(input("Я не трус.."))
    print(input("Я НЕ ТРУС!"))



home_page = "\nВы вошли в свой дом. 'Здравствуй, дом!'."

seller_page = "\nВы прибыли к торговцу. Он осмотрел вас со словами: 'Да, выглядишь не очень... Есть парочка товаров которые могут исправить это!'.\n"

forest_page = "\nВы прибыли в лес."

def act_2_recomendations():
    print(input("\nВы уверены что хотите идти к замку?\nРЕКОМЕНДОВАННЫЙ уровень персонажа -> 5"))
    print("Идти / Остаться")

def act_2_end(name):
    print(input("\nВы прошли это чёртово место."))
    print(input("Вы обрели решимость, которой будет достаточно, чтобы зайти в замок."))
    print(input("Вы идёте под ливнем думая о том, что скоро всё кончится."))
    print(input("ВПЕРЁД, " + name + ", ВПЕРЁД, К СВОЕЙ ЦЕЛИ!"))



fight_choose = "Выберите действие: удар / инвентарь / бег\n"

# гаргулья
rep_forest_fight_1 = "\nКажется там что-то в кустах... 'на вас вылетела огромная гаргулья!' \nВ доле секунды вы думаете что сделать..."
rep_forest_fight_end_1 = "Вы сражались с гаргулией и страхом одновременно. Вы оказались сильнее, враг повержен...\n*lvl + 0.6*\n"
rep_forest_fight_coins_1 = "\nИз пасти гаргульи выпало 3 монеты, да уж, удачи тебе не занимать.\n + 3 монеты"

# кабан
rep_forest_fight_2 = "\nВы видите как на вашу тропинку вышел большой твердолобый кабан. \nНадо принять решение..."
rep_forest_fight_end_2 = "Вы убили кабана. Теперь можно и поживиться...\n*lvl + 0.4* \n*hp + 10*\n"
rep_forest_fight_coins_2 = "\nИз раны кабана выпали две монетки. Наверное он их когда-то съел...\n + 2 монеты"

# грибочек
rep_forest_fight_3 = "\nВы хотели пойти собрать грибов, как вдруг из под земли вылез разумный грибочек. \nВыглядит не очень то и опасным..."
rep_forest_fight_end_3 = "\nВы случайно убили гриб, наступив на него. А он мог бы стать добрым малым... \n*lvl + 0.2*\n"
rep_forest_fight_coins_3 = "\nПод шляпкой гриба виднеется золотая монета. Где он её нашёл?\n+ 1 монета"

rep_forest_fight_begin_eye = "\n'НАЧНЁМ ЖЕ!'"

def rep_forest_fight_end_eye():
    print(input("'ИДИОТ!'"))
    print(input("'ты'"))
    print(input("'пожалеешь...'"))
    print(input("..."))
    print(input("Покойся с тишиной."))
    print(input("Вы одолели глаз! Его оболочка испарилась превратившись в пепел."))
    print(input("Теперь вы обладатель Ячейки Крепкости Тела 3."))

# побег
rep_run = "Вы бежали с такой скоростью, что ни один великан бы не догнал вас!\nВы убежали с поля боя! \n*lvl - 0.3*\n"



reps = [rep_forest_fight_1, rep_forest_fight_2, rep_forest_fight_3]



seller_medvejevika = ["Медвежевика -> 'обычная ягода' -> лечит персонажа на 15 hp -> 3 золотых", "медвежевика",
                      "Сначала 3 золотых, парень.", "\nХм? медвежевика? Не проблема.\n", 3]

seller_pechenierka = ["Печеньерка -> 'хлебобулочное изделие' -> лечит персонажа на 30 hp -> 5 золотых", "печеньерка",
                      "Сначала 5 золотых, парень.", "\nЗахотелось моих печеньерок?\n", 5]

seller_sword_1 = ["Железный меч -> 'выкован руками торговца' -> увеличивает урон персонажа на 5 -> 8 золотых", "железный меч",
                  "Сперва 8 золотых!", "\nНужна обновка? Сейчас сделаю!\n", 8]

seller_cell_of_body_2 = ["Ячейка крепкости 2 -> 'медальон в виде сердца' -> увеличивает здоровье персонажа на 30 -> 10 золотых'", "ячейка крепкости 2",
                         "Сперва 10 золотых!", "\nАа, приглянулся медальончик?\n", 10]

bought_seller_sword_1 = "Взяв меч в руки, ты чувствуешь его тяжесть, чувствуешь что он - твой новый товарищ."

bought_cell_of_body_2 = ("Вы прикладываете ячейку к груди.. Через миг она исчезает.\n"
                            "Вы чувствуете твёрдость тела, которой не было раньше.")

seller_no_coins = "Здесь кажется не хватает, приходи как накопишь, парень...\n"



home_choose = "Отдохнуть / Снаряжение / Уйти"

reference_list = ["сюжет", "уровень", "инвентарь", "инв", "управление", "диалоги", "совет", "выйти"]

call_reference = ("\nСправка:\n"
                  "Чтобы войти в меню паузы введите 'пауза'.\n"
                  "Сюжет / Уровень / Инвентарь / Управление / Диалоги / Совет /// Выйти\n")

call_reference_suj = ("Сюжет: В игре всего _ концовки.\n"
                      "Чтобы выйти за пределы родного города - достигните 3 уровня персонажа.")

call_reference_lvl = ("Уровень: Уровень можно получать убивая существ в лесу.\n"
                      "За каждые 2 уровня урон персонажа увеличивается на 1.")

call_reference_inventory = ("Инвентарь: Инвентарь можно использовать в любом месте кроме диалогов.\n"
                            "При использовании инвентаря в бою, существо не будет атаковать вас.\n"
                            "В инвентарь попадают все вещи кроме предметов экипировки.")

call_reference_refs = ("Управление: Управлять персонажем нужно с помощью ввода команд с клавиатуры.\n"
                       "ВНИМАНИЕ: Существуют сокращения НЕКОТОРЫХ команд.\n"
                       "Пример: Инвентарь -> Инв; Торговец -> Торг ; И т. п.")

call_reference_dialogues = "Диалоги: Перемещение к след. диалогу осуществляется нажатием 'Enter'."

call_reference_advice = "Совет: Перед походом на Тропу, запаситесь выпечкой и ягодами у торговца."



act_3_beginning = "\nАкт 3: Судьба Незнакомца."

def act_3_action_1():
    print(input("Шаг за шагом."))
    print(input("Крик за криком."))
    print(input("Вы уже стоите у входа в башню."))
    print(input("На входе вас встретил перепуганный но с виду мощный охранник."))
    print(input("Его глаза уставились на вас."))
    print(input("'С-стой.. Куд-да прёшь?'"))
    print("Введите номер ответа:")
    print("1. Я тебе не враг, мне нужно к дракону!\n"
          "2. Если не освободишь дорогу - УБЬЮ...")
    inp = input("Что выбрать? >> ")

    while inp != "1" and inp != "2":
        inp = input("Что же выбрать? >> ")

    return inp

def act_3_action_1_choose_1():
    print(input("'АГА! Я-Я ВИЖУ Т-ТВОИ ЗМЕИНЫЕ ГЛАЗА!'"))
    print(input("'ТЫ ПРЕСПЕШНИК ЭТОГО Д-ДРАКОНА, Д-ДА?!'"))
    print(input("Вот чёрт. Парень то с ума сошёл..."))
    print(input("'Д-ДАВАЙ, НАПАДАЙ! Я ОТРУБЛЮ ТВОЮ З-ЗМЕИНУЮ ГОЛОВУ!'"))
    print(input("Ну что ж, ничего не поделаешь :)"))
    print(input("'ДАВАЙ!'\n"))

def act_3_action_1_choose_1_end():
    print(input("Вы победили стражника."))
    print(input("'ты...'"))
    print(input("'обычный парень..'"))
    print(input("'никакой не змей...'"))
    print(input("'защити..'"))
    print(input("'нашу...'"))
    print(input("'принцессу...'"))
    print(input("'...'"))
    print(input("Его смерть на моих руках.."))
    print(input("Он сам виноват."))
    print(input("..."))
    print(input("Покойся с миром."))

def act_3_action_1_choose_1_run():
    print(input("'УБЕГАЕШЬ, ДА?'"))
    print(input("'СТОЙ'"))
    print(input("'Я СНЕСУ ТЕБЕ ГОЛ...'"))
    print(input("..."))
    print(input("..."))
    print(input("Обернувшись, вы видете картину:"))
    print(input("Стражника сожгло шальным снарядом дракона!"))
    print(input("Да уж, не завидую я тебе..."))
    print(input("..."))
    print(input("Покойся с миром."))

def act_3_action_1_choose_2(min_dmg, max_dmg):
    print(input("'НЕ ПОДХОДИ!'"))
    print(input("'НЕ ТРОГАЙ МЕНЯ!'"))
    print(input("'ПОЩАДИ'"))
    print(input("Стражник так перепугался, что упал на колени."))
    print(input("Да-да, пропусти меня, ты.. жалкий.. червь?"))
    print(input("'П-ПРОХОДИТЕ...'"))
    print(input("И вообще, отдай мне свои меч!"))
    print(input("'З-ЗАБИРАЙТЕ...'"))
    print(input("Теперь вы обладатель Платинового меча"))
    print(input("Он всё равно ему не пригодится, раз уж он такой трусливый."))
    print(input("Базовый урон:   Мин. -> 16  /  Макс. -> 20"))
    print(input("Урон персонажа:   Макс. -> " + f"{min_dmg}" + "  /  Мин. -> " + f"{max_dmg}"))

def act_3_choose_stay():
    print(input("Глаз медленно подлетел и, осмотрев меня со всех сторон, сказал:"))
    print(input("'Человек, вижу ты спешишь, к чему такая спешка?'"))
    print("Выберите номер ответа:\n"
     "1. Привет глаз. Спешу вон в ту башню, где кружит дракон.\n"
     "2. Какое тебе дело? Хочешь сразиться?!\n")