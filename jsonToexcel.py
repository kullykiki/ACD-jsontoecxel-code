import pandas
import os
import xlrd as xl
# acd_report =    [   'ACD_january2019',
#                     'ACD_february2019',
#                     'ACD_march2019',
#                     'ACD_april2019',
#                     'ACD_may2019',
#                     'ACD_june2019',
#                     'ACD_july2019',
#                     'ACD_august2019',
#                     'ACD_september2019',
#                     'ACD_october2019',
#                     'ACD_november2019',
#                     'ACD_december2019',
#                 ]

acd_report =    [   'ACD_january2020',
                    'ACD_february2020',
                    'ACD_march2020',
                    'ACD_april2020',
                    'ACD_may2020',
                    'ACD_june2020',
                    'ACD_july2020'
                ]

for file in acd_report:
    json_path = r"C:\Users\kully\Desktop\ACD_jsontoexcel_code\json file\2020"
    xlsx_path = r"C:\Users\kully\Desktop\ACD_jsontoexcel_code\excel file\2020"
    json_file = file  + '.json'
    xlsx_file =  file + '.xlsx'
    pandas.read_json(os.path.join(json_path, json_file)).to_excel(os.path.join(xlsx_path, xlsx_file), index=False)
    ff = xl.open_workbook(os.path.join(xlsx_path, xlsx_file))                    
    s1 = ff.sheet_by_index(0)                     
    s1.cell_value(0,0)
    print (f"{file} : {s1.nrows - 1} row")