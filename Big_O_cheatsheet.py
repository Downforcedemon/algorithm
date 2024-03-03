from fpdf import FPDF

# Creating instance of FPDF class
pdf = FPDF()

# Adding a page
pdf.add_page()

# Setting font: Arial bold, 16
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, 'Java Big-O Notation Cheat Sheet for Data Structures', ln=True, align='C')

# Line break
pdf.ln(10)

# Setting font: Arial, 12
pdf.set_font("Arial", size=12)

# Adding content
content = """
Data Structure      | Average Time Complexity
--------------------|------------------------
Array
    Access          | O(1)
    Search          | O(n)
    Insertion       | O(n)
    Deletion        | O(n)
LinkedList
    Access          | O(n)
    Search          | O(n)
    Insertion       | O(1)
    Deletion        | O(1)
Stack
    Access          | O(n)
    Search          | O(n)
    Insertion       | O(1)
    Deletion        | O(1)
Queue
    Access          | O(n)
    Search          | O(n)
    Insertion       | O(1)
    Deletion        | O(1)
HashMap
    Access          | -
    Search          | O(1)*
    Insertion       | O(1)*
    Deletion        | O(1)*
Binary Search Tree
    Access          | O(log n)
    Search          | O(log n)
    Insertion       | O(log n)
    Deletion        | O(log n)
Heap
    Access (Min/Max) | O(1)
    Search          | O(n)
    Insertion       | O(log n)
    Deletion (Min/Max) | O(log n)

* Average case time complexity
"""

# Splitting content into lines and writing to PDF
for line in content.split('\n'):
    pdf.cell(0, 10, line, ln=True)

# Saving the PDF to a file
pdf_file_path = "/mnt/data/Java_Big-O_Notation_Cheat_Sheet.pdf"
pdf.output(pdf_file_path)

pdf_file_path
