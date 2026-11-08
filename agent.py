# agent.py
import sys
from google import genai
import config
import tools

tools.ensure_workspace()
client = genai.Client(api_key=config.API_KEY)

print("=== Autonomous Agent: File Analyzer ===")
file_name = input("Target filename in /workspace (e.g., sample.txt): ").strip()

content = tools.read_workspace_file(file_name)

if content.startswith("Error:"):
    print(content)
    sys.exit()

print(f"\nProcessing '{file_name}'...")

prompt = f"""
You are an executive assistant and software analyst.
Analyze the following document:
---
{content}
---

Your output must follow this strict structure:
1. One-Sentence Punchline (What is happening?)
2. Top 3 Critical Insights (Bullet points)
3. Action Plan (Max 2 sentences)
"""

response = client.models.generate_content(
    model=config.MODEL_NAME,
    contents=prompt
)

# 1. Save the full analysis
output_filename = f"analysis_{file_name}"
tools.write_workspace_file(output_filename, response.text)

# 2. Print short, clean summary directly in console
print("\n" + "=" * 50)
print("EXECUTIVE SUMMARY (Directly from Agent):")
print("=" * 50)
print(response.text)
print("=" * 50)
print(f"Full report saved to workspace/{output_filename}\n")