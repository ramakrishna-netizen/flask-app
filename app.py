from flask import Flask  ,render_template,request
from flask import url_for


app = Flask(__name__)

app.template_folder = "./public"
app.static_folder ="./public/css"

@app.route('/',methods=["GET", "POST"])
def home():
	if request.method == "POST":
		print(request.form['uname'])
		print(request.form['email'])
		print(request.form['password'])
	return render_template('index.html')


app.run(debug=True, port="5000",host="0.0.0.0")
