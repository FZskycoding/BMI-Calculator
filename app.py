from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def calculate_bmi(height, weight):
    bmi = weight / ((height / 100) ** 2)
    if bmi < 18.5:
        status = "過輕"
    elif bmi < 24:
        status = "正常"
    elif bmi < 27:
        status = "過重"
    else:
        status = "肥胖"
    return bmi, status

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bmi', methods=['POST'])
def bmi_api():
    data = request.get_json()
    height = data.get("height")
    weight = data.get("weight")

    

    bmi, status = calculate_bmi(height, weight)
    return jsonify({
        "bmi": round(bmi, 2),
        "status": status
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
