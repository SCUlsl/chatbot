import openai
from flask import Flask, request, jsonify,render_template
from flask_cors import CORS,cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')
# 配置 OpenAI API 密钥
openai.api_key = "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"

# 配置模型引擎
model_engine = "gpt-3.5-turbo"


@app.route('/t2', methods=['POST'])
def t2():
    question = request.form.get('question', '')
    context = request.form.get('context', '')
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=(f"{context}用户: {question}\n机器人:"),
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    answer = response.choices[0].text.strip()
    if answer :
        return jsonify({'answer': answer})
    else:
        return jsonify({'answer':'nothing'})

@app.route('/t1', methods=['POST'])
def t1():
    question = request.form.get('question', '')
    context = request.form.get('context', '')
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=(f"{context}用户: {question}\n机器人:"),
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    answer = response.choices[0].text.strip()
    if answer :
        return jsonify({'answer': answer})
    else:
        return jsonify({'answer':'nothing'})

@app.route('/t3', methods=['POST'])
def t3():
    question = request.form.get('question', '')
    context = request.form.get('context', '')
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=(f"{context}用户: {question}\n机器人:"),
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    answer = response.choices[0].text.strip()
    if answer :
        return jsonify({'answer': answer})
    else:
        return jsonify({'answer':'nothing'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)