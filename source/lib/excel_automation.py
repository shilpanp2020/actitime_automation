import pandas as pd


def get_sheet(sheet):
    data_frame = pd.read_excel(".\\resources\\data\\actitime.xlsx",
                               sheet_name=sheet,
                               index_col="TestCaseID")
    return data_frame


def get_data(sheet, row_name, col_name):
    data_frame = get_sheet(sheet)
    value = data_frame.loc[row_name, col_name]
    return value
