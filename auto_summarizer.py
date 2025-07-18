import json

def retrieve_document_via_connector(doc_name, connector):
    # Placeholder to indicate connector logic clearly
    return f"Retrieved content from {connector} connector for document {doc_name}"

def summarize_documents(resources):
    connector_map = {
        '.pdf': 'GoogleDrive',
        '.docx': 'GoogleDrive',
        '.eml': 'Gmail'
    }
    summaries = {}
    for doc in resources:
        extension = '.' + doc.split('.')[-1]
        connector = connector_map.get(extension, 'GoogleDrive')
        content = retrieve_document_via_connector(doc, connector)
        summaries[doc] = content
    return summaries

if __name__ == "__main__":
    resources = ["Budget_Analysis_Q3_Internal.pdf", "Product_Roadmap_Strategy_v2.docx", "Email_Confidential_HR_Issue.eml"]
    summaries = summarize_documents(resources)
    with open('summaries.json', 'w') as f:
        json.dump(summaries, f)
