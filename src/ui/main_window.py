# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Projects\python\radar_project\src\ui\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1091, 702)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_add_model = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        self.btn_add_model.setFont(font)
        self.btn_add_model.setObjectName("btn_add_model")
        self.verticalLayout.addWidget(self.btn_add_model)
        self.btn_delete_model = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        self.btn_delete_model.setFont(font)
        self.btn_delete_model.setObjectName("btn_delete_model")
        self.verticalLayout.addWidget(self.btn_delete_model)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_add_paras = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        self.btn_add_paras.setFont(font)
        self.btn_add_paras.setObjectName("btn_add_paras")
        self.verticalLayout_2.addWidget(self.btn_add_paras)
        self.btn_delete_paras = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        self.btn_delete_paras.setFont(font)
        self.btn_delete_paras.setObjectName("btn_delete_paras")
        self.verticalLayout_2.addWidget(self.btn_delete_paras)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_simulation = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        self.btn_simulation.setFont(font)
        self.btn_simulation.setObjectName("btn_simulation")
        self.verticalLayout_3.addWidget(self.btn_simulation)
        self.btn_stress_analysis = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        self.btn_stress_analysis.setFont(font)
        self.btn_stress_analysis.setObjectName("btn_stress_analysis")
        self.verticalLayout_3.addWidget(self.btn_stress_analysis)
        self.btn_displacement_analysis = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        self.btn_displacement_analysis.setFont(font)
        self.btn_displacement_analysis.setObjectName("btn_displacement_analysis")
        self.verticalLayout_3.addWidget(self.btn_displacement_analysis)
        self.btn_reliability_analysis = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_reliability_analysis.setObjectName("btn_reliability_analysis")
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        self.btn_reliability_analysis.setFont(font)
        self.btn_reliability_analysis.setObjectName("btn_reliability_analysis")
        self.verticalLayout_3.addWidget(self.btn_reliability_analysis)
        self.btn_report = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        self.btn_report.setFont(font)
        self.btn_report.setObjectName("btn_report")
        self.verticalLayout_3.addWidget(self.btn_report)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.widget_content = QtWidgets.QWidget(self.centralwidget)
        self.widget_content.setObjectName("widget_content")
        self.horizontalLayout.addWidget(self.widget_content)
        self.horizontalLayout.setStretch(2, 1)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1091, 34))
        self.menubar.setObjectName("menubar")
        self.menu_1 = QtWidgets.QMenu(self.menubar)
        self.menu_1.setObjectName("menu_1")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.action_password_reset = QtWidgets.QAction(MainWindow)
        self.action_password_reset.setObjectName("action_password_reset")
        self.action_user_manage = QtWidgets.QAction(MainWindow)
        self.action_user_manage.setObjectName("action_user_manage")
        self.action_view_config = QtWidgets.QAction(MainWindow)
        self.action_view_config.setObjectName("action_view_config")
        self.action_edit_config = QtWidgets.QAction(MainWindow)
        self.action_edit_config.setObjectName("action_edit_config")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.menu_1.addAction(self.action_password_reset)
        self.menu_1.addSeparator()
        self.menu_1.addAction(self.action_user_manage)
        self.menu_2.addAction(self.action_view_config)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_edit_config)
        self.menu_3.addAction(self.action_about)
        self.menubar.addAction(self.menu_1.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "仿真模型导入"))
        self.btn_add_model.setText(_translate("MainWindow", "导入模型"))
        self.btn_delete_model.setText(_translate("MainWindow", "删除模型"))
        self.groupBox_2.setTitle(_translate("MainWindow", "环境参数管理"))
        self.btn_add_paras.setText(_translate("MainWindow", "新增参数"))
        self.btn_delete_paras.setText(_translate("MainWindow", "删除参数"))
        self.groupBox_3.setTitle(_translate("MainWindow", "仿真与可靠性分析"))
        self.btn_simulation.setText(_translate("MainWindow", "开始仿真"))
        self.btn_stress_analysis.setText(_translate("MainWindow", "应力应变分析"))
        self.btn_displacement_analysis.setText(_translate("MainWindow", "位移变形分析"))
        self.btn_reliability_analysis.setText(_translate("MainWindow", "可靠性分析"))
        self.btn_report.setText(_translate("MainWindow", "生成报告"))
        self.menu_1.setTitle(_translate("MainWindow", "用户管理"))
        self.menu_2.setTitle(_translate("MainWindow", "仿真软件配置"))
        self.menu_3.setTitle(_translate("MainWindow", "帮助"))
        self.action_password_reset.setText(_translate("MainWindow", "修改密码"))
        self.action_user_manage.setText(_translate("MainWindow", "用户管理"))
        self.action_user_manage.setToolTip(_translate("MainWindow", "用户管理"))
        self.action_view_config.setText(_translate("MainWindow", "查看配置"))
        self.action_edit_config.setText(_translate("MainWindow", "设置配置"))
        self.action_about.setText(_translate("MainWindow", "关于本软件"))
        self.action_about.setToolTip(_translate("MainWindow", "关于本软件"))
