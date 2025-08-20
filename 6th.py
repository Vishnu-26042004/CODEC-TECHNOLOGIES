def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "store hours" in user_input:
        return "Our store is open from 9 AM to 9 PM, Monday to Saturday."
    elif "return" in user_input:
        return "You can return products within 30 days of purchase with the bill."
    elif "contact" in user_input or "support" in user_input:
        return "You can reach our support at support@example.com or call 1800-123-456."
    elif "track order" in user_input or "where is my order" in user_input:
        return "You can track your order using the tracking link sent to your email."
    elif "cancel order" in user_input:
        return "To cancel an order, go to 'My Orders' and select the cancel option."
    elif "payment options" in user_input or "how can i pay" in user_input:
        return "We accept Credit/Debit Cards, UPI, Net Banking, and Cash on Delivery."
    elif "warranty" in user_input:
        return "Most products come with a 1-year manufacturer warranty. Check product details for specifics."
    elif "delivery time" in user_input or "when will it arrive" in user_input:
        return "Delivery usually takes 3-5 business days depending on your location."
    elif "discount" in user_input or "coupon" in user_input:
        return "You can apply available coupons at checkout. Check our Offers page for discounts."
    elif "lost password" in user_input or "forgot password" in user_input:
        return "Click on 'Forgot Password' on the login page to reset it."
    elif "bye" in user_input or "exit" in user_input:
        return "Thank you for visiting! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Chat loop
print("🤖 Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['bye', 'exit']:
        print("🤖 Chatbot: Thank you for visiting! Have a great day!")
        break
    response = chatbot_response(user_input)
    print("🤖 Chatbot:", response)
