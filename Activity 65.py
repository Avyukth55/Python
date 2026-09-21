from ai_model import generate_response

def ai_response(prompt):
    return generate_response(prompt, temperature=0.3, max_tokens=1024)

def teaching_assistant():
    question=input("\nEnter your question:")
    if question:
        print("\nAI Answer:")
        print(ai_response(question))

def math_mastermind():
    problem=input("\nEnter a Math Problem")
    level=input("Difficulty (Basic/Intermediate/Advanced): ")
    prompt= f"""
    You are a Math Mastermind
    Solve the problem step-by-step.
    Difficulty: {level}
    Problem: {problem}
    """
    print("\nSolution:")
    print(ai_response(prompt))

def main():
    while True:
        print("\n********AI LEARNING APP********")
        print("1. AI Teaching Assistant")
        print("2. Math Mastermind")
        print("3. Exit")
        choice=input("\nChoose an option: ")
        if choice=="1":
            teaching_assistant()
        if choice=="1":
            math_mastermind()
        elif choice=="3":
            print("Thank you")
            break;
        else:
            print("Invalid choice. Try again.")
if __name__=="__main__":
    main()