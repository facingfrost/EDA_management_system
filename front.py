# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'front.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(850, 649)
        self.stackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.stackedWidget.setGeometry(QtCore.QRect(50, 90, 621, 541))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pushButton_store_vis = QtWidgets.QPushButton(self.page)
        self.pushButton_store_vis.setGeometry(QtCore.QRect(50, 430, 341, 41))
        self.pushButton_store_vis.setObjectName("pushButton_store_vis")
        self.pushButton_TEMP = QtWidgets.QPushButton(self.page)
        self.pushButton_TEMP.setGeometry(QtCore.QRect(40, 250, 151, 51))
        self.pushButton_TEMP.setObjectName("pushButton_TEMP")
        self.pushButton_EDA = QtWidgets.QPushButton(self.page)
        self.pushButton_EDA.setGeometry(QtCore.QRect(40, 30, 151, 51))
        self.pushButton_EDA.setObjectName("pushButton_EDA")
        self.pushButton_ACC = QtWidgets.QPushButton(self.page)
        self.pushButton_ACC.setGeometry(QtCore.QRect(40, 140, 151, 51))
        self.pushButton_ACC.setObjectName("pushButton_ACC")
        self.label_file1 = QtWidgets.QLabel(self.page)
        self.label_file1.setGeometry(QtCore.QRect(250, 30, 271, 51))
        self.label_file1.setObjectName("label_file1")
        self.label_file2 = QtWidgets.QLabel(self.page)
        self.label_file2.setGeometry(QtCore.QRect(250, 150, 271, 31))
        self.label_file2.setObjectName("label_file2")
        self.label_file3 = QtWidgets.QLabel(self.page)
        self.label_file3.setGeometry(QtCore.QRect(250, 250, 271, 51))
        self.label_file3.setObjectName("label_file3")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(60, 360, 63, 69))
        self.label_2.setObjectName("label_2")
        self.lineEdit_getname = QtWidgets.QLineEdit(self.page)
        self.lineEdit_getname.setGeometry(QtCore.QRect(200, 380, 191, 31))
        self.lineEdit_getname.setObjectName("lineEdit_getname")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.page_2)
        self.graphicsView.setGeometry(QtCore.QRect(20, 90, 431, 441))
        self.graphicsView.setObjectName("graphicsView")
        self.comboBox_choose_data = QtWidgets.QComboBox(self.page_2)
        self.comboBox_choose_data.setGeometry(QtCore.QRect(20, 20, 181, 31))
        self.comboBox_choose_data.setObjectName("comboBox_choose_data")
        self.pushButton_confirm_data = QtWidgets.QPushButton(self.page_2)
        self.pushButton_confirm_data.setGeometry(QtCore.QRect(210, 20, 181, 31))
        self.pushButton_confirm_data.setObjectName("pushButton_confirm_data")
        self.pushButton_is_artifact = QtWidgets.QPushButton(self.page_2)
        self.pushButton_is_artifact.setGeometry(QtCore.QRect(480, 100, 121, 41))
        self.pushButton_is_artifact.setObjectName("pushButton_is_artifact")
        self.pushButton_previous = QtWidgets.QPushButton(self.page_2)
        self.pushButton_previous.setGeometry(QtCore.QRect(480, 180, 121, 41))
        self.pushButton_previous.setObjectName("pushButton_previous")
        self.pushButton_next = QtWidgets.QPushButton(self.page_2)
        self.pushButton_next.setGeometry(QtCore.QRect(480, 260, 121, 41))
        self.pushButton_next.setObjectName("pushButton_next")
        self.pushButton_is_not_artifact = QtWidgets.QPushButton(self.page_2)
        self.pushButton_is_not_artifact.setGeometry(QtCore.QRect(480, 340, 121, 41))
        self.pushButton_is_not_artifact.setObjectName("pushButton_is_not_artifact")
        self.pushButton_export = QtWidgets.QPushButton(self.page_2)
        self.pushButton_export.setGeometry(QtCore.QRect(480, 420, 121, 41))
        self.pushButton_export.setObjectName("pushButton_export")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label = QtWidgets.QLabel(self.page_3)
        self.label.setGeometry(QtCore.QRect(60, 50, 71, 41))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setGeometry(QtCore.QRect(130, 50, 71, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setGeometry(QtCore.QRect(320, 50, 71, 41))
        self.label_4.setObjectName("label_4")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.page_3)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(60, 130, 431, 351))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 5, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.lineEdit_ISCR = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_ISCR.setObjectName("lineEdit_ISCR")
        self.gridLayout.addWidget(self.lineEdit_ISCR, 2, 1, 1, 1)
        self.lineEdit_AUC = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_AUC.setObjectName("lineEdit_AUC")
        self.gridLayout.addWidget(self.lineEdit_AUC, 1, 1, 1, 1)
        self.lineEdit_amplitude = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_amplitude.setObjectName("lineEdit_amplitude")
        self.gridLayout.addWidget(self.lineEdit_amplitude, 0, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 0, 1, 1)
        self.lineEdit_SCR_num = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_SCR_num.setObjectName("lineEdit_SCR_num")
        self.gridLayout.addWidget(self.lineEdit_SCR_num, 3, 1, 1, 1)
        self.lineEdit_SCR_arousal = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_SCR_arousal.setObjectName("lineEdit_SCR_arousal")
        self.gridLayout.addWidget(self.lineEdit_SCR_arousal, 4, 1, 1, 1)
        self.lineEdit_SCR_recovery = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_SCR_recovery.setObjectName("lineEdit_SCR_recovery")
        self.gridLayout.addWidget(self.lineEdit_SCR_recovery, 5, 1, 1, 1)
        self.lineEdit_feature_start = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_feature_start.setGeometry(QtCore.QRect(190, 50, 111, 41))
        self.lineEdit_feature_start.setObjectName("lineEdit_feature_start")
        self.lineEdit_feature_end = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_feature_end.setGeometry(QtCore.QRect(380, 50, 111, 41))
        self.lineEdit_feature_end.setObjectName("lineEdit_feature_end")
        self.stackedWidget.addWidget(self.page_3)
        self.pushButton_upload = QtWidgets.QPushButton(Dialog)
        self.pushButton_upload.setGeometry(QtCore.QRect(50, 20, 101, 51))
        self.pushButton_upload.setObjectName("pushButton_upload")
        self.pushButton_label_data = QtWidgets.QPushButton(Dialog)
        self.pushButton_label_data.setGeometry(QtCore.QRect(170, 20, 101, 51))
        self.pushButton_label_data.setObjectName("pushButton_label_data")
        self.pushButton_extract_feature = QtWidgets.QPushButton(Dialog)
        self.pushButton_extract_feature.setGeometry(QtCore.QRect(290, 20, 101, 51))
        self.pushButton_extract_feature.setObjectName("pushButton_extract_feature")

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_store_vis.setText(_translate("Dialog", "上传数据"))
        self.pushButton_TEMP.setText(_translate("Dialog", "上传TEMP"))
        self.pushButton_EDA.setText(_translate("Dialog", "上传EDA"))
        self.pushButton_ACC.setText(_translate("Dialog", "上传ACC"))
        self.label_file1.setText(_translate("Dialog", "未选择EDA文件"))
        self.label_file2.setText(_translate("Dialog", "未选择ACC文件"))
        self.label_file3.setText(_translate("Dialog", "未选择TEMP文件"))
        self.label_2.setText(_translate("Dialog", "请输入数据名称"))
        self.pushButton_confirm_data.setText(_translate("Dialog", "确认选择"))
        self.pushButton_is_artifact.setText(_translate("Dialog", "是伪迹"))
        self.pushButton_previous.setText(_translate("Dialog", "上一段数据"))
        self.pushButton_next.setText(_translate("Dialog", "下一段数据"))
        self.pushButton_is_not_artifact.setText(_translate("Dialog", "不是伪迹"))
        self.pushButton_export.setText(_translate("Dialog", "导出数据"))
        self.label.setText(_translate("Dialog", "时间段选择"))
        self.label_3.setText(_translate("Dialog", "开始时间："))
        self.label_4.setText(_translate("Dialog", "结束时间："))
        self.label_7.setText(_translate("Dialog", "AUC"))
        self.label_5.setText(_translate("Dialog", "振幅"))
        self.label_11.setText(_translate("Dialog", "SCR唤起时间"))
        self.label_13.setText(_translate("Dialog", "SCR复原时间"))
        self.label_9.setText(_translate("Dialog", "SCR数量"))
        self.label_15.setText(_translate("Dialog", "ISCR"))
        self.pushButton_upload.setText(_translate("Dialog", "上传数据"))
        self.pushButton_label_data.setText(_translate("Dialog", "标记数据"))
        self.pushButton_extract_feature.setText(_translate("Dialog", "提取指标"))
