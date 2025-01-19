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
        taxcalc = (invqty/100 * total)
        st.write(f":blue[Tax: ${taxbar}]")
    with g:
        invtotal = st.text_input(":blue[Total Price]",disabled=True,placeholder=f"${total:,}")
        discountcal = (discount/100 * invprice)
        st.write(f":blue[Discount: ${discount}]")

        finaltotal = total-discountcal+taxcalc
    st.divider()
    h,i, = st.columns(2)
    with h:
        st.write(":blue[**Payment Info:**]")
        st.write(":blue[Acc Name: General Mills]")
        st.write(":blue[Acc Number: (204) 477-8338]")
        st.write(":blue[Bank Name: Td Canada]")

        def generat_pdf():
            pdf = FPDF()
            #--pageholder--#
            pdf.add_page() # Adds a page
            pdf.set_font("Courier",size=11,style="B") #font
            #--Columns pos--#
            colx = 10
            coly = 20
            #--imageholder--#
            pdf.image(imageholder,x=colx,y=coly)
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
                
    with i:
        st.write(":blue[**Payment Due**]")
        st.header(f":violet[${finaltotal}]")


if menu == "Change Detail":
    pass
