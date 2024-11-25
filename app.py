from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML template for the temperature converter
temperature_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Temperature Converter</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Temperature Converter</h1>
        <form method="POST" class="mt-4">
            <div class="form-group">
                <label for="celsius">Temperature (°C):</label>
                <input type="number" class="form-control" name="celsius" id="celsius" step="any" value="{{ celsius or '' }}" required>
            </div>
            <button type="submit" class="btn btn-primary">Convert to Fahrenheit</button>
        </form>

        {% if fahrenheit is not none %}
            <div class="mt-4">
                <h2>Temperature in Fahrenheit: {{ fahrenheit }}°F</h2>
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def temperature_converter():
    fahrenheit = None
    celsius = None
    if request.method == "POST":
        try:
            # Retrieve input value
            celsius = float(request.form["celsius"])

            # Convert Celsius to Fahrenheit
            fahrenheit = round((celsius * 9/5) + 32, 2)
        except ValueError:
            fahrenheit = "Invalid input. Please enter a valid number."

    # Pass celsius back to the template
    return render_template_string(temperature_template, fahrenheit=fahrenheit, celsius=celsius)

if __name__ == "__main__":
    app.run(debug=True)