from fpdf import FPDF

def main():
    shirt(input("Name: "))

def shirt(n):
    # pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_title("CS50 Shirtificate")
    pdf.image("shirtificate.png", x=10, y=70, w=190)
    pdf.set_font("helvetica", "B", 40)
    # pdf.set_text_color(0, 0, 0)
    pdf.set_xy(5, 25)
    pdf.cell(210, 20, "CS50 Shirtificate", align="C")
    pdf.set_font("helvetica", "B", 30)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(2, 110)
    pdf.cell(210, 20, f"{n} took CS50", align="C")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()