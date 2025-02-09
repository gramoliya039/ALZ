import os
import json
from google.cloud import aiplatform

print("Imported successfully...")

# Initialize Vertex AI
aiplatform.init(project="your-gcp-project-id", location="us-central1")

# Define the prompt
prompt = """
    You are a cricket expert. Now just tell me when RCB will win the IPL?
"""

# Define the model ID for Llama 3 on GCP
model_id = "llama3_1-70b"  # Change to "llama3_1-8b" if needed

# Load the model from Vertex AI
model = aiplatform.generation.TextGenerationModel.from_pretrained(model_id)

# Generate the response
response = model.predict(prompt, temperature=0.3, max_output_tokens=512, top_p=0.9)

# Print the response
print(response.text)
