
import streamlit as st

class PersonalInfo():
    def __init__(self, age):
        self.age = age
        
    def customer_age(self):
        if self.age < 25:
            points = 0
        elif self.age > 25 and self.age < 35:
            points = 10
        elif self.age > 35 and self.age < 50:
            points = 20
        else:
            points = 15
        return points  
    
class EmploymentInfo():
    def __init__(self, status):
        self.status = status
    
    def employment_status(self):
        if self.status == 'unemployed':
            points = 0
        elif self.status == 'self-employed':
            points = 10
        elif self.status == 'employed: < 1 year':
            points = 15
        elif self.status == 'employed: 1-3 years':
            points = 20
        else:
            points =25 

        return points
    
class FinancialInfo():
    def __init__(self, income, ratio):
        self.income = income
        self.ratio = ratio
        
    def annual_income(self):
        if self.income < 30000:
            points = 0
        elif self.income > 30000 and self.income < 50000:
            points = 10
        elif self.income > 50000 and self.income < 75000:
            points = 20
        else: 
            points = 30
        return points
    
    def debt_income(self):
        if self.ratio > (0.5 *100):
            points = 0
        elif self.ratio > (0.4 * 100) and self.ratio < (0.5 * 100):
            points = 10
        elif self.ratio > (0.3 * 100) and self.ratio < (0.39 * 100):
            points = 20
        else:
            points = 30
        return points
    
class CreditHistory():
    def __init__(self, score, utilization):
        self.score = score
        self.utilization = utilization
        
    def credit_score(self):
        if self.score < 600:
            points = 0
        elif self.score > 600 and self.score < 649:
            points = 10
        elif self.score > 650 and self.score < 699:
            points = 20
        else:
            points = 25
        return points
    
    def credit_utilization(self):
        if self.utilization > (0.5 * 100):
            points = 0
        elif self.utilization > (0.3 * 100) and self.utilization < (0.49 * 100):
            points = 10
        elif self.utilization > (0.1 * 100) and self.utilization < (0.29 * 100):
            points = 20
        else:
            points = 25
        return points
    
class ExpertScore():
    def __init__(self, age, status, income, ratio, score, utilization):
        self.personal_info = PersonalInfo(age)
        self.employment_info = EmploymentInfo(status)
        self.financial_info = FinancialInfo(income, ratio)
        self.credit_history = CreditHistory(score, utilization)
    
    def credit_score(self):
        total_score = (self.personal_info.customer_age() + 
                       self.employment_info.employment_status()+
                       self.financial_info.annual_income() +
                       self.financial_info.debt_income()+
                       self.credit_history.credit_score()+
                       self.credit_history.credit_utilization())
                           
        if total_score > 120 and total_score < 150:
            print(f"total score is {total_score}, High creditworthiness, low risk")
        elif total_score >90 and total_score < 120:
            print(f"total score is {total_score}, Moderate creditworthiness, moderate risk")
        else:
            return f"total score is {total_score},Low creditworthiness, high risk "   
 

def main():
    st.title("Credit Score Calculator")

    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    status = st.selectbox("Employment Status", ['unemployed', 'self-employed', 'employed: < 1 year', 'employed: 1-3 years', 'employed: > 3 years'])
    income = st.number_input("Annual Income", min_value=0)
    ratio = st.number_input("Debt-to-Income Ratio (as percentage)", min_value=0.0, max_value=100.0)
    score = st.number_input("Credit Score", min_value=0, max_value=850)
    utilization = st.number_input("Credit Utilization Ratio (as percentage)", min_value=0.0, max_value=100.0)

    if st.button("Calculate Credit Score"):
        expert = ExpertScore(age, status, income, ratio, score, utilization)
        result = expert.credit_score()
        st.write(result)

if __name__ == "__main__":
    main()
