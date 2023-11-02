import os.path
from pathlib import Path
from langchain.text_splitter import CharacterTextSplitter
import faiss
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
import pickle
import openai
from langchain import OpenAI, LLMChain
from langchain.prompts import Prompt


def train():
    trainingData = "trainer.txt"  # Adjusted to look for all files in subdirectories
    with open("trainer.txt", "r") as input_file:
        text = input_file.read()

    # Perform the desired word replacement
    text = text.replace("I", "you are")
    text = text.replace("my", "yours")

    # Open the output file for writing
    with open("trainer.txt", "w") as output_file:
        # Write the modified content to the output file
        output_file.write(text)

    data = []
    with open(trainingData) as f:
        data.append(f.read())

    textSplitter = CharacterTextSplitter(chunk_size=2000,
                                         separator="\n")  # Adjusted 'seprator' to 'separator' and '/n' to '\n'

    docs = []
    for sets in data:
        docs.extend(textSplitter.split_text(sets))
    store = FAISS.from_texts(docs,
                             OpenAIEmbeddings(openai_api_key="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"))

    faiss.write_index(store.index, "training.index")
    store.index = None
    with open("faiss.pkl", "wb") as f:
        pickle.dump(store, f)


class PromptClass():
    def prompt_function(self):
        index = faiss.read_index("training.index")
        with open("faiss.pkl", "rb") as f:
            self.store = pickle.load(f)
        self.store.index = index

        with open("trainer.txt", "r") as f:
            promptTemplate = f.read()

        self.prompt = Prompt(template=promptTemplate, input_variables=["history", "context", "question"])
        self.llmChain = LLMChain(prompt=self.prompt + "\n\n{question}", llm=OpenAI(temperature=0.25,
                                                                                   openai_api_key="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"))

    def onMessage(self, question = "", history=""):
        self.docs = self.store.similarity_search(question)
        contexts = []
        history = []
        while True:
            if question != "" or history != "":
                for i, doc in enumerate(self.docs):
                    contexts.append(f"Context{i}:\n{doc.page_content}")
                    answer = self.llmChain.predict(question=question, context="\n\n".join(contexts), history=history)
                    print(f"Bot: {answer}")

            history.append(f"Human:{question}")
            history.append(f"Bot: {answer}")
            return answer

    def execute(self, message):
        self.prompt_function()
        return self.onMessage(message)


def runPrompt(message):
    return PromptClass().execute(message)


train()
