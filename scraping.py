import requests
from bs4 import BeautifulSoup
from googlesearch import search
# import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def scrape_web_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        soup = BeautifulSoup(response.content, 'html.parser')
        text_data = ' '.join([p.get_text() for p in soup.find_all('p')]) 
        return text_data
    except (requests.exceptions.RequestException, requests.exceptions.HTTPError, Exception):
        return None  

def create_corpus(data_list):
    corpus = '\n'.join(data_list)
    return corpus

user_topic = input("Enter a topic: ")

search_results = list(search(user_topic, num_results=3))

if search_results:
    web_data_list = []
    for result in search_results:
        scraped_data = scrape_web_data(result)
        if scraped_data is not None:
            web_data_list.append(scraped_data)

    corpus = create_corpus(web_data_list)
    # print(corpus)

    corpus_length = len(corpus.split())
    print(f"Corpus Length: {corpus_length} words")
else:
    print("No relevant search results found.")



model_name = "gpt2"  
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)


text_data = corpus[:900]
responses = []
input_ids = tokenizer.encode(text_data, return_tensors="pt")
prompt = input("What do you want to ask the model? :  ")
input_text = text_data + " " + prompt
input_ids = tokenizer.encode(input_text, return_tensors="pt")

max_length = len(corpus)+ len(input_ids[0]) + 100  
output = model.generate(input_ids, max_length=max_length, num_return_sequences=1, no_repeat_ngram_size=2,pad_token_id=tokenizer.eos_token_id)
generated_response = tokenizer.decode(output[0][len(input_ids[0]):], skip_special_tokens=True)
print("Generated Response:", generated_response)
