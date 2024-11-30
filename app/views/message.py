from app.scripts.get_response_from_model import get_response_from_model


def model_response(message) -> str:
    response = get_response_from_model(message.text)

    return response.content if hasattr(response, 'content') else str(response)


def waiting_for_response() -> str:
    return 'Waiting for the model to respond ⏳'