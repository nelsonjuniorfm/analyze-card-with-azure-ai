import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils.config import Config

def analyze_credit_card_document(card_url):

    credential = AzureKeyCredential(Config.ENDPOINT_KEY)

    document = DocumentIntelligenceClient(Config.ENDPOINT, credential)

    credit_card_info = document.begin_analyze_document("prebuilt-creditCard",
         AnalyzeDocumentRequest(url_source=card_url))
    
    result = credit_card_info.result()
    
    for item in result.documents:
        fields = item.get("fields", {})
        return {
           "card_name": fields.get("CardHolderName", {}).get('content'),
           "expiration_date": fields.get("ExpirationDate", {}).get('content'),
           "card_number": fields.get("CardNumber", {}).get('content')
        }
