import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QComboBox,
)
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
        self.total_pension_20_num = 0
        self.total_pension_25_num = 0
        self.total_pension_30_num = 0
        self.drop_comp_20 = 0
        self.drop_comp_25 = 0

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

        self.total_pension_20_delimit = QLabel("20 Year Scenario")
        self.total_pension_20_delimit.setAlignment(Qt.AlignCenter)
        self.total_pension_20 = QLabel("")
        self.total_pension_20.setAlignment(Qt.AlignCenter)
        self.total_pension_25_delimit = QLabel("25 Year Scenario")
        self.total_pension_25_delimit.setAlignment(Qt.AlignCenter)
        self.total_pension_25 = QLabel("")
        self.total_pension_25.setAlignment(Qt.AlignCenter)
        self.total_pension_30_delimit = QLabel("30 Year Scenario")
        self.total_pension_30_delimit.setAlignment(Qt.AlignCenter)
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
        layout.addWidget(self.total_pension_20_delimit)
        layout.addWidget(self.total_pension_20)
        layout.addWidget(self.total_pension_25_delimit)
        layout.addWidget(self.total_pension_25)
        layout.addWidget(self.total_pension_30_delimit)
        layout.addWidget(self.total_pension_30)

        # set layout for tab1
        self.tab1.setLayout(layout)

    def initTab2(self):
        # create widgets for tab2
        self.drop_label = QLabel("Monthly Pension Benefit in the Drop Program:")
        self.drop_input = QLineEdit()
        self.years_retired_label = QLabel(
            "How many years will you collect retirement benefits?"
        )
        self.years_retired_input = QLineEdit()

        self.calculate_drop_button = QPushButton("Calculate")
        self.calculate_drop_button.clicked.connect(self.calculate_drop)

        self.drop_result_label = QLabel("")
        self.drop_result_label.setAlignment(Qt.AlignCenter)
        self.drop_comp_20_label = QLabel("")
        self.drop_comp_20_label.setAlignment(Qt.AlignCenter)
        self.drop_comp_25_label = QLabel("")
        self.drop_comp_25_label.setAlignment(Qt.AlignCenter)
        self.drop_amort_label = QLabel("")
        self.drop_amort_label.setAlignment(Qt.AlignCenter)

        # create layout for tab2
        layout = QVBoxLayout()
        layout.addWidget(self.drop_label)
        layout.addWidget(self.drop_input)
        layout.addWidget(self.years_retired_label)
        layout.addWidget(self.years_retired_input)
        layout.addWidget(self.calculate_drop_button)
        layout.addWidget(self.drop_result_label)
        layout.addWidget(self.drop_comp_20_label)
        layout.addWidget(self.drop_comp_25_label)
        layout.addWidget(self.drop_amort_label)

        # set layout for tab2
        self.tab2.setLayout(layout)

    def initTab3(self):
        # create widgets for tab3
        self.monthly_salary_lable = QLabel("Monthly Pension:")
        self.monthly_salary_lable.setAlignment(Qt.AlignCenter)
        self.hourly_rate_lable = QLabel("Hourly Rate in Menial Job:")
        self.hourly_rate_input = QLineEdit()
        self.hours_per_week_lable = QLabel("How many hours per week can you work:")
        self.hours_per_week_input = QLineEdit()

        self.calculate_compare_button = QPushButton("Calculate")
        self.calculate_compare_button.clicked.connect(self.calculate_compare)

        self.compare_result_label = QLabel("")
        self.compare_result_label.setAlignment(Qt.AlignCenter)

        # create layout for tab3
        layout = QVBoxLayout()
        layout.addWidget(self.monthly_salary_lable)
        layout.addWidget(self.hourly_rate_lable)
        layout.addWidget(self.hourly_rate_input)
        layout.addWidget(self.hours_per_week_lable)
        layout.addWidget(self.hours_per_week_input)
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
            self.monthly_pension = monthly_pension
            self.result_label_20.setText(f"Monthly Benefit: ${monthly_pension:.2f}")

            # calculate projected monthly benefit and future value based on CPI
            cpi = 0.02
            projected_monthly_pension = monthly_pension * (1 + increase / 100) ** (
                death_age - age
            )
            future_value = projected_monthly_pension * (1 + cpi / 12) ** (
                12 * (death_age - age)
            )
            self.result_label_20.setText(
                self.result_label_20.text()
                + f"\nProjected Monthly Benefit: ${projected_monthly_pension:.2f}\nFuture Value Based on CPI: ${future_value:.2f}"
            )
            base_pension_25 = (25 * 0.025 * salary) / 12
            self.base_pension_25 = base_pension_25
            base_pension_30 = (30 * 0.025 * salary) / 12
            self.base_pension_30 = base_pension_30
            self.result_label_25.setText(
                f"Monthly Benefit at 25 years of service: ${base_pension_25:.2f}"
            )
            self.result_label_30.setText(
                f"Monthly Benefit at 30 years of service: ${base_pension_30:.2f}"
            )

            # total pension for years of service at 20, 25, 30
            self.total_pension_20_num = base_pension + (20 * 0.025 * salary) * (
                death_age - age
            )
            # THis is for comparison with in DROP tab
            self.total_pension_drop_20_num = base_pension + (20 * 0.025 * salary) * (
                death_age - (age + 5)
            )
            self.total_pension_25_num = base_pension + (25 * 0.025 * salary) * (
                death_age - (age + 5)
            )
            self.total_pension_30_num = base_pension + (30 * 0.025 * salary) * (
                death_age - (age + 10)
            )
            self.total_pension_20.setText(
                f"Total Pension for {death_age - age} years: ${self.total_pension_20_num:.2f}"
            )
            self.total_pension_25.setText(
                f"Total pension for {(death_age - (age + 5))} years (less 5 due to working longer): ${self.total_pension_25_num:.2f}\n with a difference of ${self.total_pension_25_num - self.total_pension_20_num:.2f} from 20 years of service"
            )
            self.total_pension_30.setText(
                f"Total pension for {(death_age - (age + 10))} years (less 10 due to working longer): ${self.total_pension_30_num:.2f}\n with a difference of ${self.total_pension_30_num - self.total_pension_20_num:.2f} from 20 years of service"
            )

    def calculate_drop(self):
        # retrieve input values
        monthly_pension = float(self.drop_input.text())
        years_retired = int(self.years_retired_input.text())

        # calculate drop program amount
        interest_rate = 0.07
        years = 5
        monthly_rate = interest_rate / 12
        num_payments = years * 12
        drop_amount = 0
        for i in range(num_payments):
            drop_amount = (drop_amount + monthly_pension) * (1 + monthly_rate)

        amortized_amount = drop_amount / num_payments
        self.drop_result_label.setText(
            f"Total Paid over the Course of the Pension with the Drop Program: ${drop_amount:.2f}"
        )

        # calculate yearly accumulation and show in separate labels
        # yearly_accumulation = drop_amount / years
        # for i in range(1, years + 1):
        #     label = QLabel(f"Year {i}: ${yearly_accumulation * i:.2f}")
        #     self.tab2.layout().addWidget(label)

        # lets figure out the total compensation for those who do not and do participate in the DROP program
        # lets assume that the person who does not participate in the DROP program retires at 20 years of service
        # and the person who does participate in the DROP program retires at 25 years of service
        # we must factor age and death age into the equation
        self.drop_comp_20_label.setText(
            "Total Pension at 20 years of service last operation is ${:.2f}".format(
                self.total_pension_20_num
            )
        )
        total_pen_drop_25 = self.total_pension_drop_20_num + drop_amount
        diff_drop_25 = total_pen_drop_25 - self.total_pension_20_num
        self.drop_comp_25_label.setText(
            f"Total Pension at 20 years of service subtracting 5 years of pension collection for DROP is ${total_pen_drop_25:.2f}\n The difference is ${diff_drop_25:.2f} as this person collected pension for 5 years additional years."
        )

        self.drop_amort_label.setText(
            f"Amortize the DROP and pension over ${(years_retired - 5)} years of collecting pension is ${(total_pen_drop_25 / (years_retired - 5)):.2f} per year.\n Amortize standard 20 year pension over ${years_retired} years is ${(self.total_pension_20_num / years_retired):.2f} per year.\n Difference is ${(total_pen_drop_25 / (years_retired - 5) - (self.total_pension_20_num / years_retired)):.2f} per year."
        )

    def calculate_compare(self):
        # retrieve input values
        self.monthly_salary_lable.setText(
            f"Monthly Pension at 20 years is: ${self.monthly_pension:.2f} and at 25 years is: ${self.base_pension_25:.2f} and at 30 years is: ${self.base_pension_30:.2f}"
        )
        monthly_salary = self.monthly_pension
        hourly_rate = float(self.hourly_rate_input.text())
        hours_per_week = float(self.hours_per_week_input.text())

        # calculate equivalent hourly rate at 20 years
        equivalent_hourly_rate = monthly_salary / (4 * hours_per_week)
        difference = equivalent_hourly_rate - hourly_rate

        # calculate equivalent hourly rate to make difference bewteen 20 and 25 years
        equivalent_hourly_rate_diff = (self.base_pension_25 - monthly_salary) / (
            4 * hours_per_week
        )
        difference_diff = equivalent_hourly_rate_diff - hourly_rate

        # display result
        if difference <= 0:
            self.compare_result_label.setText(
                "You are already earning enough to meet or exceed your monthly pension."
            )
        else:
            self.compare_result_label.setText(
                f"You would need to make at least ${equivalent_hourly_rate:.2f} per hour to meet or exceed your monthly pension in total. \
                                               This is a difference of ${difference:.2f} per hour.\n \
                                               However, if you retire at 20 years with {monthly_salary:.2f} the equivalent hourly rate to make up the difference between 20 and 25 years is ${equivalent_hourly_rate_diff:.2f} per hour. \
                                               This is a difference of ${difference_diff:.2f} per hour."
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = PensionCalculator()
    calculator.show()
    sys.exit(app.exec_())
