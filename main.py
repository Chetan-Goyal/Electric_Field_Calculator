from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QDialog, QMessageBox
from PyQt5 import QtGui
import sys
import mpmath as mp
from EFP_Calculator_GUI import *
from EF_of_dipole import *
from copy import deepcopy

mp.dps = 100
class myForm(QMainWindow):
    '''
    Purpose: Main GUI class to handle all the GUI operations and invoking different functions to calculate results
    '''
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.calculate_pushButton.clicked.connect(self.cal_result)
        self.show()


    def mistakes_disp(self, errors:list):
        '''
        Purpose: to display a popup message with list of all the invalid values
        '''
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
        '''
        Purpose: To calculate and results and display results

        Variables Used:
                       1. DM = to store the value of dipole moment
                       2. Exact_Potential = to store the exact potential calculated
                       3. Approx_Potential = to store the value of approx potential calculated
                       4. Error = to store the error i.e difference of exact potential and approx potential
        '''

        DM = dipole_moment(self.charge, self.a)
        self.ui.DM_lineEdit.setText(str(DM))

        Exact_Potential = dipole(self.r, self.angle, self.charge, self.a)
        self.ui.EP_lineEdit.setText(str(Exact_Potential))

        Approx_Potential = dipole_approx(self.r, self.angle, self.charge, self.a)
        self.ui.AP_lineEdit.setText(str(Approx_Potential))

        Error = diff(Exact_Potential, Approx_Potential)
        self.ui.Error_lineEdit.setText(str(Error))

    def cal_result(self):
        '''
        Purpose        : To check if all the input parameters are of correct datatypes. If there's any mistake then invoking mistakes_disp()
                        otherwise invoking results_disp()

        Varaibles Used :
                        1. self.r = to store the distance between center of dipole and the point of observation along with it's unit
                        2. self.a = to store the distance between center of dipole and either charge along with it's unit
                        3. self.angle = to store the angle between point of observation, positive charge and center of dipole along with it's unit
                        4. self.charge = to store the value of charge along with it's unit
                        5. invalid values = to store the names of the attributes with invalid values received
        '''

        invalid_values = list() # Initially, there are no invalid parameters

        # checking if correct value is given to r
        try:
            self.r = ( float( self.ui.r_lineEdit.text()), self.ui.r_comboBox.currentText() )

            # Checking if entered value is not negative
            if self.r[0] <= 0:
                invalid_values.append('r')
        except ValueError:
            invalid_values.append('r')

        # checking if correct value is given to a
        try:
            self.a = ( float( self.ui.a_lineEdit.text() ), self.ui.a_comboBox.currentText() )

            # Checking if entered value is not negative
            if self.a[0] <= 0:
                invalid_values.append('a')
        except ValueError:
            invalid_values.append('a')

        # checking if correct value is given to angle
        try:
            self.angle = ( float( self.ui.theta_lineEdit.text() ), self.ui.theta_comboBox.currentText() )
        except ValueError:
            invalid_values.append('Angle')

        # checking if correct value is given to charge
        try:
            self.charge = ( float( self.ui.q_lineEdit.text() ), self.ui.q_comboBox.currentText() )
            if not self.charge[0]:
                invalid_values.append('Charge')
            elif self.charge[0] < 0:
                self.charge[0] = 0 - self.charge[0]
        except ValueError:
            invalid_values.append('Charge')


        if len(invalid_values):  # If there are some invalid values received
            self.mistakes_disp(invalid_values)
        else:                    # If there's no invalid value received
            self.results_disp()


# Executing our application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myForm()
    w.show()
    sys.exit(app.exec_())