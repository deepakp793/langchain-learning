from langchain_core.prompts import PromptTemplate

template= PromptTemplate(
    template = """Answer the question of this query '{chat_input}' but keep words minimum so not much tokens get spend on this.
    refer below chat history:
    '{chat_history}'
""",
input_variables=['chat_input','chat_history']
)

template.save('aitemplate.json')