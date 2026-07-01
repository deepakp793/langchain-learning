from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

splitter = RecursiveCharacterTextSplitter.from_language(
    language= Language.PYTHON,
    chunk_size = 100,
    chunk_overlap = 0
)

code ="""
class Employee:
    company = "ITC"
    def show(self):
        print(f"company name is : {self.company}")

class Programmer(Employee):
    language = "Python"
    company = "BPC"

class Developer(Programmer):
    tool = "langChain"

a = Programmer()
a.show()
print(a.language)
print(a.company)

b = Developer()
b.show()
print(b.company)
"""

result = splitter.split_text(code)

print(result[0])