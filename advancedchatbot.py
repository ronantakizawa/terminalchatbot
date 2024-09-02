#!/usr/bin/env python
import os
import openai
import itertools
import threading
import time


# Set up your OpenAI API key
openai.api_key = "OPEN-AI-API-KEY"

def get_chatgpt_response(prompt):
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that responds in both English and Spanish."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=4096,
        temperature=0.7,
    )
    return response.choices[0].message.content

def clear_screen():
    # Clears the terminal screen
    os.system('clear' if os.name == 'posix' else 'cls')

def loading_animation():
    while True:
        for cursor in '|/-\\':
            yield cursor

def main():
    clear_screen()
    print("Welcome to the ChatGPT CLI (English & Spanish)!")
    print("Type 'exit' to quit.\n")
    
    while True:
        prompt = input("You: ")
        if prompt.lower() == "exit":
            print("Goodbye!")
            break

        # Start the loading animation in a separate thread
        loading_gen = loading_animation()
        stop_event = threading.Event()

        def animate_loading():
            while not stop_event.is_set():
                print(f'\rChatGPT is thinking {next(loading_gen)}', end='')
                time.sleep(0.1)

        loading_thread = threading.Thread(target=animate_loading)
        loading_thread.start()

        response = get_chatgpt_response(prompt)

        stop_event.set()
        loading_thread.join()
        
        print(f"ChatGPT:\n{response}\n")

if __name__ == "__main__":
    main()
