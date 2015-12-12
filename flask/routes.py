from flask import request, render_template, redirect, url_for, send_from_directory
from flask import Flask
import pafy

app = Flask(__name__, static_url_path='')

@app.route('/download_vid', methods=['POST'])
def download_vid():
    print("I got it!")
    url = request.form['download_path']
    print(url)
    print "1"
    v = pafy.new(url)
    print "2"
    s = v.allstreams[len(v.allstreams)-1]
    print "3"
    filename = s.download("static/test.mp4")  # starts download
    print "4"
    return redirect(url_for('done'))

@app.route('/done')
def done():
    print "X"
    # return app.send_static_file('test.mp4')
    return redirect('/static/test.mp4')

@app.route('/')
def download():
    if request.method == 'GET':
        return render_template('basic.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0")
