import csv
import os
import datetime
import re


dir_path = os.path.dirname(os.path.abspath(__file__))
print(dir_path)
os.chdir(dir_path)

employee_data = os.path.join("employee_data.csv")
print(employee_data)

employee_ids = []
first_name = []
last_name = []
new_dob = []
new_ssn = []
state = []


us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

with open(employee_data, "r", encoding="utf-8") as csvfile:
    csvReader = csv.reader(csvfile,delimiter=",")
    print(csvReader)
    next(csvfile)

    for row in csvReader:

                #for employee ID's
        employee_ids = employee_ids + [row[0]]
#print(employee_ids)

        #Split 1st and last name
        name = row[1].split(' ')
        first_name.append(name[0])
        last_name.append(name[1])

        #Convert DOB
        dob = row[2]
        formatDOB = datetime.datetime.strptime(dob, '%Y-%m-%d').strftime('%m/%d/%Y')
        new_dob.append(formatDOB)

        #Convert SN
        ssn = row[3]
        reformat_ssn = re.sub(r'\d', '*', ssn, count=5)
        new_ssn.append(reformat_ssn)

        #Convert state name
        state_abbrev = us_state_abbrev[row[4]]
        state.append(state_abbrev)

new_employee_format = zip(employee_ids, first_name, last_name, new_dob,new_ssn, state)

output_file = os.path.join("analysis", "new_employee_format.csv")

with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Employee ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    writer.writerows(new_employee_format)



#print(tuple(new_employee_format))
#print(state)
#print(state_abbrev)
#print(split_ssn)
#print(formatDOB)        
#print(new_dob)        
#print(name)
#print(first_name)
#print(last_name)