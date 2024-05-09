# Simple Customer Support Chatbot
def greet():
    print("Hello! I'm your friendly customer support bot.")
    print("How can I assist you today?")

def respond_to_customer(input_message):
    if "order" in input_message:
        print("It sounds like you have a question about your order.")
        print("Please provide your order number so I can assist you further.")
    elif "issue" in input_message or "problem" in input_message:
        print("I'm sorry to hear that. Let me try to help.")
        print("Please provide more details about the issue you're experiencing.")
    elif "return" in input_message or "exchange" in input_message:
        print("For returns or exchanges, please refer to our return policy.")
        print("If you need further assistance, let me know.")
    else:
        print("I'm sorry, but I'm not sure how to assist with that.")
        print("Feel free to ask another question.")

def main():
    greet()
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "exit":
            print("Thank you for chatting with us. Goodbye!")
            break
        
        respond_to_customer(user_input)

if __name__ == "__main__":
    main()
