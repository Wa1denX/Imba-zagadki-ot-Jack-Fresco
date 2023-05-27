from PyQt5. QtCore import Qt
from PyQt5. QtWidgets import QApplication, QButtonGroup, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox, QRadioButton, QHBoxLayout, QGroupBox
from random import shuffle
from random import randint

class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Когда умрёт Уильям Афтон', 'Никогда', 'Чё', 'в 1932','жижа' ))
question_list.append(Question('Как ваше имя', 'А ваше', 'Антон', 'This is Ilon Mask', 'СЭМ'))
question_list.append(Question('Где живут люди', 'на земле', 'в городах', 'в жопе', 'в ядре марса'))
question_list.append(Question('Как зовут ГГ джоджо', 'ДжоДжо', 'Наруто', 'Гон', 'Сайтама'))
question_list.append(Question('Счастсливый билет - правильный ответ сила', 'сила', 'деньги', 'гравитация', 'ядро'))
question_list.append(Question('Где живут фазан', 'под радугой', 'в городах', 'негде', 'в африке'))
question_list.append(Question('Вы люди?', 'Нет я араб', 'я инопрешленец', 'я ДЖОН СИНААААААААА ТУ ТУ ТУУУУУУ', 'Я илон маскц'))
question_list.append(Question('Где деньги взять?', '8 800 555 3535 - лучше позвонить чем у когото занимать', 'у друга в долг', 'у банка', 'у Илона Маска'))
question_list.append(Question('Где деньги', 'сам незнаю', 'в гараже', 'в тайнике', 'в кашельке'))
question_list.append(Question('СНГ', 'снг это снг', 'чё', 'хз', 'я '))
question_list.append(Question('Имя плачущего мальчика', 'у него есть имя?', 'Иван', 'Крис', 'Кэсседи? (кто это сюда вставил)'))
question_list.append(Question('Где Снег', 'хороший вопрос', 'в горах', 'в Москве', 'в Питере'))
question_list.append(Question('Can you feel so broken', 'Can you feel can you feel my HEARD ту ту ту ту', 'I fall in the dark', 'D', 'в ядре марса'))
question_list.append(Question('Где спят люди', 'на кровате', 'в комнате', 'в доме', 'в яице '))
question_list.append(Question('Кто ГГ из аниме Человек Бинзопила', 'Денджи', 'наруто', 'изуку', 'танжиро'))
question_list.append(Question('Макима злодей ?', 'да', 'нет', 'возмонжно', 'незнаю'))
question_list.append(Question('Ерен герой?', 'да', 'нет', 'возмонжно', 'незнаю'))
question_list.append(Question('Правда ли, что The world over heven сильнее Gold Expirience Requim', 'да', 'нет', 'возмонжно', 'незнаю'))
question_list.append(Question('Мармок смешной ?', 'да', 'нет', 'возмонжно', 'незнаю'))






app = QApplication([])
window = QWidget()



btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Когда умрёт Уилльям Афтон')


RadioGroupBox = QGroupBox('Варианты ответа')



rbtn_1 = QRadioButton('Жираф')
rbtn_2 = QRadioButton('Чундрачучундра')
rbtn_3 = QRadioButton('КиШ')
rbtn_4 = QRadioButton('Африка')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)


RadioGroupBox.setLayout(layout_ans1)




AnsGroupBox = QGroupBox('Результат текста')
Lb_Result = QLabel('Правильно/Неправильно')
lb_Correct = QLabel('Правильный ответ')

layout_res = QVBoxLayout()
layout_res.addWidget(Lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
AnsGroupBox.setLayout(layout_res)


layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)




#RadioGroupBox.hide()


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)


layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)

layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_quastion():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)



def test():
    if 'Ответить' == btn_OK.text():
        show_result()
    else:
        show_quastion()

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_quastion()


def show_correct(res):
    Lb_Result.setText(res)
    show_result()



def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        window.score += 1
        print('Статистика\n-Всего вопросов:', window.total, '\n-Правильных ответов:', window.score)
        print('Рейтинг:', (window.score/window.total*100),'%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг:', (window.score/window.total*100),'%')
def next_question():
    window.total += 1
    print('Статистика\n- Всего вопросов:', window.total, '\n-Правильных ответов', window.score)
    cur_question = randint(0,len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)


def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()








window.cur_question = -1
btn_OK.clicked.connect(click_OK)
window.score = 0
window.total = 0

window.setLayout(layout_card)
next_question()
window.resize(400, 500)
window.setWindowTitle('ФНИФ 10 ФУЛ ИКСКЛЮСИВ')
window.show()

app.exec_()