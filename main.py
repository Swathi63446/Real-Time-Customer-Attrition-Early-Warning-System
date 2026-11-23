import google.generativeai as genai
genai.configure(api_key="GEMINI_API_KEY")

available_models = genai.list_models()
print([model.name for model in available_models])
