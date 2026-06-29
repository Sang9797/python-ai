from transformers import AutoTokenizer

def get_tokenizer(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return tokenizer;

def tokenize_text(text):
    tokenizer = get_tokenizer("bert-base-uncased")
    tokens = tokenizer.tokenize(text)
    return tokens

def encode_tokens(tokens):
    tokenizer = get_tokenizer("bert-base-uncased")
    encoded_tokens = tokenizer.convert_tokens_to_ids(tokens)
    return encoded_tokens

def decode_tokens(tokens):
    tokenizer = get_tokenizer("bert-base-uncased")
    decoded_text = tokenizer.convert_tokens_to_string(tokens)
    return decoded_text