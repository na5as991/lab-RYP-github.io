from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <title>My reports on github</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f5f5f5;
      margin: 0;
      padding: 0;
      text-align: center;
    }
    header {
      background-color: #333;
      color: #fff;
      padding: 20px;
    }
    .container {
      margin: 20px auto;
      width: 80%;
    }
    .columns {
      display: flex;
      justify-content: space-around;
      margin-top: 20px;
    }
    .column {
      background: #fff;
      padding: 20px;
      box-shadow: 0 0 8px rgba(0,0,0,0.1);
      border-radius: 8px;
      width: 40%;
    }
    .column h2 {
      margin-bottom: 20px;
      color: #333;
    }
    .btn {
      display: block;
      margin: 10px auto;
      width: 80%;
      padding: 10px;
      text-decoration: none;
      color: #fff;
      background: #007BFF;
      border-radius: 5px;
      transition: background 0.3s;
    }
    .btn:hover {
      background: #0056b3;
    }
  </style>
</head>
<body>
  <header>
    <h1>My reports on github</h1>
  </header>
  <div class="container">
    <div class="columns">
      <!-- Первый столбец: код для лабораторных работ -->
      <div class="column">
        <h2>код к лабораторным работам</h2>
        <a href="https://github.com/yourusername/lab1" class="btn">lab 1</a>
        <a href="https://github.com/yourusername/lab2" class="btn">lab 2</a>
        <a href="https://github.com/yourusername/lab3" class="btn">lab 3</a>
        <a href="https://github.com/yourusername/lab4" class="btn">lab 4</a>
      </div>
      <!-- Второй столбец: письменный отчёт -->
      <div class="column">
        <h2>письменный отчёт</h2>
        <a href="https://github.com/yourusername/report1" class="btn">письменный отчёт для лабораторной работы 1</a>
        <a href="https://github.com/yourusername/report2" class="btn">письменный отчёт для лабораторной работы 2</a>
        <a href="https://github.com/yourusername/report3" class="btn">письменный отчёт для лабораторной работы 3</a>
        <a href="https://github.com/yourusername/report4" class="btn">письменный отчёт для лабораторной работы 4</a>
      </div>
    </div>
  </div>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
