import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QMainWindow,QApplication
import sys
import numpy as np
from ManageData import sqlite_to_df



class Figure_Canvas(FigureCanvas):   # 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplot lib的关键

    def __init__(self, parent=None, width=6, height=6, dpi=70):
        fig = Figure(figsize=(width, height), dpi=dpi)  # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure

        FigureCanvas.__init__(self, fig) # 初始化父类
        self.setParent(parent)

        self.ax1 = fig.add_subplot(311) # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法
        self.ax2 = fig.add_subplot(312)
        self.ax3 = fig.add_subplot(313)

    def test(self,start_index, table_name):
        df = sqlite_to_df(table_name)
        x1 = range(start_index,start_index+200)
        y1 = df["EDA"][start_index:start_index+200]
        y21 = df["AccelX"][start_index:start_index+200]
        y22 = df["AccelY"][start_index:start_index+200]
        y23 = df["AccelZ"][start_index:start_index+200]
        y3 = df["Temp"][start_index:start_index+200]

        self.ax1.plot(x1, y1, 'o-')
        self.ax1.legend(["EDA"])
        self.ax1.set_ylabel('EDA')

        self.ax2.plot(x1, y21, '.-')
        self.ax2.plot(x1, y22, '.-')
        self.ax2.plot(x1, y23, '.-')
        self.ax2.set_xlabel('time (s)')
        self.ax2.set_ylabel('ACC')
        self.ax2.legend(["AccelX","AccelY","AccelZ"])

        self.ax3.plot(x1, y3, '.-')
        self.ax3.set_xlabel('time (s)')
        self.ax3.legend(["Temp"])
        self.ax3.set_ylabel('Temp')
