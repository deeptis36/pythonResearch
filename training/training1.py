from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained GPT-2 model and tokenizer
model = GPT2LMHeadModel.from_pretrained('gpt2')
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# Define the prompt for generating EQ-related questions
prompt = "Laravel is a popular open-source PHP framework designed for web application development. It follows the Model-View-Controller (MVC) architectural pattern and provides an elegant syntax that makes it easier to build robust, maintainable web applications. Laravel aims to streamline common web development tasks such as routing, authentication, sessions, and caching, allowing developers to focus more on building their applications rather than handling low-level technical details."

# Tokenize the input prompt
inputs = tokenizer.encode(prompt, return_tensors='pt')

# Generate text using the model
outputs = model.generate(
    inputs, 
    max_length=50,       # Generate text up to 50 tokens long
    num_return_sequences=1,  # Generate one sequence
    no_repeat_ngram_size=2,  # Avoid repetition of phrases
    do_sample=True,          # Sample (randomness) instead of greedy decoding
    top_k=50,                # Limit the sampling pool to the top 50 tokens
    top_p=0.95               # Cumulative probability for nucleus sampling
)

# Decode the generated text
generated = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(generated)
