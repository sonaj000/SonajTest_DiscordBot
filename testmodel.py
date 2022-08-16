import torch
import json
import random
from model import NeuralNet
from nltk_util import bag_of_words,tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('test.json','r') as f: #json file needs to be out of the same folder as the python scripts
    intents = json.load(f)
FILE = "data.pth"
data = torch.load(FILE)


input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
trigger_words = data['trigger_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

#this needs to be done a private dm not an open channel 
"""  if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        #run the bot chat here 
        while True:
            # sentence = "do you use credit cards?"
            sentence = message.content
            if message.content.startswith('$quit'):
                break

            sentence = tokenize(sentence)
            X = bag_of_words(sentence, trigger_words)
            X = X.reshape(1, X.shape[0])
            X = torch.from_numpy(X).to(device)

            output = model(X)
            _, predicted = torch.max(output, dim=1)

            tag = tags[predicted.item()]

            probs = torch.softmax(output, dim=1)
            prob = probs[0][predicted.item()]
            if prob.item() > 0.75:
                for intent in intents['intents']:
                    if tag == intent["tag"]:
                        await message.channel.send(random.choice(intent['responses']))
            else:
                await message.channel.send('what')"""