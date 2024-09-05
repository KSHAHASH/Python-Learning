from transformers import pipeline

# Create the pipeline object for automatic speech recognition
asr_pipeline = pipeline(task="automatic-speech-recognition")

# Use the pipeline to process the audio file
result = asr_pipeline("https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/mlk.flac")

# Print the result
print(result)


