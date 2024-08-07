from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def index():
    str_flask="Hello, Flask!"
    return  render_template("index.html", var_from_python=str_flask)


@app.route("/api/<param>")
def url_api(param):
    print(param)
    return ("param: "+param)

@app.route("/api", methods={"post"})
def post_api():
    param=request.form.get("inname_data")
    print(param)
    return ("param: "+param)

if __name__=="__main__":
    app.run() 
