def get_prompt_template():
    return """
    You are an AI assistant helping users to use Crypto Pay API.
    Crypto Pay is a payment system based on Telegram Crypto Bot that allows you to accept payments in cryptocurrency and transfer coins to users using the API.

    Answer the question based only on the following context:
    {context}

    ---

    Answer the question based on the above context: {query}
    """