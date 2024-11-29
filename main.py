import os
import argparse

from dotenv import load_dotenv, find_dotenv

from scripts.load_query_from_chroma import load_query_from_chroma
from scripts.pass_prompt_template_to_model import pass_prompt_template_to_model


def main():
    load_dotenv(find_dotenv())

    chroma_path = os.getenv("CHROMA_PATH")

    parser = argparse.ArgumentParser()
    parser.add_argument('query_text', type=str, help='Query text')
    args = parser.parse_args()
    query_text = args.query_text

    result = load_query_from_chroma(chroma_path, query_text)

    context_text = '\n\n---\n\n'.join([
        document.page_content for document, _score in result
    ])
    sources = [
        document.metadata.get('source', None) for document, _score in result
    ]

    model_response = pass_prompt_template_to_model(context_text, query_text, sources)

    print(model_response)


if __name__ == "__main__":
    main()