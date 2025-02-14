# Azure OpenAI Test Script

This script is used to test the Azure OpenAI API.

## Setup

```bash
pip install -r requirements.txt
```

Create a `.env` file and add the following:

```text
AZURE_OPENAI_ENDPOINT=https://<your-azure-openai-endpoint>.openai.azure.com
AZURE_OPENAI_API_KEY=<your-azure-openai-api-key>
AZURE_OPENAI_EMBEDDING_ENDPOINT=https://<your-azure-openai-embedding-endpoint>.openai.azure.com
AZURE_OPENAI_EMBEDDING_API_KEY=<your-azure-openai-embedding-api-key>
```

## Usage

```bash
python test_azure_openai.py
```

Example output:

```text
Testing Completion API...
Completion test successful!
Response: Sure, here's a silly computer joke for you:

Why did the computer go to therapy?

Because it had too many bytes!

Testing Embedding API...
Embedding test successful!
Embedding dimension: 1536
```

## Notes

- The script uses the Azure OpenAI API to generate a response to the prompt.
