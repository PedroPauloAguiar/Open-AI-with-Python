import openai

# Preencher com sua secret key gerada no site da Open AI
openai.api_key = "secret key"

resultado = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "What is the distance between eath and mars?"}
    ],
)
print(resultado)
