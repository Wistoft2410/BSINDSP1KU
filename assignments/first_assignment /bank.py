#-----------------------------------------------------------------------
# <copyright file="D:/Users/computer/Desktop/data science/Mandatory courses/Introduction to Data Science and Programming/assignments/Bank - No. 1/bank.py">
#     Author: Adam Isaac
#     ITU mail: adiw@itu.dk
#     Copyright (c) Developer Express. All rights reserved.
# </copyright>
#-----------------------------------------------------------------------

import math 

def calculate_balance(transactions):
	#write your function here
	sum = 0

	for i in range(0, len(transactions)):
		sum = sum + transactions[i]

	return sum


def calculate_compound(account_balance, rate, years):
	#write your function here
	sum = 0
	sum = account_balance * (1+ rate)**years

	return sum

def filter_withdrawals(transactions):
	#write your function here
	sum_list = []
	for i in range(0, len(transactions)):
		if transactions[i] < 0: 
			sum_list.append(transactions[i])

	return sum_list

def risk_analysis(transactions):
	#write your function here
	sum_list = []
	for i in range(0, len(transactions)):
		if transactions[i-1] > i:
			sum_list.append(transactions[i])

	return sum_list

def join_records(names, transactions):
	#write your function here
	
	return 

def unique_deposit_names(joined_transactions):
	#write your function here

	return	

def main():
	#calculate balance example
	transactions = [100 , 5000 , -30, -1200]
	balance = calculate_balance(transactions)
	print(balance) #Expected output: 3870

	#calculate compound example
	compound_balance = calculate_compound(500 , 0.05 , 25)
	print(compound_balance) #Expected outuput: 1693.17[...]

	#filter withdrawals example
	withdrawals = filter_withdrawals(transactions)
	print(withdrawals) #Expected outuput: [-30, -1200]

	#risk analysis example 
	transactions = [-5000, 200, 120, 120, -99999] 
	risk = risk_analysis(transactions)
	print(risk)#Expected outuput: -99999

	#join records example
	names = ['Muhammed', 'emma', 'Emma', 'Maria', 'julie']
	joined_transactions = join_records(names, transactions)
	print(joined_transactions)#Expected outuput: [( ’Muhammed’, −5000), ( ’emma’ , 200), ( ’Emma’ , 120), ( ’Maria’ , 120), ( ’ julie ’ , −99999)]

	#unique deposit names example
	unique_names = unique_deposit_names(joined_transactions)
	print(unique_names) #Expected outuput: ['emma', 'maria'] #order does not matter


if __name__ == "__main__":
	# execute only if run as a script
	main()
	#Expected output:
	#3870
	#1693.17[...]
	#-99999
	#[( ’Muhammed’, −5000), ( ’emma’ , 200), ( ’Emma’ , 120), ( ’Maria’ , 120), ( ’ julie ’ , −99999)]
	#['emma', 'maria'] #order does not matter

