from langchain_text_splitters import CharacterTextSplitter

text = '''
CharacterTextSplitter is a LangChain utility that breaks large bodies of text into smaller, more manageable chunks based on a specific character or separator (like \n\n for paragraphs or   for words). It splits first by the separator, then merges pieces together until they hit a defined length limit.Key Parametersseparator: The character sequence used to split the text. (Default: \n\n).chunk_size: The maximum number of characters allowed in a single chunk.chunk_overlap: The number of characters shared between consecutive chunks to preserve context.
'''

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator=''
)

result = splitter.split_text(text)

print(result)