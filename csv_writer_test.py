import csv
  
fields = ['Employee', 'ID', 'Salary'] 
    
rows = [ ['XYZ', '011', '2000'], 
         ['ABC', '012', '8000'],
         ['PQR', '351', '5000'],
         ['EFG', '146', '10000'] ] 
  
with open('EmployeeData.csv', 'w', newline='', encoding='utf-8') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(fields)
    csv_writer.writerows(rows)