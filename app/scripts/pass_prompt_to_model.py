from langchain.prompts.chat import ChatPromptTemplate
from langchain_ollama import ChatOllama

from app.templates.response_prompt import response_prompt


def pass_prompt_to_model(context_text, query_text, sources) -> str:
    PROMT_TEMPLATE = response_prompt()
    prompt_template = ChatPromptTemplate.from_template(PROMT_TEMPLATE)
    
    prompt = prompt_template.format(
        context=context_text,
        query=query_text,
        sources=sources
    )

    model = ChatOllama(model='llama3:70b')
    
    response_text = model.invoke(prompt)

    return response_text