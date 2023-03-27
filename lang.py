# -*- coding: cp1252 -*-
import openai
import os
import re

# Set up your OpenAI API credentials
openai.api_key = "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"

def summariser(text):
  #  text = "Hi there,Are your ML and CV teams delivering value or spending most of their time managing and processing training data?We believe AI teams that get ahead are workflow-centric, consistently solving real business problems while designing clear processes for humans, models, and data to do their best work together.If higher speed and deliverability are a priority for your team, we'd love for you to join our live webinar on March 28 at 5 PM GMT | 12 PM ET | 9 AM PT.One of V7’s most experienced AI Researchers, Thomas Varsavsky, and our Head of Sales, Matt Brown, will show how training data pipelines and V7's workflows can drive fast, accurate, and iterative AI in your business.What to expect in our 45-minute webinar"
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
    #print(response['choices'][0]['message']['content'])
    return response['choices'][0]['message']['content']