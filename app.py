from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors 
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

sheet = [
        ["UserName", "Email","ITEM", "PAYMENT DATE", "AMOUNT"],
        ["dummyuser1", "dummyuser1@dummy.txt","Python Book", "2000-01-01", "RS 2000"],
        ["dummyuser2", "dummyuser2@dummy.txt","MySql Book", "2000-01-02", "RS 3000"],
        ["dummyuser3", "dummyuser3@dummy.txt","Computer vision", "2000-01-03", "RS 2500"],
        ["dummyuser4", "dummyuser4@dummy.txt","Javascript", "2000-01-04", "RS 2100"],
        ["dummyuser5", "dummyuser5@dummy.txt","Machine Learning", "2000-01-05", "RS 2200"],
    ]


pdf = SimpleDocTemplate("user_transaction.pdf",pagesize=A4)

styles = getSampleStyleSheet()

title_style = styles['Heading1']
title_style.alignment = 0

title = Paragraph("User Transactions", title_style)

style = TableStyle( 
    [ 
        ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ), 
        ( "GRID" , ( 0, 0 ), ( 5 , 5 ), 0 , colors.black ), 
        ( "BACKGROUND" , ( 0, 0 ), ( 5, 0 ), colors.gray ), 
        ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ), 
        ( "BACKGROUND" , ( 0 , 0 ) , ( -1 , -1 ), colors.beige ), 
    ] 
) 

table = Table(sheet, style=style)

pdf.build([title, table])