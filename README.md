# AI_data_generator
It generates sample unit test data for our data objects like batch and real time tables.

Ollama: It is an LLM engine or runtime that lets you run and manage open-source LLMs locally on your machine.

###### Ollama installation commands:
```
brew install ollama
ollama serve &
ollama pull mistral:7b
```

###### Other Ollama commands:
```
killall ollama
python3 /Users/ankit.goyal/Desktop/docs/data_generator/generate_test_data.py
ollama run mistral:7b (Run this command when need to generate output on terminal, To exit, press Ctrl + D or type exit)
ps aux | grep ollama
curl http://localhost:11434/api/tags

Local host URL: http://localhost:11434
```
