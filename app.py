from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    # Simple logic: Echo back or basic response
    if not user_message:
        return jsonify({"response": "Please say something!"})
    
    response_text = f"You said: {user_message}. I'm a simple agent hosted on Render!"
    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
