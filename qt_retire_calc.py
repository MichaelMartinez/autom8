import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox
from PyQt5.QtCore import Qt

class PensionCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Firefighter Pension Calculator")

        # create tabs
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.tabs.addTab(self.tab1, "Calculate Pension")
        self.tabs.addTab(self.tab2, "Drop Program")
        self.tabs.addTab(self.tab3, "Compare Working Years")

        # initialize widgets
        self.initTab1()
        self.initTab2()
        self.initTab3()

    def initTab1(self):
        # create widgets for tab1
        self.years_label = QLabel("Years Worked:")
        self.years_input = QLineEdit()

        self.salary_label = QLabel("Highest Salary Earned:")
        self.salary_input = QLineEdit()

        self.age_label = QLabel("Current Age:")
        self.age_input = QLineEdit()

        self.death_age_label = QLabel("Age at Which You May Die:")
        self.death_age_input = QLineEdit()

        self.increase_label = QLabel("Percentage Increase per Year:")
        self.increase_input = QLineEdit()

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate_pension)

        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignCenter)

        # create layout for tab1
        layout = QVBoxLayout()
        layout.addWidget(self.years_label)
        layout.addWidget(self.years_input)
        layout.addWidget(self.salary_label)
        layout.addWidget(self.salary_input)
        layout.addWidget(self.age_label)
        layout.addWidget(self.age_input)
        layout.addWidget(self.death_age_label)
        layout.addWidget(self.death_age_input)
        layout.addWidget(self.increase_label)
        layout.addWidget(self.increase_input)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)

        # set layout for tab1
        self.tab1.setLayout(layout)

    def initTab2(self):
        # create widgets for tab2
        self.drop_label = QLabel("Monthly Pension Benefit in the Drop Program:")
        self.drop_input = QLineEdit()

        self.calculate_drop_button = QPushButton("Calculate")
        self.calculate_drop_button.clicked.connect(self.calculate_drop)

        self.drop_result_label = QLabel("")
        self.drop_result_label.setAlignment(Qt.AlignCenter)

        # create layout for tab2
        layout = QVBoxLayout()
        layout.addWidget(self.drop_label)
        layout.addWidget(self.drop_input)
        layout.addWidget(self.calculate_drop_button)
        layout.addWidget(self.drop_result_label)

        # set layout for tab2
        self.tab2.setLayout(layout)

    def initTab3(self):
        # create widgets for tab3
        self.working_years_label = QLabel("Working Years:")
        self.working_years_combo = QComboBox()
        self.working_years_combo.addItem("20")
        self.working_years_combo.addItem("25")

        self.calculate_compare_button = QPushButton("Calculate")
        self.calculate_compare_button.clicked.connect(self.calculate_compare)

        self.compare_result_label = QLabel("")
        self.compare_result_label.setAlignment(Qt.AlignCenter)

        # create layout for tab3
        layout = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addWidget(self.working_years_label)
        hbox.addWidget(self.working_years_combo)
        layout.addLayout(hbox)
        layout.addWidget(self.calculate_compare_button)
        layout.addWidget(self.compare_result_label)

        # set layout for tab3
        self.tab3.setLayout(layout)

    def calculate_pension(self):
        # retrieve input values
        years = int(self.years_input.text())
        salary = int(self.salary_input.text())
        age = int(self.age_input.text())
        death_age = int(self.death_age_input.text())
        increase = float(self.increase_input.text())

        # calculate pension amount
        if years < 20:
            self.result_label.setText("Years worked must be at least 20.")
        else:
            base_pension = salary * 0.5
            additional_pension = (years - 20) * 0.025 * salary
            total_pension = base_pension + additional_pension
            monthly_pension = total_pension / 12
            self.result_label.setText(f"Monthly Benefit: ${monthly_pension:.2f}")

            # calculate projected monthly benefit and future value based on CPI
            cpi = 0.02
            projected_monthly_pension = monthly_pension * (1 + increase/100)**(death_age - age)
            future_value = projected_monthly_pension * (1 + cpi/12)**(12 * (death_age - age))
            self.result_label.setText(self.result_label.text() + f"\nProjected Monthly Benefit: ${projected_monthly_pension:.2f}\nFuture Value Based on CPI: ${future_value:.2f}")

            # calculate total amount paid over the course of the pension for 20, 25, and 30 years
            total_paid_20 = monthly_pension * 12 * 20
            total_paid_25 = monthly_pension * 12 * 25
            total_paid_30 = monthly_pension * 12 * 30
            self.result_label.setText(self.result_label.text() + f"\nTotal Paid for 20 Years: ${total_paid_20:.2f}\nTotal Paid for 25 Years: ${total_paid_25:.2f}\nTotal Paid for 30 Years: ${total_paid_30:.2f}")

    def calculate_drop(self):
        # retrieve input values
        monthly_pension = float(self.drop_input.text())

        # calculate drop program amount
        interest_rate = 0.07
        years = 5
        drop_amount = monthly_pension * (1 + interest_rate)**years
        amortized_amount = drop_amount / (years * 12)
        self.drop_result_label.setText(f"Total Paid over the Course of the Pension with the Drop Program: ${amortized_amount:.2f}")

    def calculate_compare(self):
        # retrieve input values
        working_years = int(self.working_years_combo.currentText())

        # calculate equivalent salary for 25 years of work
        if working_years == 20:
            equivalent_salary = float(self.result_label.text().split(": $")[1].split("\n")[0]) / (25 - 20)
        else:
            equivalent_salary = float(self.result_label.text().split(": $")[1].split("\n")[0])

        # display result
        self.compare_result_label.setText(f"To earn an equivalent monthly benefit for 25 years of work, you would need to make ${equivalent_salary:.2f} per month in your next job.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = PensionCalculator()
    calculator.show()
    sys.exit(app.exec_())