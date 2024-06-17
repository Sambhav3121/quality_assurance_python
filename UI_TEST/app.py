from flask import Flask, request, render_template
from solution import Solution

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/rotate', methods=['POST'])
def rotate():
    matrix_str = request.form.get('matrix')
    
    if not matrix_str.strip():
        return render_template('index.html', error="ValueError: Matrix input cannot be empty", matrix=matrix_str)

    try:
        matrix = [list(map(int, row.split(','))) for row in matrix_str.split(';')]
        Solution().rotate(matrix)
        return render_template('index.html', result=matrix, matrix=matrix_str)
    except ValueError as e:
        return render_template('index.html', error=f"ValueError: {str(e)}", matrix=matrix_str)
    except Exception as e:
        return render_template('index.html', error=f"Error: {str(e)}", matrix=matrix_str)

if __name__ == '__main__':
    app.run(debug=True)
