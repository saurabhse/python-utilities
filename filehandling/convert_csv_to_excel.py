import openpyxl

wb = openpypxml.Workbook()
ws = ws.active

f = open("csv_file")
reader = csv.reader(f,delimiter=',')
for row in reader:
  ws.append(row)
f.close()
wb.save("file.xslx')

