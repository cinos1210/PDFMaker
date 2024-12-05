from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="letter")

pdf.add_page()

pdf.set_font(family="Arial",style="B",size=12)
pdf.cell(w=0,h=12,txt="HelloWorld",align="l",ln=1,border=1)

pdf.output("output.pdf")