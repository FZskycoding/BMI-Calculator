import requests

def test_bmi_api_normal():
    url = "http://127.0.0.1:5000/bmi"
    data = {"height": 170, "weight": 65}
    response = requests.post(url, json=data)
    assert response.status_code == 200
    result = response.json()
    assert round(result["bmi"], 2) == 22.49
    assert result["status"] == "正常"

def test_bmi_api_underweight():
    url = "http://127.0.0.1:5000/bmi"
    data = {"height": 170, "weight": 45}
    response = requests.post(url, json=data)
    assert response.status_code == 200
    result = response.json()
    assert result["status"] == "過輕"

def test_bmi_api_overweight():
    url = "http://127.0.0.1:5000/bmi"
    data = {"height": 170, "weight": 80}
    response = requests.post(url, json=data)
    assert response.status_code == 200
    result = response.json()
    assert result["status"] == "肥胖"

def test_bmi_api_missing_data():
    url = "http://127.0.0.1:5000/bmi"
    data = {"height": 170}
    response = requests.post(url, json=data)
    assert response.status_code == 400
    result = response.json()
    assert result["error"] == "請提供身高與體重"
