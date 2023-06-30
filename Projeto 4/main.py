import openai

openai.api_key = "secret-key"

audio_file = open("audio/german1.mp3", "rb")
result = openai.Audio.translate("whisper-1", audio_file)

print(result)
