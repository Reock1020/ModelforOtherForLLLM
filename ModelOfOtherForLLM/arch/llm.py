import os
import openai

openai.api_key = 

class LLM():
    def __init__(self, gpt_version="gpt-4") -> None:
        self.gpt_version = gpt_version

    def simple_llm(self,docstring, **params_data):
        prompt = docstring

        for key ,value in params_data.items():
            prompt += f"{key}: {value},"
        # print(prompt)

        messages = [{"role": "system", "content": "You are a helpful assistant."},{"role":"user","content":prompt}]
        # print(messages)
        responses = openai.ChatCompletion.create(
            model = self.gpt_version,
            messages=messages,
            temperature=0.6
        )
        text = responses['choices'][0]['message']['content']
        return text
    
    
