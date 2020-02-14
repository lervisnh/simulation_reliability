from PyQt5 import QtWidgets, QtGui, QtCore


class AbstractFunction(object):

    def move_to_center(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def show_warning_message(self, message, title='警告', parent=None):
        '''显示警告信息'''
        reply = QtWidgets.QMessageBox.warning(
            parent, title, message, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )
        if reply == QtWidgets.QMessageBox.Yes:
            return True
        else:
            return False


