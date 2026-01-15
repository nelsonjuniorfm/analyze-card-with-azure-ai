import streamlit as st
from services.blob_service import upload_blob
from services.credit_card_service import analyze_credit_card_document

def configure_interface():
    st.title("Upload Document for Fraud Detection using Azure Document Intelligence in Foundry Tools")
    uploaded_file = st.file_uploader("Upload your document here", type=["pdf", "png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        fileName = uploaded_file.name
        ## enviar para o blob do azure
        blob_url = upload_blob(uploaded_file, fileName)
        if blob_url:
            st.write(f"File successfully sent to Azure.: {fileName}")
            credit_card_info = analyze_credit_card_document(blob_url)
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write("Failed to upload the file to Azure.")


def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Image sent", use_column_width=True)
    st.write("Validating credit card information...")
    st.write(f"returno {credit_card_info}")
    if credit_card_info and credit_card_info["card_name"]:
        st.markdown(f"<h1 style='color: green;'>Valid Card</h1>", unsafe_allow_html=True)
        st.markdown(f"Cardholder Name: {credit_card_info['card_name']}")
        st.markdown(f"Card Number: {credit_card_info['card_number']}")
        st.markdown(f"Expiration Date: {credit_card_info['expiration_date']}")
    else:
        st.markdown(f"<h1 style='color: blue;'>Invalid card</h1>", unsafe_allow_html=True)
        st.write("The credit card information could not be validated.")

if __name__ == "__main__":
    configure_interface()