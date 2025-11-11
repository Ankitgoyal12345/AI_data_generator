import requests
import json
from datetime import datetime
import os

prompt = """
Generate 10 rows of CSV data with columns:
claim_id (int), service_date (yyyy-mm-dd), amount (float with 2 decimals),
ward_type (string: 'General' or 'Private'), add_on (boolean).
Output only the CSV data without explanations.
"""

url = "http://localhost:11434/api/generate"

# Stream Ollama's output
with requests.post(url, json={"model": "mistral:7b", "prompt": prompt}, stream=True) as resp:
    full_response = ""
    for line in resp.iter_lines():
        if line:
            data = json.loads(line)
            if "response" in data:
                full_response += data["response"]
            if data.get("done"):
                break


timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_dir = os.path.expanduser("~/Desktop/docs/data_generator/test_data")  # folder on your Desktop
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, f"test_data_{timestamp}.csv")


with open(output_file, "w") as f:
    f.write(full_response.strip())

print(f"\n✅ Data generation complete! Saved to:\n{output_file}\n")


print("🔹 Preview of generated data:\n")
print("\n".join(full_response.splitlines()[:6]))
