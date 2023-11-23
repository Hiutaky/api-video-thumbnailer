from flask import Flask, request, send_file
import subprocess

app = Flask(__name__)

@app.route('/screenshot', methods=['GET'])
def get_screenshot():
    video_source = request.args.get('video_source')
    seconds = request.args.get('seconds', default = 0, type = int)
    filePath = "results/image1.jpg";
    subprocess.call(['ffmpeg', '-y', '-i', video_source, '-ss', seconds_to_time_format(seconds), '-vframes', '1', '-f', 'image2', filePath])
    return send_file(f"./{filePath}", mimetype="image/jpg" )

def seconds_to_time_format(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d:%02d" % (hours, minutes, seconds)

if __name__ == '__main__':
    app.run(debug=True)

