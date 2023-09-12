from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return ("\
    <html>\
    テスト\
    </html>\
    ")

@app.route("/api/<param>")
def openaiapi(param):
    print(param)
    return (param+"hogrhoge")

if __name__=="main":
    app.run(port=8888, host="0.0.0.0", debug=True) 