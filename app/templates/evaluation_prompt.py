def evaluation_prompt() -> str:
    return """
    Expected response: {expected_response}
    Actual response: {actual_response}
    ---
    (Answer with 'true' or 'false') Does the actual response match the expected response?
    """