from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


# Load the model and tokenizer
model_name = "SalesForce/codet5-base"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def fixTokens(input_code, invalid_tokens=None):
    # Optionally process the invalid tokens (e.g., replace or highlight them)
    if invalid_tokens:
        # If invalid tokens are provided, we can highlight them in the input
        for token in invalid_tokens:
            input_code = input_code.replace(token, f"[INVALID]{token}[INVALID]")

    # Tokenize the input code
    inputs = tokenizer(input_code, return_tensors='pt')

    # Generate the output code using the model
    outputs = model.generate(**inputs, max_length=512, num_beams=5, early_stopping=True)

    # Decode the generated output
    generated_code = tokenizer.decode(outputs[0], skip_special_tokens=True)

    print("Corrected Code:", generated_code)

