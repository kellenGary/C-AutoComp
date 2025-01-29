from openai import OpenAI

client = OpenAI(api_key="<DeepSeek API Key>", base_url="https://api.deepseek.com")
grammar = ("program -> expr SEMICOLON;"
           "expr -> expr ADD term | expr SUBTRACT term | term;"
           "term -> term MULT factor | term DIVIDE factor | factor;"
           "factor -> IDENTIFIER | LPAREN expr RPAREN")

def fixTokens(input_code, invalid_tokens=None):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user",
             "content": f"Fix the following incorrect tokens: {invalid_tokens}, within the code: {input_code} "
                        f"using the grammar: {grammar}"}
        ],
        stream=False
    )
    print(response.choices[0].message.content)
