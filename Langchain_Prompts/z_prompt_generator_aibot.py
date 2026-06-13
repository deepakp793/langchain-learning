from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.load import dumps, load

template= ChatPromptTemplate.from_messages([
    ('system',"You are a career guide. Please guide on career. Use minimum words to generate response"),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

json_string = dumps(template, pretty= True)

with open('z_aitemplate.json', 'w') as f:
    f.write(json_string)