from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0
)

text = """
CharacterTextSplitter is a LangChain utility that breaks large bodies of text into smaller, more manageable chunks based on a specific character or separator (like nn for paragraphs or for words). 
It splits first by the separator, then merges pieces together until they hit a defined length limit.
Key Parametersseparator: The character sequence used to split the text. (Default:nn).
chunk_size: The maximum number of characters allowed in a single chunk.chunk_overlap: The number of characters shared between consecutive chunks to preserve context.
"""

result = splitter.split_text(text)

print(result[0])
print('***------------------***')
print(result[1])