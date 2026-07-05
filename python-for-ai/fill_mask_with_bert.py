from transformers import pipeline

fill_mask = pipeline("fill-mask", model="bert-base-uncased")
result = fill_mask("Artificial intelligence is changing the [MASK] industry.")
for item in result:
    print(f"Sequence: {item['sequence']}, Token: {item['token_str']}, Score: {item['score']:.4f}")

# BERT is good for:

# classification
# search
# embeddings
# masked word prediction
# understanding text