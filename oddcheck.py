# Import Flask
from flask import Flask, render_template, request

# Create an app object
app = Flask(__name__)

# Define the home route
@app.route("/")
def home():
    # Render the home.html file
    return render_template("home.html")

# Define the check route
@app.route("/check", methods=["POST"])
def check():
    # Get the number from the form
    number = int(request.form["number"])
    # Check if the number is odd or even
    if number % 2 == 0:
        result = "even"
    else:
        result = "odd"
    # Render the result.html file with the result and number
    return render_template("result.html", number=number, result=result)

# Ensure the app is run only when executed directly
if __name__ == "__main__":
    # Run the app on 0.0.0.0 (all available interfaces) on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
