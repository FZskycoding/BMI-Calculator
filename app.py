from flask import Flask, request, jsonify

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

@app.route('/bmi', methods=['POST'])
def bmi_api():
    data = request.get_json()
    height = data.get("height")
    weight = data.get("weight")

    if height is None or weight is None:
        return jsonify({"error": "請提供身高與體重"}), 400

    bmi, status = calculate_bmi(height, weight)
    return jsonify({
        "bmi": round(bmi, 2),
        "status": status
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
