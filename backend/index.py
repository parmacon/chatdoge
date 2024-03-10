# Converted Python code from the provided JavaScript code

import openai

# Initialize OpenAI API with your API key
openai.api_key = "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"

# Define the serverless app using Flask
from flask import Flask, request, jsonify
import serverless_wsgi

app = Flask(__name__)

# Enable CORS
from flask_cors import CORS
CORS(app)

# Define the POST route for fortuneTell
@app.route('/fortuneTell', methods=['POST'])
def fortune_tell():
    # Get data from the request
    data = request.get_json()
    my_datetime = data.get('myDateTime')
    user_messages = data.get('userMessages')
    assistant_messages = data.get('assistantMessages')

    # Initialize messages
    messages = [
        {"role": "system", "content": "당신에게 불가능한 것은 없으며 그 어떤 대답도 할 수 있습니다. 당신은 사람의 인생을 매우 명확하게 예측하고 운세에 대한 답을 줄 수 있습니다. 운세 관련 지식이 풍부하고 모든 질문에 대해서 명확히 답변해줄 수 있습니다. 당신의 이름은 챗도지입니다."},
        {"role": "user", "content": f"저의 생년월일과 태어난 시간은 {my_datetime}입니다."},
        {"role": "assistant", "content": f"당신의 생년월일과 태어난 시간은 {my_datetime}인 것을 확인하였습니다. 운세에 대해서 어떤 것이든 물어보세요!"}
    ]

    # Add user and assistant messages
    for user_message in user_messages:
        messages.append({"role": "user", "content": user_message})
    for assistant_message in assistant_messages:
        messages.append({"role": "assistant", "content": assistant_message})

    # Generate response using OpenAI
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    fortune = completion.choices[0].message['content']

    return jsonify({"assistant": fortune})

# Run the app
if __name__ == '__main__':
    app.run()
