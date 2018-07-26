from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return """
    <img src="/static/ME_Logo.png" alt="maclean logo" style="width:300px;height:35px;"></img>

    <h2>Remote Dashboard</h2>

    <iframe src="http://192.168.0.102:8888/stream?topic=/jetson_cam/image_raw" width="640" height="360" frameborder="0" allowfullscreen></iframe>
    """

if __name__=='__main__':
    app.run(debug=True, use_reloader=True)
