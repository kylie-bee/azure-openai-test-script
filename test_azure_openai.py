import os
from typing import Any

from dotenv import load_dotenv
from openai import AzureOpenAI


def init_azure_client(endpoint: str, api_key: str) -> AzureOpenAI:
    """Initialize Azure OpenAI client."""
    return AzureOpenAI(
        azure_endpoint=endpoint, api_key=api_key, api_version="2024-02-15-preview"
    )


def test_completion(client: AzureOpenAI) -> dict[str, Any]:
    """Test completion API."""
    response = client.chat.completions.create(
        model="gpt-4",  # deployment name
        messages=[
            {"role": "user", "content": "Please generate a silly joke about computers."}
        ],
    )
    return response.model_dump()


def test_embedding(client: AzureOpenAI) -> dict[str, Any]:
    """Test embedding API."""
    response = client.embeddings.create(
        model="text-embedding-ada-002",  # deployment name
        input="Hello world",
    )
    return response.model_dump()


def main() -> None:
    """Main function to run tests."""
    # Load environment variables
    load_dotenv()

    # Test completion API
    completion_client = init_azure_client(
        os.getenv("AZURE_OPENAI_ENDPOINT", ""), os.getenv("AZURE_OPENAI_API_KEY", "")
    )

    # Test embedding API
    embedding_client = init_azure_client(
        os.getenv("AZURE_OPENAI_EMBEDDING_ENDPOINT", ""),
        os.getenv("AZURE_OPENAI_EMBEDDING_API_KEY", ""),
    )

    try:
        # Run completion test
        print("\nTesting Completion API...")
        completion_result = test_completion(completion_client)
        print("Completion test successful!")
        print(f"Response: {completion_result['choices'][0]['message']['content']}")

        # Run embedding test
        print("\nTesting Embedding API...")
        embedding_result = test_embedding(embedding_client)
        print("Embedding test successful!")
        print(f"Embedding dimension: {len(embedding_result['data'][0]['embedding'])}")

    except Exception as e:
        print(f"Error occurred: {str(e)}")


if __name__ == "__main__":
    main()
