import pdfplumber
import csv
name = """\
N   I   L   E   S   H
/ / / / / / / / / / /
I                   I
/                   /
L                   L
/                   /
E                   E
/                   /
S                   S
/                   /
H / / / / / / / / / H
"""

print(name)


def pdf_to_csv(pdf_file, csv_file):
    with pdfplumber.open(pdf_file) as pdf:
        with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Date", "Purchaser Name", "Denomination"]) # Writing headers
            for page in pdf.pages:
                text = page.extract_text()
                lines = text.split('\n')
                for line in lines:
                    if line.strip(): # Ignore empty lines
                        parts = line.split() # Split the line into parts
                        if len(parts) >= 5: # Ensure there are enough parts
                            date = parts[0]
                            name = ' '.join(parts[1:-2]) # Join the name parts
                            denomination = parts[-1].replace(',', '') # Remove commas from the denomination
                            writer.writerow([date, name, denomination])

# Replace 'input.pdf' with your PDF file and 'output.csv' with the desired CSV file name
pdf_to_csv('bonddata.pdf', 'output1.csv')
