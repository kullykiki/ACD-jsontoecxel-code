import pandas

acd_report =    [   'ACD_january2019',
                    'ACD_february2019',
                    'ACD_march2019',
                    'ACD_april2019',
                    'ACD_may2019',
                    'ACD_june2019',
                    'ACD_july2019',
                    'ACD_august2019',
                    'ACD_september2019',
                    'ACD_october2019',
                    'ACD_november2019',
                    'ACD_december2019',
                ]

for file in acd_report:
    file_js = '"' + file + ".json" + '"'
    file_xlsx = '"' + file + ".xlsx" + '"'
    # pandas.read_json("ACD_january2020.json").to_excel("ACD_january2020.xlsx", index=False)
    print(f'command : pandas.read_json({file_js}).to_excel({file_xlsx}, index=False)')