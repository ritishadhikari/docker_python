from flask import Flask, escape, request

app=Flask(__name__)

@app.route('/')
def hello():
    name=request.args.get("name","world")
    return f"Hello,{escape(name)}"

# if __name__=="__main__":
#     app.run(port=5000,debug=False,host="0.0.0.0")
