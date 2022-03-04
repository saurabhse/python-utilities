'''
csv file
col1;col2
1;2
'''
import csv

def new_column():
    filename = "old_file.csv"
    new_file = "new_file.csv"
    with open(filename, "r") as infile, open(new_file, "w") as outfile:
        reader = csv.reader(infile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer = csv.writer(outfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        header = next(reader)
        header.append('new_col')
        writer.writerow(header)
        for row in reader:
            col1, col2 = tuple(row)
            new_col_val = 3
            row.append(new_col_val)
            writer.writerow(row)

if __name__ == "__main__":
    new_column()
