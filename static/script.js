function calculateBMI() {
  const height = document.getElementById("height").value;
  const weight = document.getElementById("weight").value;

  // 檢查是否有負數或 0
  if (height <= 0 || weight <= 0) {
    alert("身高與體重必須為正數且大於 0");
    document.getElementById("result").innerHTML = `BMI：錯誤<br>狀態：錯誤`;
    return;
  }    

  fetch("/bmi", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      height: parseFloat(height),
      weight: parseFloat(weight),
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.bmi) {
        document.getElementById("result").innerHTML = `BMI：${data.bmi.toFixed(2)}<br>狀態：${data.status}`;
      } else if (data.error) {
        document.getElementById("result").innerHTML = data.error;
      }
    })
    .catch((err) => {
      document.getElementById("result").innerHTML = "發生錯誤，請稍後再試。";
    });
}
