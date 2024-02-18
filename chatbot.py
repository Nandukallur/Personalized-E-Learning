import os
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain import PromptTemplate

# Assign the OpenAI API key
openai_api_key = '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'

# Create an instance of the OpenAI class with the API key as a named parameter
llm = OpenAI(openai_api_key=openai_api_key, temperature=0.8)

while True:
    # Get user input
    input_text = input('Enter your query (type "exit" to quit): ')

    # Check if the user wants to exit
    if input_text.lower() == 'exit':
        print('Thank you for using Chatbot. Have a great day ahead')
        break
    elif input_text.lower() in ['hi', 'hai', 'hello', 'hy']:
        print('Hai, Welcome to Chatbot')
        continue  # Skip the prompt processing for greetings

    elif input_text.lower() in ['bye', 'by', 'goodbye', 'thank you', 'thanks']:
        print('Thank you for using Chatbot. Have a great day ahead.')

    # Create a prompt template based on user input
    input_prompt = PromptTemplate(input_variables=['query'], template='IT related {query}')

    # Create an instance of the LLMChain with the OpenAI instance and the prompt template
    chain = LLMChain(llm=llm, prompt=input_prompt, verbose=True)

    # Run the chain and print the result
    print(chain.run(input_text))
