import streamlit as st 
from groqai import generate_response
#from hf import generate_response
def get_answer(question):
    prompt=f"""
    Answer the question clearly in numbered points.
    Complete every sentence and do not stop midway.
    
    Question: (question)
    """
    answer=generate_response(prompt, temperature=0.3, max_tokens=2048)
    #If answer seems incomplete, ask AI to continue
    if answer and not answer.rstrip().endswith((".", "!", "?")):
        answer+="\n"+generate_response(f"Continue the answer without repeating anything: \n{answer}",
                                       temperature=0.3,
                                       max_tokens=2048
        )
    print("abcd")
print("AI teaching assistant")
print("Ask a question and get a clear AI generated answer")
question=input("Enter you question :")
if question: 
    print("**Your Question**", question)
    print("**AI's answer: **")
    get_answer(question)
          