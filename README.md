Rotate Image with E2E/UI Tests
This project implements a web-based tool using Flask for rotating an 
𝑛
×
𝑛
n×n matrix 90 degrees clockwise. It includes Selenium-based end-to-end tests to validate the web interface.

Solution Requirements
Flask
Selenium
Chrome WebDriver (for Selenium)
Project Structure
app.py: Flask application that implements the web interface.
solution.py: Contains the algorithm for rotating the image (matrix).
templates/index.html: HTML template for the web interface.
test_e2e.py: Selenium-based end-to-end tests to verify the web application.
Tests
test_e2e.py contains multiple test cases:

test_rotate_image: Validates the rotation of the matrix.
test_all_same_values: Checks the rotation with all same values in the matrix.
test_invalid_input: Checks error handling for invalid input.
test_leading_trailing_spaces: Checks the input handling with leading and trailing spaces.
test_negative_values: Checks the rotation with negative values in the matrix.
test_non_integer_input: Checks the error handling for non-integer inputs.
test_large_values: Validates the rotation with the maximum allowable values.
test_large_input_size: Checks the performance and correctness with the maximum size matrix.
test_incorrect_delimiters: Validates error handling for incorrect delimiters.
test_mixed_positive_negative_values: Validates error handling for mixed positive and negative values.
test_non_numeric_characters: Validates error handling for non-numeric characters.
test_whitespace_only_input: Checks error handling for whitespace only input.
test_values_exceeding_max_limit: Validates error handling for values exceeding the maximum limit.
Constraints
n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000

Usage
Run the Flask Application:

bash
Copy code
python app.py
Access the Application:

Open your web browser and go to http://127.0.0.1:5000/ to use the application.

Run Selenium Tests:

Ensure the Flask application (app.py) is running, then run the Selenium end-to-end tests:

bash
Copy code
python test_e2e.py
