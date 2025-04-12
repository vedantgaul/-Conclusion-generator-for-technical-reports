from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key="AIzaSyDcL-LJo9T68XiiTW1AQWzrmKLU1ifGVOc")
model = genai.GenerativeModel("gemini-1.5-flash")  # Updated model name

@app.route("/", methods=["GET", "POST"])
def index():
    conclusion = ""
    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        if user_input.strip():
            prompt = f"""Read the following technical documentation and generate a concise conclusion with these rules:
            1. Summarize key points in bullet points
            2. Keep it under 100 words
            3. Highlight any potential limitations
            4. Use technical but clear language
            
            Documentation:\n{user_input}"""
            try:
                response = model.generate_content(prompt)
                conclusion = response.text
            except Exception as e:
                conclusion = f"Error generating response: {str(e)}"
    return render_template("index.html", conclusion=conclusion)

if __name__ == "__main__":
    app.run(debug=True)