from flask import jsonify, request
from app import app  # Update "your_app" to the name of your Flask app directory
import openai

# Replace this with your actual GPT-3 API key
api_key = "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"

# Initialize the GPT-3 model
openai.api_key = api_key

@app.route('/', methods=['GET'])
def index():
    return "Welcome to the Code Converter!"

# @app.route('/convert-code')
# def convert_code():
#     code = request.args.get('code')
#     source_language = request.args.get('source_language')
#     target_language = request.args.get('target_language')

#     try:
#         # Use the OpenAI API to translate code
#         response = openai.Completion.create(
#             engine="text-davinci-002",
#             prompt=f"Translate the following code from {source_language} to {target_language}:\n\n{code}",
#             max_tokens=100
#         )
#         translated_code = response.choices[0].text
        

#         return jsonify({'translated_code': translated_code})
#     except Exception as e:
#         return jsonify({'error': str(e)})


@app.route('/convert-code')
def convert_code():
    code = request.args.get('code')
    source_language = request.args.get('source_language')
    target_language = request.args.get('target_language')

    try:
        # Use the OpenAI API to translate code
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Translate the following code from {source_language} to {target_language}:\n\n{code}",
            max_tokens=500
        )
        translated_code = response.choices[0].text

        return translated_code, 200  # Return the translated code as plain text
    except Exception as e:
        return str(e), 500  # Return an error message as plain text
