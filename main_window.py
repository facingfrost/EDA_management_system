# coding:utf-8

import sys
import front
import login
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QGraphicsScene
from explorer_load_data import loadData_E4
from ManageData import df_to_sqlite, extract_tables_names,label_artifact,label_not_artifact, sqlite_to_df
from Display import Figure_Canvas
from qt_material import apply_stylesheet


class MainDialog(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = front.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_EDA.clicked.connect(self.open_file_1)
        self.ui.pushButton_ACC.clicked.connect(self.open_file_2)
        self.ui.pushButton_TEMP.clicked.connect(self.open_file_3)
        self.ui.pushButton_store_vis.clicked.connect(self.store_and_vis)
        self.ui.pushButton_upload.clicked.connect(self.switch_widget_1)
        self.ui.pushButton_label_data.clicked.connect(self.switch_widget_2)
        self.ui.pushButton_extract_feature.clicked.connect(self.switch_widget_3)
        self.ui.pushButton_confirm_data.clicked.connect(self.start_label)
        self.start_index = 0
        self.ui.pushButton_previous.clicked.connect(self.previous)
        self.ui.pushButton_next.clicked.connect(self.next)
        self.ui.pushButton_is_artifact.clicked.connect(self.is_artifact)
        self.ui.pushButton_is_not_artifact.clicked.connect(self.is_not_artifact)
        self.ui.pushButton_export.clicked.connect(self.export_data)
        
    
    def open_file_1(self):
        openfile_name = QFileDialog.getOpenFileName(self,'选择文件','','')
        self.EDA_filename = openfile_name[0]
        self.ui.label_file1.setText(openfile_name[0])

    def open_file_2(self):
        openfile_name = QFileDialog.getOpenFileName(self,'选择文件','','')
        self.ACC_filename = openfile_name[0]
        self.ui.label_file2.setText(openfile_name[0])

    def open_file_3(self):
        openfile_name = QFileDialog.getOpenFileName(self,'选择文件','','')
        self.TEMP_filename = openfile_name[0]
        self.ui.label_file3.setText(openfile_name[0])
    
    def switch_widget_1(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def switch_widget_2(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.comboBox_choose_data.addItems(extract_tables_names())

    def switch_widget_3(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    
    def store_and_vis(self):
        df = loadData_E4(self.EDA_filename,self.ACC_filename,self.TEMP_filename)
        table_name = self.ui.lineEdit_getname.text()
        df_to_sqlite(df,table_name)

    def start_label(self):
        dr = Figure_Canvas()
        #实例化一个FigureCanvas
        dr.test(self.start_index, self.ui.comboBox_choose_data.currentText())  # 画图
        graphicscene = QGraphicsScene()  # 第三步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        graphicscene.addWidget(dr)  # 第四步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
        self.ui.graphicsView.setScene(graphicscene)  # 第五步，把QGraphicsScene放入QGraphicsView
        self.ui.graphicsView.show()  # 最后，调用show方法呈现图形！Voila!!
        # self.ui.graphicsView.setFixedSize(200,200)
    
    def previous(self):
        self.start_index -= 40
        dr = Figure_Canvas()
        #实例化一个FigureCanvas
        dr.test(self.start_index, self.ui.comboBox_choose_data.currentText())  # 画图
        graphicscene = QGraphicsScene()  # 第三步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        graphicscene.addWidget(dr)  # 第四步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
        self.ui.graphicsView.setScene(graphicscene)  # 第五步，把QGraphicsScene放入QGraphicsView
        self.ui.graphicsView.show()  # 最后，调用show方法呈现图形！Voila!!
    
    def next(self):
        self.start_index += 40
        dr = Figure_Canvas()
        #实例化一个FigureCanvas
        dr.test(self.start_index, self.ui.comboBox_choose_data.currentText())  # 画图
        graphicscene = QGraphicsScene()  # 第三步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        graphicscene.addWidget(dr)  # 第四步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
        self.ui.graphicsView.setScene(graphicscene)  # 第五步，把QGraphicsScene放入QGraphicsView
        self.ui.graphicsView.show()  # 最后，调用show方法呈现图形！Voila!!
    
    def is_artifact(self):
        label_artifact(self.ui.comboBox_choose_data.currentText(),self.start_index)
        self.next()
    
    def is_not_artifact(self):
        label_not_artifact(self.ui.comboBox_choose_data.currentText(),self.start_index)
        self.next()

    def export_data(self):
        df = sqlite_to_df(self.ui.comboBox_choose_data.currentText())
        df.to_csv(self.ui.comboBox_choose_data.currentText()+".csv")


class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = login.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_login.clicked.connect(self.login_func)

    def login_func(self):
        # self.frontDlg = MainDialog()
        # self.frontDlg.show()
        # self.frontDlg.exec_()
        self.accept()


if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    apply_stylesheet(myapp, theme='light_blue.xml')
    LoginDlg = LoginDialog()
    if LoginDlg.exec_() == QDialog.Accepted:
        # 初始化主功能窗口
        frontDlg = MainDialog()
        # 展示窗口
        frontDlg.show()
        # 设置应用退出
        sys.exit(myapp.exec_())