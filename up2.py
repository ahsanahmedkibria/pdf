
import PyPDF2
import re

pdf_file = open('m.pdf', 'rb')  # Replace 'example.pdf' with the name of your PDF file
pdf_reader = PyPDF2.PdfReader(pdf_file)

abbreviations = []

# Loop through each page of the PDF document
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    page_text = page.extract_text()
    
    # Use regular expressions to find all the abbreviations on the page
    abbreviation_pattern = re.compile(r'\b[A-Z]+\b')
    abbreviations_on_page = abbreviation_pattern.findall(page_text)
    
    # Add the abbreviations on the page to the list of all abbreviations
    abbreviations.extend(abbreviations_on_page)

# Print the list of all abbreviations
#print(abbreviations)

abbreviations = list(set(abbreviations))
#print(abbreviations) # Output: [1, 2, 3, 4, 5, 6]


for i, abbr in enumerate(abbreviations):
    print(f"{i+1}. {abbr}")


import csv

#abbreviations = ['ABC', 'DEF', 'GHI']  # Replace with your list of abbreviations

# Create a new CSV file and write the abbreviations to it
with open('abbreviations.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Abbreviations'])
    for abbr in abbreviations:
        writer.writerow([abbr])

print('CSV file created successfully.')

