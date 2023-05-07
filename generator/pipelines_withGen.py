""" Data, "techcrunch.csv"
permalink,company,numEmps,category,city,state,fundedDate,raisedAmt,raisedCurrency,round
digg,Digg,60,web,San Francisco,CA,1-Dec-06,8500000,USD,b
digg,Digg,60,web,San Francisco,CA,1-Oct-05,2800000,USD,a
facebook,Facebook,450,web,Palo Alto,CA,1-Sep-04,500000,USD,angel
facebook,Facebook,450,web,Palo Alto,CA,1-May-05,12700000,USD,a
photobucket,Photobucket,60,web,Palo Alto,CA,1-Mar-05,3000000,USD,a
"""
file_name = "techcrunch.csv"
lines = (line for line in open(file_name))    #reads in each line of the file
list_line = (s.rstrip()split(",") for s in lines)     # splits each line into values 
cols = next(list_line)      # uses next() to store the column names in a list
company_dicts = (dict(zip(cols, data)) for data in list_line)   
funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)
total_series_a = sum(funding)
print(f"Total series A fundraising: ${total_series_a}")
