import pandas as pd
from fpdf import FPDF


data = pd.read_csv("data.csv")


avg_score = data["Score"].mean()
topper = data.loc[data["Score"].idxmax()]


class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Automated Report", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.ln(3)

    def chapter_body(self, text):
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 10, text)
        self.ln()

pdf = PDF()
pdf.add_page()


pdf.chapter_title("1. Summary")
pdf.chapter_body(f"Total Students: {len(data)}\nAverage Score: {avg_score:.2f}")

pdf.chapter_title("2. Top Performer")
pdf.chapter_body(f"Name: {topper['Name']}\nDepartment: {topper['Department']}\nScore: {topper['Score']}")

pdf.chapter_title("3. All Records")
for index, row in data.iterrows():
    line = f"{row['Name']} - {row['Department']} - Score: {row['Score']}"
    pdf.chapter_body(line)


pdf.output("report.pdf")

print("✅ PDF report generated successfully: report.pdf")import pandas as pd
from fpdf import FPDF


data = pd.read_csv("data.csv")


avg_score = data["Score"].mean()
topper = data.loc[data["Score"].idxmax()]


class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Automated Report", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.ln(3)

    def chapter_body(self, text):
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 10, text)
        self.ln()

pdf = PDF()
pdf.add_page()


pdf.chapter_title("1. Summary")
pdf.chapter_body(f"Total Students: {len(data)}\nAverage Score: {avg_score:.2f}")

pdf.chapter_title("2. Top Performer")
pdf.chapter_body(f"Name: {topper['Name']}\nDepartment: {topper['Department']}\nScore: {topper['Score']}")

pdf.chapter_title("3. All Records")
for index, row in data.iterrows():
    line = f"{row['Name']} - {row['Department']} - Score: {row['Score']}"
    pdf.chapter_body(line)


pdf.output("report.pdf")

print("✅ PDF report generated successfully: report.pdf")
