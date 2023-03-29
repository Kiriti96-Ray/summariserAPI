# -*- coding: cp1252 -*-
import openai
import os
import re

# Set up your OpenAI API credentials
openai.api_key = <#open_ai_key#>

def summariser(text):
    text = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "",text)
    # Send the request to the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant, so write a concise & intelligent summary of the given context"},
            {"role": "user", "content": text}],
        max_tokens=256,
        temperature=0.1)

    # Extract the summary from the response
    return response['choices'][0]['message']['content']
