from flask import Flask, Blueprint, render_template, request, url_for, redirect, send_file, send_from_directory
from src import api_request
from os import listdir
from os.path import isfile, join
import urllib.request
import os

bp = Flask(__name__)

if not os.path.exists('data_files'):
    os.makedirs('data_files')

@bp.context_processor
def inject_bg_color():
    return {"bg_color": os.environ.get("BG_COLOR", "#ffffff")}

@bp.route("/", methods = ['GET'])
def home():
    return render_template("pages/home.html")

@bp.route("/weather", methods = ['POST'])
def weather():
    name = request.form.get('weather')
    try:
        weather_data = api_request.main_def(name)
        '''
        if not weather_data.week:
            return render_template("pages/weather.html", country=weather_data.country, city=weather_data.city, weather=weather_data)
        '''
    except Exception as e:
        return render_template("pages/home.html", error="Failed to fetch weather data. Please try again.")

    return render_template("pages/weather.html", weather=weather_data)

@bp.route('/download')
def download():
    image_path = '/app/project_board/sky.jpg'
    try:
        urllib.request.urlretrieve('https://my-static-website-bucket-119.s3.eu-central-1.amazonaws.com/sky.jpg', image_path)

        return send_file(image_path, as_attachment=True)

    except Exception as e:
        return f"Failed to download image: {str(e)}", 500

@bp.route('/history')
def history():
    files = get_files()

    return render_template("pages/history.html", files=files)

def get_files():
    mypath = "data_files"
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return files

@bp.route('/download/<filename>')
def download_file(filename):
    return send_from_directory("data_files", filename, as_attachment=True)

if __name__ == '__main__':
    bp.run(host="0.0.0.0", port=8000, debug=True)
