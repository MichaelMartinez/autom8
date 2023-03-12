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

        self.age_label = QLabel("Age when you retire:")
        self.age_input = QLineEdit()

        self.death_age_label = QLabel("Age at Which You May Die:")
        self.death_age_input = QLineEdit()

        self.increase_label = QLabel("Percentage Increase per Year:")
        self.increase_input = QLineEdit()

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate_pension)

        self.result_label_20 = QLabel("")
        self.result_label_20.setAlignment(Qt.AlignCenter)
        self.result_label_25 = QLabel("")
        self.result_label_25.setAlignment(Qt.AlignCenter)
        self.result_label_30 = QLabel("")
        self.result_label_30.setAlignment(Qt.AlignCenter)

        self.total_pension_20 = QLabel("")
        self.total_pension_20.setAlignment(Qt.AlignCenter)
        self.total_pension_25 = QLabel("")
        self.total_pension_25.setAlignment(Qt.AlignCenter)
        self.total_pension_30 = QLabel("")
        self.total_pension_30.setAlignment(Qt.AlignCenter)

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
        layout.addWidget(self.result_label_20)
        layout.addWidget(self.result_label_25)
        layout.addWidget(self.result_label_30)
        layout.addWidget(self.total_pension_20)
        layout.addWidget(self.total_pension_25)
        layout.addWidget(self.total_pension_30)

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
        self.monthly_pension_label = QLabel("Monthly Pension:")
        self.monthly_pension_input = QLineEdit()

        self.calculate_compare_button = QPushButton("Calculate")
        self.calculate_compare_button.clicked.connect(self.calculate_compare)

        self.compare_result_label = QLabel("")
        self.compare_result_label.setAlignment(Qt.AlignCenter)

        # create layout for tab3
        layout = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addWidget(self.working_years_label)
        hbox.addWidget(self.working_years_combo)
        hbox.addWidget(self.monthly_pension_label)
        hbox.addWidget(self.monthly_pension_input)
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
            self.result_label_20.setText("Years worked must be at least 20.")
        else:
            base_pension = salary * 0.5
            additional_pension = (years - 20) * 0.025 * salary
            total_pension = base_pension + additional_pension
            monthly_pension = total_pension / 12
            self.result_label_20.setText(f"Monthly Benefit: ${monthly_pension:.2f}")

            # calculate projected monthly benefit and future value based on CPI
            cpi = 0.02
            projected_monthly_pension = monthly_pension * (1 + increase/100)**(death_age - age)
            future_value = projected_monthly_pension * (1 + cpi/12)**(12 * (death_age - age))
            self.result_label_20.setText(self.result_label_20.text() + f"\nProjected Monthly Benefit: ${projected_monthly_pension:.2f}\nFuture Value Based on CPI: ${future_value:.2f}")
            base_pension_25 = (25 * 0.025 * salary) / 12
            base_pension_30 = (30 * 0.025 * salary) / 12
            self.result_label_25.setText(f"Monthly Benefit at 25 years of service: ${base_pension_25:.2f}")
            self.result_label_30.setText(f"Monthly Benefit at 30 years of service: ${base_pension_30:.2f}")

            #total pension for years of service at 20, 25, 30
            total_pension_20 = base_pension + (20 * 0.025 * salary) * (death_age - age)
            total_pension_25 = base_pension + (25 * 0.025 * salary) * (death_age - (age + 5))
            total_pension_30 = base_pension + (30 * 0.025 * salary) * (death_age - (age + 10))
            self.total_pension_20.setText(f"Total Pension at 20 years of service for {death_age - age} years: ${total_pension_20:.2f}")
            self.total_pension_25.setText(f"Total Pension at 25 years of service for {death_age - (age + 5)} years (less 5 due to working longer): ${total_pension_25:.2f}\nwith a difference of ${total_pension_25 - total_pension_20:.2f} from 20 years of service")
            self.total_pension_30.setText(f"Total Pension at 30 years of service for {death_age - (age + 10)} years (less 10 due to working longer): ${total_pension_30:.2f}\nwith a difference of ${total_pension_30 - total_pension_20:.2f} from 20 years of service")


    def calculate_drop(self):
        # retrieve input values
        monthly_pension = float(self.drop_input.text())

        # calculate drop program amount
        interest_rate = 0.07
        years = 5
        monthly_rate = interest_rate / 12
        num_payments = years * 12
        drop_amount = 0
        for i in range(num_payments):
            drop_amount = (drop_amount + monthly_pension) * (1 + monthly_rate)

        amortized_amount = drop_amount / num_payments
        self.drop_result_label.setText(f"Total Paid over the Course of the Pension with the Drop Program: ${drop_amount:.2f}")

        # calculate yearly accumulation and show in separate labels
        yearly_accumulation = drop_amount / years
        for i in range(1, years+1):
            label = QLabel(f"Year {i}: ${yearly_accumulation * i:.2f}")
            self.tab2.layout().addWidget(label)


    def calculate_compare(self):
        # retrieve input values
        working_years = int(self.working_years_combo.currentText())
        monthly_pension = float(self.monthly_pension_input.text())
        # calculate equivalent monthly benefit for 25 years of work
        if working_years == 20:
            equivalent_months = 25 * 12
            equivalent_monthly_benefit = monthly_pension / (1 + 0.02 * (25 - 20)) * (1 + 0.02)**(equivalent_months / 12 - 5)
        elif working_years == 25:
            equivalent_monthly_benefit = monthly_pension
        else:
            equivalent_months = 25 * 12
            equivalent_monthly_benefit = monthly_pension / (1 + 0.02 * (30 - 20)) * (1 + 0.02)**(equivalent_months / 12 - 5)

        # display result
        self.compare_result_label.setText(f"To earn an equivalent monthly benefit for 25 years of work, you would need to make ${equivalent_monthly_benefit:.2f} per month in your next job.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = PensionCalculator()
    calculator.show()
    sys.exit(app.exec_())