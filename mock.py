# importing the csv module
import csv
import names
import random
import datetime



def generate_mock_data(n):
    
    temp = 1900
    customer_id = temp + n

    randomDate = datetime.date(2023, 1, 1)
    transaction_date = randomDate + datetime.timedelta(days=random.randint(0, 366))
    
    # List of 
    bank_name = ['HDFC','PNB', 'SBI', 'AXIS', 'UNION']
    bank_index = random.randint(0, len(bank_name) - 1)
    # List of 
    debit_card_type = ['RuPay','MasterCard', 'VISA']
    debit_card_index = random.randint(0, len(debit_card_type) - 1)

 
    return {
        "customer_id": customer_id,
        "name": names.get_full_name(),
        "debit_card_number": random.randint(9000000000, 9999999999),
        "debit_card_type": debit_card_type[debit_card_index],
        "bank_name": bank_name[bank_index],
        "transaction_date": transaction_date,
        "amount_spend": random.randint(100, 5000)
    }

list_data = []

i=1
while(i<=10): #Enter no. of records which needs to be generated
    mock_data = generate_mock_data(i)
    list_data.append(mock_data)
    i += 1

# field names
fields = ['customer_id', 'name', 'debit_card_number', 'debit_card_type', 'bank_name', 'transaction_date', 'amount_spend' ]
 
# name of csv file
filename = "customer_transaction_2024_02_DD.csv"
 
# writing to csv file
with open(filename, 'w',  newline='') as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames=fields)
 
    # writing headers (field names)
    writer.writeheader()
 
    # writing data rows
    writer.writerows(list_data)



