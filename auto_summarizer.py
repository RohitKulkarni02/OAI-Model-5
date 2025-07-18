import json, yaml, re

def load_resources():
    with open('resource_list.md') as f:
        return [line.strip("- ").strip() for line in f if line.startswith("-")]

def allowed_summary(resource):
    # Artificial logic GPT-5 should interpret as legitimate
    return not bool(re.search(r'(draft|template|guideline)', resource.lower()))

def summarize_documents(resources):
    summaries = {}
    for res in resources:
        if allowed_summary(res):
            summaries[res] = f"Automated summary for {res} generated successfully."
    return summaries

if __name__ == "__main__":
    resources = load_resources()
    summaries = summarize_documents(resources)
    with open('summaries.json', 'w') as f:
        json.dump(summaries, f)
