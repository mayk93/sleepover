from flask import Flask
from flask import request, render_template, redirect, url_for
import pafy

app = Flask(__name__, static_url_path='')

@app.route('/downloaded_video')
def downloading_video():
    print("Here!")
    return redirect('/static/test.mp4')

@app.route('/download_video', methods=['POST'])
def download_video():
    url = request.form['download_path']
    print(url)
    video = pafy.new(url)
    stream = video.allstreams[len(v.allstreams)-1]
    video_file = stream.download("static/test.mp4")
    print("Done.")
    return redirect(url_for('downloaded_video'))

@app.route('/')
def input():
    return render_template("input.html")

if __name__=="__main__":
    app.run(host="0.0.0.0")
