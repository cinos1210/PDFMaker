from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="letter")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Arial",style="B",size=24)
    pdf.set_text_color(100,100,100)
    topic = row["Topic"]
    pdf.cell(w=0,h=12,txt=topic,align="L",ln=1)
    pdf.line(10,23,200,23)

    for i in range(23,298,10):
        pdf.line(10, i, 200, i)

    #set footer
    pdf.ln(248)
    pdf.set_font(family="Arial",style="I",size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0,h=10,txt=row["Topic"],align="R")





    for i in range(row["Pages"] - 1):
        pdf.add_page()

        for i in range(10,298,10):
            pdf.line(10, i, 200, i)
        pdf.ln(258)
        pdf.set_font(family="Arial", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output2.pdf")