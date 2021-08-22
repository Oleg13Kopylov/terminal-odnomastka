import random


class Game:
    cards_set0 = set()
    cards_set1 = set()
    cards_list0 = list()
    cards_list1 = list()
    combined_cards = list()
    k = -1
    card_on_table0 = -1
    card_on_table1 = -1
    is_ordinary_version = True

    def beginning(self):
        print("Введите, обычная или мизерная версия игры. Если обычная, введите 0, если мизерная, то 1")
        input_int = int(input())
        if input_int == 1:
            is_ordinary_version = False
        else:
            is_ordinary_version = True

        print("Введите массив, обозначающий принадлежности карт по следующему принципу:")
        print("0 - карта принадлежит Вам, 1 - карта принадлежит противнику")
        i = 0
        str = input()
        for c in str:
            if c == '0':
                i += 1
                self.cards_set0.add(i)
                self.cards_list0.append(i)
                self.combined_cards.append(i)
            elif c == '1':
                i += 1
                self.cards_set1.add(i)
                self.cards_list1.append(i)
                self.combined_cards.append(i)

        if i % 2 != 0:
            print('Ошибка! Введен вектор нечетной длины, а карт должно быть поровну!')
        else:
            print('Кто ходит первым: 0 (это Вы, игрок) или 1 (это компьютер)?')
            first_player = int(input())
            print()
            print("Ваши карты", self.cards_list0)
            print("Карты компьютера", self.cards_list1)
            print("Ожидаем, что победит ", end='')
            if is_ordinary_version:
                if (self.combined_cards[-1] in self.cards_set0):
                    print("игрок.")
                else:
                    print("компьютер.")
                print()
                self.attack(first_player)
            else:
                if (self.combined_cards[0] in self.cards_set0):
                    print("игрок.")
                else:
                    print("компьютер.")
                print()
                self.attack_negative(first_player)



    def attack(self, player):
        if len(self.combined_cards) == 0:
            return
        if player == 0:
            print("Ваш ход: ")
            cur_card = int(input())
            self.card_on_table0 = cur_card
            self.cards_list0.remove(cur_card)
            self.combined_cards.remove(cur_card)
            self.cards_set0.discard(cur_card)
        else:
            fl = True
            # fl = "все карты компьютера меньше всех карт игрока-противника"
            optimals = list()
            num_of_cards_considered = 0
            for i in range(len(self.combined_cards)):
                el = self.combined_cards[i]
                if el not in self.cards_set1:
                    fl = False
                    continue
                num_of_cards_considered += 1
                if ((num_of_cards_considered * 2 < len(self.combined_cards)) or (fl) or (num_of_cards_considered == 1)):
                    optimals.append(el)
                else:
                    prev_el = self.combined_cards[i - 1]
                    if prev_el in self.cards_set1:
                        optimals.append(el)
            cur_card = random.choice(optimals)
            print("Все оптимальные ходы компьютера: ", optimals)
            print("Ход компьютера:", cur_card)
            self.card_on_table1 = cur_card
            self.cards_list1.remove(cur_card)
            self.combined_cards.remove(cur_card)
            self.cards_set1.discard(cur_card)
        self.defence((1 + player) % 2)


    def defence(self, player):
        if player == 0:
            print("Ваш ход: ")
            cur_card = int(input())
            self.card_on_table0 = cur_card
            self.cards_list0.remove(cur_card)
            self.combined_cards.remove(cur_card)
            self.cards_set0.discard(cur_card)
        else:
            fl = True
            # fl = "все карты компьютера меньше всех карт игрока-противника"
            optimals = list()
            num_of_cards_considered = 0
            for i in range(len(self.combined_cards)):
                el = self.combined_cards[i]
                if el not in self.cards_set1:
                    fl = False
                    continue
                num_of_cards_considered += 1
                if ((num_of_cards_considered * 2 < len(self.combined_cards)) or (fl) or (num_of_cards_considered == 1)):
                    optimals.append(el)
                else:
                    prev_el = self.combined_cards[i - 1]
                    if prev_el in self.cards_set1:
                        optimals.append(el)
            cur_card = random.choice(optimals)
            print("Все оптимальные ходы компьютера: ", optimals)
            print("Ход компьютера:", cur_card)
            self.card_on_table1 = cur_card
            self.cards_list1.remove(cur_card)
            self.combined_cards.remove(cur_card)
            self.cards_set1.discard(cur_card)
        self.process()



    def process(self):
        if self.card_on_table1 > self.card_on_table0:
            player = 1
            print("Взятку берёт компьютер.")
        else:
            player = 0
            print("Взятку берёт игрок.")
        if len(self.combined_cards) == 0:
            print("Игра окончена.")

            if player == 0:
                print("Победили Вы!")
            else:
                print("Победил компьютер!")
        else:
            print()
            print("Оставшиеся Ваши карты", self.cards_list0)
            print("Оставшиеся карты компьютера", self.cards_list1)
            print("Ожидаем, что победит ", end='')
            if (self.combined_cards[-1] in self.cards_set0):
                print("игрок.")
            else:
                print("компьютер.")
            print()
            self.attack(player)

    def attack_negative(self, player):
        if len(self.combined_cards) == 0:
            return
        if player == 0:
            print("Ваш ход: ")
            cur_card = int(input())
            self.card_on_table0 = cur_card
            self.cards_list0.remove(cur_card)
            self.combined_cards.remove(cur_card)
            self.cards_set0.discard(cur_card)
        else:
            fl = True
            # fl = "все карты компьютера больше всех карт игрока-противника"
            optimals = list()
            num_of_cards_considered = 0
            for i in range(len(self.combined_cards) - 1, -1, -1):
                el = self.combined_cards[i]
                if el not in self.cards_set1:
                    fl = False
                    continue
                num_of_cards_considered += 1
                if ((num_of_cards_considered * 2 < len(self.combined_cards)) or (fl) or (num_of_cards_considered == 1)):
                    optimals.append(el)
                else:
                    prev_el = self.combined_cards[i + 1]
                    if prev_el in self.cards_set1:
                        optimals.append(el)
            cur_card = random.choice(optimals)
            print("Все оптимальные ходы компьютера: ", optimals)
            print("Ход компьютера:", cur_card)
            self.card_on_table1 = cur_card
            self.cards_list1.remove(cur_card)
            self.combined_cards.remove(cur_card)
            self.cards_set1.discard(cur_card)
        self.defence_negative((1 + player) % 2)


    def defence_negative(self, player):
        if player == 0:
            print("Ваш ход: ")
            cur_card = int(input())
            self.card_on_table0 = cur_card
            self.cards_list0.remove(cur_card)
            self.combined_cards.remove(cur_card)
            self.cards_set0.discard(cur_card)
        else:
            fl = True
            # fl = "все карты компьютера больше всех карт игрока-противника"
            optimals = list()
            num_of_cards_considered = 0
            for i in range(len(self.combined_cards) - 1, -1, -1):
                el = self.combined_cards[i]
                if el not in self.cards_set1:
                    fl = False
                    continue
                num_of_cards_considered += 1
                if ((num_of_cards_considered * 2 < len(self.combined_cards)) or (fl) or (num_of_cards_considered == 1)):
                    optimals.append(el)
                else:
                    prev_el = self.combined_cards[i + 1]
                    if prev_el in self.cards_set1:
                        optimals.append(el)
            cur_card = random.choice(optimals)
            print("Все оптимальные ходы компьютера: ", optimals)
            print("Ход компьютера:", cur_card)
            self.card_on_table1 = cur_card
            self.cards_list1.remove(cur_card)
            self.combined_cards.remove(cur_card)
            self.cards_set1.discard(cur_card)
        self.process_negative()



    def process_negative(self):
        if self.card_on_table1 > self.card_on_table0:
            player = 1
            print("Взятку берёт компьютер.")
        else:
            player = 0
            print("Взятку берёт игрок.")

        if len(self.combined_cards) == 0:
            print("Игра окончена.")
            if player == 1:
                print("Победили Вы!")
            else:
                print("Победил компьютер!")
        else:
            print()
            print("Оставшиеся Ваши карты", self.cards_list0)
            print("Оставшиеся карты компьютера", self.cards_list1)
            print("Ожидаем, что победит ", end='')
            if (self.combined_cards[0] in self.cards_set0):
                print("игрок.")
            else:
                print("компьютер.")
            print()
            self.attack_negative(player)



my_game = Game()
my_game.beginning()
