from langchain.prompts.chat import ChatPromptTemplate
from langchain_ollama import ChatOllama

from app.scripts.get_prompt_template import get_prompt_template


def pass_prompt_template_to_model(context_text, query_text, sources) -> str:
    PROMT_TEMPLATE = get_prompt_template()
    prompt_template = ChatPromptTemplate.from_template(PROMT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, query=query_text)

    model = ChatOllama(model='llama3')
    
    response_text = model.invoke(prompt)

    return response_text