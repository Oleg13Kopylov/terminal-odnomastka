# terminal-odnomastka
Код на Python, моделирующий работу игры "Терминальная одномастка" в обычной и мизерной версиях.

          Условие задачи заключено между светло-синими полосами.
----------
Игра "Одномастка". Предложил Эммануил Ласкер в 1929 году.
Числа    1,2,..., 2k написаны на карточках и  каким-то образом поделены между двумя игроками (сданы). У каждого ровно k карт.
Выбираем, кто ходит первым.
После этого игрок выбирает, какой картой (из своих карт, естественно) ходить. Кладет эту карту на стол. Затем второй игрок выбирает,
какой картой ходить. Кладет на стол её. Сравнивают, чья карта больше.
Далее игрок, карта которого больше, "берет взятку" и начинает следующий ход.
Две карты, который до этого лежали на столе, перед следующим ходом сбрасываются.

В "Одномастке" цель - максимизировать число своих взяток. Побеждает тот, кто взял больше всего взяток.

В "терминальной одномастке" (ДЛЯ КОТОРОЙ НАПИСАНА МОЯ ПРОГРАММА) целью является взять ПОСЛЕДНЮЮ взятку. Тот, кто ее взял, - победитель.

Выше описаны условия для обычной версии игры. В мизерной версии победитель определяется наоборот, а именно:
1) В мизерной "одномастке" победитель - тот, кто взял меньше всего взяток.
2) В мизерной "терминальной одномастке" победитель - это тот, кто НЕ взял последнюю взятку.
----------


          Смысл моей программы:
Реализовать игру в терминальную одномастку (обычную и мизерную версии) для пользователя. Пользователь играет против компьютера (моей программы).
При этом компьютер играет оптимально: определяет множество всех оптимальных ходов для себя, 
ходит случайно и равновероятно одним из этих оптимальных ходов. Компьютер наперед просчитывает, кто победит при оптимальной игре обоих игроков.
Компьютер учитывает возможность ситуации,
где изначально пользователь при правильной игре может победить, но допускает ошибку, тем самым давая компьютеру шанс на победу.
Поэтому уомпьютер ходит так, чтобы при ошибке пользователя одержать над ним победу.
Если же изначально у компьютера есть выигрышная стратегия, то он сразу реализует одну из них (как правило, таких выигрышных стратегий несколько).


          Размышления, выводы:
Первоначально моя идея реализации "терминальной одномастки" была во внесении изменений в код моего коллеги Евгения Краснова,
который реализовал обычную одномастку с помощью сохранения словаря, описывающего всевозможные игровые ситуации. Иными словами, сначала я думал переделать "одномастку" в "терминальную одномастку", сохранив при этом логику работы программы.
Однако позже я осознал, что "терминальную одномастку" можно реализовать другим, более простым на мой взгляд спообом, более математическим.
Он не требует сохранения этого немалого словаря, работает эффективно как по памяти, так и по времени.
И по времени, и по памяти - O(k^2), что является более чем приемлемым: можно обработать k порядка тысячи.
Успех!
