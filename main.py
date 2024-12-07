from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="letter")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Arial",style="B",size=24)
    pdf.set_text_color(100,100,100)
    topic = row["Topic"]
    pdf.cell(w=0,h=12,txt=topic,align="L",ln=1)
    pdf.line(10,23,200,23)
pdf.output("output.pdf")