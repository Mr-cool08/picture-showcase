from flask import Flask, render_template
import os

app = Flask(__name__)
def create_lists_images():
  images_folder_path = "static/photos"
  image_filenames = []
  for filename in os.listdir(images_folder_path):
    if os.path.isfile(os.path.join(images_folder_path, filename)):
      image_filenames.append(filename)
  return image_filenames
@app.route('/')
def index():
    return render_template('index.html', photos=image_filenames)
  
  
@app.route('/slideshow')
def slideshow():
    return render_template('slideshow.html', photos=image_filenames)
  

if __name__ == '__main__':
    image_filenames = create_lists_images()
    app.run(debug=True, host="0.0.0.0", port=8080)