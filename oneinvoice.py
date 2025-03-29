import streamlit as st
from fpdf import FPDF # python module to generate pdfs
import base64 # python module to convert binary data (my code) to printable character for the pdf
imageholder = "logo.png"

st.set_page_config(page_title="Invoice Generator",page_icon="📃",initial_sidebar_state="expanded")
menu = st.sidebar.selectbox("Menu",["Invoice Generator","Change Detail"])

if menu == "Invoice Generator":
    img1,img2,img3 = st.columns([2,1,1])
    st.sidebar.write("**OPTIONAL**")
    taxbar = st.sidebar.number_input("Enter Tax %")
    discount = st.sidebar.number_input("Enter Discount %")
    with img1:
        st.image(imageholder,width=100)
        st.write(":blue[General Mills]")
        st.write(":blue[1555 Chevrier Blvd, Winnipeg MB R3T1Y7]")
        st.write(":blue[Winnipeg, Manitoba]")
    with img3:
        st.write("")
        st.header(":blue[INVOICE]")

    st.write()
    a,b,c = st.columns([2,1,1])

    with a:
        cusname = st.text_input(":blue[**Bill To:**]",placeholder="Customer Name")
        cusemail = st.text_input("email",placeholder="Enter Email Adress",label_visibility="collapsed")
    
    with b:
        st.write("")
        st.write("")
        st.write(":blue[**Invoice:**]")
        st.write("")
        st.write(":blue[**Invoice date:**]")
        st.write("")
        st.write(":blue[**Due Date:**]")

    with c:
        st.write("")
        st.write("")
        invnum = st.text_input("Invoice Number",placeholder="Invoice Number",label_visibility="collapsed")
        invdate = st.date_input("invoice",label_visibility="collapsed")
        invduedate = st.date_input("invoice Due Date",label_visibility="collapsed")

    d,e,f,g = st.columns(4)

    with d:
        invdesc = st.text_input(":blue[Description]")
    with e:
        invqty = st.number_input(":blue[Quality]",0)
    with f:
        
        invprice = st.number_input(":blue[Price|Unit]",.0)
        total = invqty * invprice
        taxcalc = (taxbar/100 * total) #tax
        st.write(f":blue[Tax: ${taxbar}]")
    with g:
        invtotal = st.text_input(":blue[Total Price]",disabled=True,placeholder=f"${total:,}")
        discountcal = (discount/100 * total) #discount
        st.write(f":blue[Discount: ${discount}]")

        finaltotal = total-discountcal+taxcalc
    st.divider()
    h,i, = st.columns(2)
    with i:
        st.write(":blue[**Payment Due**]")
        st.header(f":violet[${finaltotal:,}]") 

    with h:
        st.write(":blue[**Payment Info:**]")
        st.write(":blue[Acc Name: General Mills]")
        st.write(":blue[Acc Number: (204) 477-8338]")
        st.write(":blue[Bank Name: Td Canada]")

        def generat_pdf():
            pdf = FPDF()
            #--pageholder--#
            pdf.add_page() # Adds a page
            pdf.set_font("Courier",size=12,style="B") #font
            #--Columns pos--#
            colx = 10
            coly = 20
            colw = 90
            #--imageholder--#
            pdf.image(imageholder,x=colx,y=coly,w=35)

            #invoice
            pdf.set_font(family= "Courier",size=20,style="B")
            pdf.set_xy(x=colx+130,y=coly+10)
            pdf.cell(colw,txt="Invoice",ln=True)

            #General Mills
            pdf.set_font(family= "Courier",size=16,style="B")
            pdf.set_xy(x=colx,y=coly+40)
            pdf.cell(colw,txt="General Mills",ln=True)

            #Address
            pdf.set_font(family= "Courier",size=14,style="B")
            pdf.set_xy(x=colx,y=coly+50)
            pdf.cell(colw,txt="1555 Chevrier Blvd, Winnipeg MB R3T1Y7",ln=True)

            #Country
            pdf.set_font(family= "Courier",size=14,style="B")
            pdf.set_xy(x=colx,y=coly+60)
            pdf.cell(colw,txt="Winnipeg, Manitoba",ln=True)

            #Bill TO
            pdf.set_font(family= "Courier",size=14,style="B")
            pdf.set_xy(x=colx,y=coly+80)
            pdf.cell(colw,txt="BILL TO:",ln=True)

            #Customer Name
            pdf.set_font(family= "Courier",size=14,style="B")
            pdf.set_xy(x=colx,y=coly+90)
            pdf.cell(colw,txt=f'{cusname}',ln=True)

            #Customer Email
            pdf.set_font(family= "Courier",size=14,style="B")
            pdf.set_xy(x=colx,y=coly+100)
            pdf.cell(colw,txt=f'{cusemail}',ln=True)

            #Invoice Number
            pdf.set_font(family= "Courier",size=14,style="B")
            pdf.set_xy(x=colx+130,y=coly+90)
            pdf.cell(colw,txt=f'Invoice: #{invnum}',ln=True)

            #Invoice Date
            pdf.set_font(family= "Courier",size=14,style="B")
            pdf.set_xy(x=colx+130,y=coly+100)
            pdf.cell(colw,txt=f'Invoice Date: {invdate}',ln=True)

            #Description
            pdf.set_font(family= "Courier",size=14,style="B")
            pdf.set_xy(x=colx,y=coly+125)
            pdf.cell(colw,txt=f'DESCRIPTION',ln=True)

            #Quantity
            pdf.set_font(family= "Courier",size=14,style="B")
            pdf.set_xy(x=colx+45,y=coly+125)
            pdf.cell(colw,txt=f'QUANTITY',ln=True)

            #Price|Unit
            pdf.set_font(family= "Courier",size=14,style="B")
            pdf.set_xy(x=colx+90,y=coly+125)
            pdf.cell(colw,txt=f'PRICE|UNIT',ln=True)

            #TotalPrice
            pdf.set_font(family= "Courier",size=14,style="B")
            pdf.set_xy(x=colx+135,y=coly+125)
            pdf.cell(colw,txt=f'TOTAL PRICE',ln=True)

            #Draw A line ---
            pdf.set_line_width(0.5)
            pdf.line(colx,coly+130, colx+170,coly+130)

            #Product
            pdf.set_font(family= "Courier",size=14,style="B")
            pdf.set_xy(x=colx,y=coly+135)
            pdf.cell(colw,txt=f'{invdesc}',ln=True)

            #ProductQuantity
            pdf.set_font(family= "Courier",size=14,style="B")
            pdf.set_xy(x=colx+45,y=coly+135)
            pdf.cell(colw,txt=f'{invqty}',ln=True) 

            #ProductPrice|Unit
            pdf.set_font(family= "Courier",size=14,style="B")
            pdf.set_xy(x=colx+90,y=coly+135)
            pdf.cell(colw,txt=f'{invprice:,}',ln=True)

            #TotalPrice
            pdf.set_font(family= "Courier",size=14,style="B")
            pdf.set_xy(x=colx+135,y=coly+135)
            pdf.cell(colw,txt=f'{finaltotal:,}',ln=True)

            #Discount
            pdf.set_font(family= "Courier",size=14,style="B")
            pdf.set_xy(x=colx+135,y=coly+140)
            pdf.cell(colw,txt=f'Tax: {taxbar:,}',ln=True)

            #Tax
            pdf.set_font(family= "Courier",size=14,style="B")
            pdf.set_xy(x=colx+135,y=coly+145)
            pdf.cell(colw,txt=f'Discount: {discount:,}',ln=True)

            #----#
            pdf_file = "logo.pdf"
            pdf.output(pdf_file)
            return pdf_file
            


        if st.button("View Invoice"):
            pdf_function = generat_pdf() # generates pdf

            with open(pdf_function, "rb") as binary: # read the bdf function as a binary data
                read_pdf = binary.read()

                write_pdf = base64.b64encode(read_pdf).decode("utf-8") # write the pdf using base64

                #Generate HTML page to view the PDF
                view_pdf = f'<embed src="data:application/pdf;base64,{write_pdf}" type="application/pdf" width="100%" height="600px" />'

                st.markdown(view_pdf,unsafe_allow_html=True)

#            if (cusname and cusemail and invnum and invdesc and invprice and invqty):
#                pass
#            else:
#                st.error("Kindly Fill All Boxes")

if menu == "Change Detail":
    pass
