from langchain.prompts.chat import ChatPromptTemplate
from langchain_ollama import OllamaChat

from app.scripts.pass_prompt_to_model import pass_prompt_template_to_model

from app.templates.evaluation_prompt import evaluation_prompt


def pass_evaluation_to_model(question: str, expected_response: str) -> bool:
    response_text = pass_prompt_template_to_model(question)

    PROMPT_TEMPLATE = evaluation_prompt()
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)

    prompt = prompt_template.format(
        expected_response=question,
        actual_response=response_text
    )

    model = OllamaChat(model='llama3:70b')
    evaluation_results = model.invoke(prompt)

    final_result = evaluation_results.strip().lower()

    if 'true' in final_result:
        return True
    elif 'false' in final_result:
        return False
    else:
        raise ValueError('Cannot determine if true or false')