from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# API endpoint for interacting with GPT
@app.route('/gpt', methods=['POST'])
def interact_with_gpt():
    data = request.get_json()
    prompt = data['prompt']

    # Send prompt to GPT server and get response
    gpt_response = requests.post('kk.jmvision.top', json={'prompt': prompt})
    response_data = gpt_response.json()

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8310)
