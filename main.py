import fpdf
import pandas as pd
import os
import func

PATH_FILES = os.scandir('Invoice_files')

for e in PATH_FILES:
    
    total__total = 0

    # # Initialisation de la variables Total Price
    # total_price = None

    # # Bloc de traitement
    # qte = int(data_row[2])
    # unit_price = float(data_row[3])
    # total_price = qte*unit_price
    # total_price = f"{total_price:.2f}"
    
    pdf = fpdf.FPDF()
    # pdf.auto_page_break = False

    file_name = e.name[4:]
    file_path = e.path
    file_id_invoice = e.name.split('-')[0].split(' ')[1]
    invoice_date =e.name.replace('.xlsx',"")
    invoice_date = invoice_date.split('-')[1]
    
    df = pd.read_excel(file_path, header=0,decimal=".",engine="openpyxl")
    df.loc[:,"total_price"] = float(0)

    for r in range(len(df)):

        qte = df.iloc[r].get('amount_purchased')

        unit_price = df.iloc[r].get('price_per_unit')
        
        total_price = int(qte)*float(unit_price)

        total_price = float(total_price)

        total__total = total_price + float(total__total)

        total_price = f"{total_price:.2f}"

        df.loc[r:r,"total_price"] = total_price

    df_str = df.map(str)
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, text=f"Invoice N : {file_id_invoice}", align="L", ln=1)
    pdf.cell(w=50, h=8, text=f"Date : {invoice_date}", align="L", new_y="NEXT", new_x="LEFT")

    pdf.set_font(family='helvetica', size=10)

    # Convertir le DataFrame Pandas en une liste
    donnees_tableau = [list(x) for x in df_str.values]


    header = list(df_str.columns)


    header = [e.replace("_", " ").title() for e in header]


    donnees_tableau.insert(0, header)

    with pdf.table(align="LEFT", width=190, col_widths=(20,60,30,30,20)) as table:

        # Loop de traitement de données
        for data_row in donnees_tableau:

            row = table.row()

            for d in data_row:
                row.cell(d)

        row = table.row()
        row.cell(colspan=4)
        row.cell(str(f"{total__total:.2f}"))


    # pdf.set_margins()
    pdf.set_font(family="Times",size=14,style="B")
    pdf.cell(w=0,txt=" ",ln=1)
    pdf.cell(w=200,txt=f"The total due amount is {total__total:.2f} Euros.", ln=1)
    pdf.cell(w=200,txt=f"Python How",new_x="END")
    pdf.image(name="trident.png",dims=[30,30])

    pdf.output(f"{file_id_invoice}.pdf")