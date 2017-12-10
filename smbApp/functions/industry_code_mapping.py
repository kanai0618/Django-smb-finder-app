import csv
import pandas as pd
# with open('/Users/sbhowmik/Desktop/smb-finder-data.csv', 'rb') as f:
#     reader = csv.reader(f, delimiter=';')
#     for row in reader:
        # print row[0]
def industry_type_mapping(code) :
    print code
    df = pd.read_csv('smbApp/Workbook2.csv')
    data_dict = {}

    for i in df.index :
        data_dict[df['code'][i].strip()] = df['data'][i]

    if str(code) in data_dict.keys() :
        return data_dict[code]
    elif str(code[:4]) in data_dict.keys() :
        return data_dict[code[:4]]
    elif str(code[:3]) in data_dict.keys() :
        return data_dict[code[:3]]
    else :
        return None
