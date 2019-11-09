import sys
from NumberWin import *
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import random




di = {"01": "灵药", "02": "铃儿", "03": "领赏", "04": "零食", "05": "鹦鹉", "06": "领路",
            "07": "令旗", "08": "泥巴", "09": "菱角", "10": "棒球", "11": "筷子", "12": "婴儿",
            "13": "医生", "14": "钥匙", "15": "月亮", "16": "玫瑰", "17": "仪器", "18": "要发",
            "19": "药酒", "20": "二石", "21": "报纸", "22": "饿鹅", "23": "乔丹", "24": "鹅卵石",
            "25": "二胡", "26": "二流子", "27": "耳机", "28": "恶霸", "29": "阿胶", "30": "三菱汽车",
            "31": "山药", "32": "扇儿", "33": "闪闪", "34": "绅士", "35": "珊瑚", "36": "山鹿",
            "37": "山鸡", "38": "女人", "39": "三角尺", "40": "司令", "41": "司仪", "42": "柿儿",
            "43": "石山", "44": "石狮", "45": "师傅", "46": "石榴", "47": "司机", "48": "石板",
            "49": "天安门", "50": "武林盟主", "51": "工人", "52": "斧儿", "53": "武僧", "54": "武士",
            "55": "火车", "56": "蜗牛", "57": "武器", "58": "尾巴", "59": "五角星", "60": "榴莲",
            "61": "儿童", "62": "炉儿", "63": "刘三姐", "64": "柳丝", "65": "锣鼓", "66": "蝌蚪",
            "67": "油漆", "68": "喇叭", "69": "漏斗", "70": "冰淇淋", "71": "奇异果", "72": "企鹅",
            "73": "花旗参", "74": "骑士", "75": "起舞", "76": "气流", "77": "桥", "78": "青蛙",
            "79": "气球", "80": "巴黎铁塔", "81": "白蚁", "82": "靶儿", "83": "花生", "84": "巴士",
            "85": "白虎", "86": "白兔", "87": "白棋", "88": "爸爸", "89": "芭蕉", "90": "酒瓶",
            "91": "球衣", "92": "球儿", "93": "救生圈", "94": "教师", "95": "酒壶", "96": "九牛",
            "97": "紫荆花", "98": "酒吧", "99": "舅舅", "00": "望远镜", "1": "树", "2": "鸭子",
            "3": "耳朵", "4": "红旗", "5": "钩子", "6": "勺子", "7": "拐杖", "8": "葫芦",
            "9": "猫"}


class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)




    def shownum(self):
        shownum = random.choice(list(di.keys()))
        self.ui.numEdit.setText(shownum)

    def showword(self):
        showword=random.choice(list(value for value in di.values()))
        self.ui.wordEdit.setText(showword)

    def showpic(self):
        shownumber = str(self.ui.numEdit.text())
        showwords = str(self.ui.wordEdit.text())

        if di.get(shownumber) == showwords:
            print("输入正确:显示("+shownumber+"---"+showwords+")的图片.")
            pic = QPixmap(".\\res\\"+shownumber+".jpg")
            self.ui.showpic.setPixmap(pic)  # 在label上显示图片
            self.ui.showpic.setScaledContents(True)  # 让图片自适应label大小

        elif list(di.values()).index(showwords) == int(int(shownumber)-1):
            print("输入正确:显示("+shownumber+"---"+showwords+")的图片.")
            pic = QPixmap(".\\res\\" + shownumber + ".jpg")
            self.ui.showpic.setPixmap(pic)  # 在label上显示图片
            self.ui.showpic.setScaledContents(True)  # 让图片自适应label大小
        else:
            print("输入错误:请输入正确的(数字---文字).")
            self.ui.showpic.setText("              请输入正确的(数字---文字).")



if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

