from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QDialog, QMessageBox
from PyQt5 import QtGui
import sys
import mpmath as mp
from EFP_Calculator_GUI import *
from EF_of_dipole import *

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
        
        DM = dipole_moment(self.value_q, self.value_a)
        self.ui.DM_lineEdit.setText(str(DM))

        Exact_Potential = dipole(self.value_r, self.value_theta, self.value_q, self.value_a)
        self.ui.EP_lineEdit.setText(str(Exact_Potential))

        Approx_Potential = dipole_approx(self.value_r, self.value_theta, self.value_q, self.value_a)
        self.ui.AP_lineEdit.setText(str(Approx_Potential))

        Error = diff(Exact_Potential, Approx_Potential)
        self.ui.Error_lineEdit.setText(str(Error))

    def cal_result(self):
        invalid_values = list()
        
        # Storing Units of all the input parameters
        self.unit_r = self.ui.r_comboBox.currentText()
        self.unit_q = self.ui.q_comboBox.currentText()
        self.unit_angle = self.ui.theta_comboBox.currentText()
        self.unit_a = self.ui.a_comboBox.currentText()

        try:
            self.value_r = mp.mpf( self.ui.r_lineEdit.text() )
        except ValueError:
            invalid_values.append('r')
        
        try:
            self.value_a = mp.mpf( self.ui.a_lineEdit.text() )
        except ValueError:
            invalid_values.append('a')
        
        try:
            self.value_theta = mp.mpf( self.ui.theta_lineEdit.text() )
        except ValueError:
            invalid_values.append('Angle')
        
        try:
            self.value_q = mp.mpf( self.ui.q_lineEdit.text() )
        except ValueError:
            invalid_values.append('Charge')
        
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