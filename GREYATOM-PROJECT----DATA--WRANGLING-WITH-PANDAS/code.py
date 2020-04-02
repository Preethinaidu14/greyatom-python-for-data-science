# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 

path

# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)

# code ends here


# --------------
# code starts here
banks = bank.drop('Loan_ID',axis = 1)
print(banks)
print(banks.isnull().sum())
bank_mode = banks.mode().iloc[0]
banks = banks.fillna(bank_mode)

#code ends here


# --------------
# Code starts here
avg_loan_amount = banks.pivot_table(index=['Gender','Married','Self_Employed'],values = 'LoanAmount')



# code ends here



# --------------
# code starts here



loan_approved_se = ((banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')).value_counts()
#print(loan_approved_se)
loan_approved_nse = ((banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')).value_counts()
print(loan_approved_nse)
Loan_Status = 614
percentage_se = (56/Loan_Status)*100
percentage_nse = (366/Loan_Status)*100




# code ends here


# --------------
# code starts here

loan_term = banks['Loan_Amount_Term'].apply (lambda x : int(x)/12)
print(loan_term.value_counts())
big_loan = [i for i in loan_term if i >= 25]
big_loan_term = len(big_loan)
print(big_loan_term)

#[loan_term.value_counts()[i] for i in range(len(loan_terms)) if loan_term.value_counts().index[i] >= 25]
# code ends here




# --------------
# code starts here
loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby['ApplicantIncome','Credit_History']
mean_values = loan_groupby.mean()


# code ends here


