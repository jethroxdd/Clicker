from PyQt5 import QtWidgets
from ui import Ui_MainWindow  # импорт нашего сгенерированного файла
from uishop import Ui_WindowShop
from threading import Timer
from save import save, load
import sys


class MyWindow(QtWidgets.QMainWindow):
    t = Timer
    boost_1_cost = 100
    boost_2_cost = 1000
    boost_3_cost = 50000
    boost_4_cost = 250000
    auto_1_cost = 1000
    auto_2_cost = 10000
    auto_3_cost = 50000
    auto_4_cost = 250000
    lvl = 1
    lvlexp = 100
    exp = 0
    total_clicks = 0
    points = 0
    spoint = 0
    click_cost = 10
    auto_cost = 0

    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.btn_clicked)
        self.ui.Button_shop.clicked.connect(self.btn_shop)
        self.ui.save.clicked.connect(self.save)
        self.ui.load.clicked.connect(self.load)
        self.ui.ProgressBar.setMaximum(self.lvlexp)
        self.ui.ProgressBar.setValue(0)
        self.ui.label_lvl.setText("Уровень " + str(self.lvl))

        self.shop = QtWidgets.QMainWindow()
        self.ui2 = Ui_WindowShop()
        self.ui2.setupUi(self.shop)
        self.shop.setFixedSize(self.shop.width(), self.shop.height())

        self.ui2.clickboost_1.clicked.connect(self.click_boost_1)
        self.ui2.clickboost_2.clicked.connect(self.click_boost_2)
        self.ui2.clickboost_3.clicked.connect(self.click_boost_3)
        self.ui2.clickboost_4.clicked.connect(self.click_boost_4)
        self.ui2.autoclick_1.clicked.connect(self.click_auto_1)
        self.ui2.autoclick_2.clicked.connect(self.click_auto_2)
        self.ui2.autoclick_3.clicked.connect(self.click_auto_3)
        self.ui2.autoclick_4.clicked.connect(self.click_auto_4)
        self.timer()

    def closeEvent(self, event):
        self.t.cancel()
        self.shop.close()

    def save(self):
        save(self.boost_1_cost, self.boost_2_cost, self.boost_3_cost, self.boost_4_cost,
             self.auto_1_cost, self.auto_2_cost, self.auto_3_cost, self.auto_4_cost,
             self.lvl, self.lvlexp, self.exp, self.total_clicks, self.points,
             self.spoint, self.click_cost, self.auto_cost)

    def load(self):
        saves = load()
        self.boost_1_cost = saves[0]
        self.boost_2_cost = saves[1]
        self.boost_3_cost = saves[2]
        self.boost_4_cost = saves[3]
        self.auto_1_cost = saves[4]
        self.auto_2_cost = saves[5]
        self.auto_3_cost = saves[6]
        self.auto_4_cost = saves[7]
        self.lvl = saves[8]
        self.lvlexp = saves[9]
        self.exp = saves[10]
        self.total_clicks = saves[11]
        self.points = saves[12]
        self.spoint = saves[13]
        self.click_cost = saves[14]
        self.auto_cost = saves[15]
        self.reset()

    def reset(self):
        self.ui.label_ptotal.setText("Всего очков: " + str(round(self.points/10000, 4)))
        self.ui.label_auto.setText("Автозароботок: " + str(round(self.auto_cost/10000, 4)))
        self.ui.label_ctotal.setText("Кликов сделано:\n" + str(self.total_clicks))
        self.ui.ProgressBar.setValue(self.exp)
        self.ui.ProgressBar.setMaximum(self.lvlexp)
        self.ui.label_lvl.setText("Уровень " + str(self.lvl))
        self.ui2.cost_1.setText(str(round(self.boost_1_cost/10000, 4)))
        self.ui2.cost_2.setText(str(round(self.boost_2_cost / 10000, 4)))
        self.ui2.cost_3.setText(str(round(self.boost_3_cost / 10000, 4)))
        self.ui2.cost_4.setText(str(round(self.boost_4_cost / 10000, 4)))
        self.ui2.cost_5.setText(str(round(self.auto_1_cost / 10000, 4)))
        self.ui2.cost_6.setText(str(round(self.auto_2_cost / 10000, 4)))
        self.ui2.cost_7.setText(str(round(self.auto_3_cost / 10000, 4)))
        self.ui2.cost_8.setText(str(round(self.auto_4_cost / 10000, 4)))

    def timer(self):
        self.points += self.auto_cost
        self.ui.label_ptotal.setText("Всего очков: " + str(round(self.points / 10000, 4)))
        self.ui.label_psec.setText("Очков в секунду: " + str(round(self.spoint/10000, 4)))
        self.spoint = 0
        self.t = Timer(1, self.timer)
        self.t.start()

    def click_boost_1(self):
        if self.boost_1_cost <= self.points:
            self.points -= self.boost_1_cost
            self.ui.label_ptotal.setText("Всего очков: " + str(round(self.points/10000, 4)))
            self.boost_1_cost += round(self.boost_1_cost/100*5)
            self.click_cost += 5
            self.ui2.cost_1.setText(str(round(self.boost_1_cost/10000, 4)))

    def click_boost_2(self):
        if self.boost_2_cost <= self.points:
            self.points -= self.boost_2_cost
            self.ui.label_ptotal.setText("Всего очков: " + str(round(self.points/10000, 4)))
            self.boost_2_cost += round(self.boost_2_cost/100*10)
            self.click_cost += 10
            self.ui2.cost_2.setText(str(round(self.boost_2_cost/10000, 4)))

    def click_boost_3(self):
        if self.boost_3_cost <= self.points:
            self.points -= self.boost_3_cost
            self.ui.label_ptotal.setText("Всего очков: " + str(round(self.points/10000, 4)))
            self.boost_3_cost += round(self.boost_3_cost/100*10)
            self.click_cost += 500
            self.ui2.cost_3.setText(str(round(self.boost_3_cost/10000, 4)))

    def click_boost_4(self):
        if self.boost_4_cost <= self.points:
            self.points -= self.boost_4_cost
            self.ui.label_ptotal.setText("Всего очков: " + str(round(self.points/10000, 4)))
            self.boost_4_cost += round(self.boost_4_cost/100*10)
            self.click_cost += 2500
            self.ui2.cost_4.setText(str(round(self.boost_4_cost/10000, 4)))

    def click_auto_1(self):
        if self.auto_1_cost <= self.points:
            self.points -= self.auto_1_cost
            self.auto_1_cost += round(self.auto_1_cost / 100 * 10)
            self.auto_cost += 10
            self.ui.label_auto.setText("Авозароботок:" + str(round(self.auto_cost / 10000, 4)))
            self.ui2.cost_5.setText(str(round(self.auto_1_cost / 10000, 4)))

    def click_auto_2(self):
        if self.auto_2_cost <= self.points:
            self.points -= self.auto_2_cost
            self.auto_2_cost += round(self.auto_2_cost/100*10)
            self.auto_cost += 100
            self.ui.label_auto.setText("Авозароботок:" + str(round(self.auto_cost/10000, 4)))
            self.ui2.cost_6.setText(str(round(self.auto_2_cost/10000, 4)))

    def click_auto_3(self):
        if self.auto_3_cost <= self.points:
            self.points -= self.auto_3_cost
            self.auto_3_cost += round(self.auto_3_cost/100*10)
            self.auto_cost += 500
            self.ui.label_auto.setText("Авозароботок:" + str(round(self.auto_cost/10000, 4)))
            self.ui2.cost_7.setText(str(round(self.auto_3_cost/10000, 4)))

    def click_auto_4(self):
        if self.auto_4_cost <= self.points:
            self.points -= self.auto_4_cost
            self.auto_4_cost += round(self.auto_4_cost/100*10)
            self.auto_cost += 2000
            self.ui.label_auto.setText("Авозароботок:" + str(round(self.auto_cost/10000, 4)))
            self.ui2.cost_8.setText(str(round(self.auto_4_cost/10000, 4)))

    def level(self):
        self.exp += round(self.click_cost)
        self.ui.ProgressBar.setValue(self.exp)
        if self.exp >= self.lvlexp:
            self.exp = 0
            self.ui.ProgressBar.setValue(self.exp)
            self.lvlexp += round(self.lvlexp/100*10)
            self.ui.ProgressBar.setMaximum(self.lvlexp)
            self.lvl += 1
            self.ui.label_lvl.setText("Уровень " + str(self.lvl))

    def btn_clicked(self):
        self.spoint += self.click_cost
        self.total_clicks += 1
        self.ui.label_ctotal.setText("Кликов сделано: " + str(self.total_clicks))
        self.points += self.click_cost
        self.points = self.points
        self.ui.label_ptotal.setText("Всего очков:" + str(round(self.points/10000, 4)))
        self.level()

    def btn_shop(self):
        self.shop.show()
        self.shop.move(870, 190)
        self.shop.activateWindow()


app = QtWidgets.QApplication([])
application = MyWindow()
application.setFixedSize(application.width(), application.height())
application.show()

sys.exit(app.exec())
