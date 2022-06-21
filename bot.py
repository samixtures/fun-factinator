import gspread

gc = gspread.service_account('credentials.json')

# Open a sheet from a spreadsheet in one go
wks = gc.open("google api").sheet1

# python-api@api-shtuff.iam.gserviceaccount.com

wks.update('A1', [[1, 2], [3, 4]])