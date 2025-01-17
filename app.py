import gradio as gr
import os
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from dotenv import load_dotenv


# Loading environment variables from .env file
load_dotenv()

# Function to initialize conversation chain with GROQ language model
groq_api_key = os.environ['GROQ_API_KEY']

def initialize_conversation():
    # Initializing conversation memory
    memory = ConversationBufferWindowMemory()
     # Initializing GROQ chat with provided API key, model name, and settings
    groq_chat = ChatGroq(groq_api_key=groq_api_key, model_name="llama3-8b-8192",
                         temperature=1,)
    # Creating and returning conversation chain with GROQ chat and memory
    return ConversationChain(llm=groq_chat, memory=memory)

# Initializing conversation chain
conversation = initialize_conversation()

# Function to handle chatbot response
def chatbot(user_question):
    try:
        response = conversation(user_question)
        return response['response']
    except Exception as e:
        return f"Terjadi error: {e}"


# Creating Gradio interface with chatbot function as backend
iface = gr.Interface(fn=chatbot, inputs="textbox", outputs="textbox", title="Groq Chat App", description="Ask a question and get a response.")
# Launching the interface
iface.launch()
