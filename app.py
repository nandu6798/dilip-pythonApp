from flask import Flask, request, render_template_string

app = Flask(__name__)

form_html = """
<!doctype html>
<title>Hello</title>
<h2>Enter your name</h2>
<form method="POST">
  <input type="text" name="name" placeholder="Your name">
  <input type="submit" value="Say Hey">
</form>
{% if name %}
  <h3>Hey {{ name }}!</h3>
{% endif %}
"""

@app.route('/', methods=['GET', 'POST'])
def greet():
    name = None
    if request.method == 'POST':
        name = request.form.get('name')
        if name == "":
            name = None
    return render_template_string(form_html, name=name)

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

