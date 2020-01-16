from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QDialog, QMessageBox
from PyQt5 import QtGui
import sys
import mpmath as mp
from EFP_Calculator_GUI import *
from EF_of_dipole import *
from copy import deepcopy

mp.dps = 100
class myForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.calculate_pushButton.clicked.connect(self.cal_result)
        self.show()


    def mistakes_disp(self, errors:list):
        # First line of error message 
        message = 'Invalid Input received for the following attribute(s) :\n'

        # Editing Message as per the errors
        for i, error in enumerate(errors):
            message += str(i+1) + ' : ' + error + '\n'

        # Displaying error message
        response = QMessageBox.question(self, 'Errors!', message, QMessageBox.Ok )

        # Closing Message Box
        if response == QMessageBox.Yes:
            sys.exit()


    def results_disp(self):
        
        DM = dipole_moment(self.charge, self.a)
        self.ui.DM_lineEdit.setText(str(DM))

        Exact_Potential = dipole(self.r, self.angle, self.charge, self.a)
        self.ui.EP_lineEdit.setText(str(Exact_Potential))

        Approx_Potential = dipole_approx(self.r, self.angle, self.charge, self.a)
        self.ui.AP_lineEdit.setText(str(Approx_Potential))

        Error = diff(Exact_Potential, Approx_Potential)
        self.ui.Error_lineEdit.setText(str(Error))

    def cal_result(self):
        invalid_values = list()
        

        try:
            self.r = ( float( self.ui.r_lineEdit.text()), self.ui.r_comboBox.currentText() )
        except ValueError:
            invalid_values.append('r')
        
        try:
            self.a = ( float( self.ui.a_lineEdit.text() ), self.ui.a_comboBox.currentText() )
        except ValueError:
            invalid_values.append('a')
        
        try:
            self.angle = ( float( self.ui.theta_lineEdit.text() ), self.ui.theta_comboBox.currentText() )
        except ValueError:
            invalid_values.append('Angle')
        
        try:
            self.charge = ( float( self.ui.q_lineEdit.text() ), self.ui.q_comboBox.currentText() )
        except ValueError:
            invalid_values.append('Charge')
        
        # * # Storing Units of all the input parameters
        # * self.unit_r = self.ui.r_comboBox.currentText()
        # * self.unit_q = semp.mpflf.ui.q_comboBox.currentText()
        # * self.unit_angle = self.ui.theta_comboBox.currentText()
        # * self.unit_a = self.ui.a_comboBox.currentText()


        print(invalid_values)

        if len(invalid_values):
            self.mistakes_disp(invalid_values)
        else:
            self.results_disp()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myForm()
    w.show()
    sys.exit(app.exec_())