import PyPDF2
import nltk

nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize, word_tokenize

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def answer_question(text, question):
    sentences = sent_tokenize(text)
    question_words = word_tokenize(question.lower())

    for sentence in sentences:
        for word in question_words:
            if word in sentence.lower():
                return sentence
    return "I couldn't find an answer to your question."

# Example usage
pdf_path = "/opt/render/project/src/Gaurav_Pandey_Resume.pdf"
text = extract_text_from_pdf(pdf_path)

while True:
    question = input("Ask your question: ")
    answer = answer_question(text, question)
    print(answer)