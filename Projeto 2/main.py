import openai

openai.api_key = "secret key"

resultado = openai.Image.create(
    prompt="A cute yellow fish inside a fish bowl in mars", n=1, size="1024x1024"
)

print(resultado)
