import openpyxl

def get_data():
    workbook = openpyxl.load_workbook("C://Selenium_E26/Demo_Tricentis_Framework/test_data/login_data.xlsx")
    sheet = workbook["Sheet1"]

    data = []

    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append(row)

    return data




