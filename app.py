from flask import Flask, request, send_file
from rembg import remove
import io

app = Flask(__name__)

@app.route('/remove-background', methods=['POST'])
def remove_background():
    if 'file' not in request.files:
        return 'Dosya bulunamadı', 400

    file = request.files['file']
    input_image = file.read()
    output_image = remove(input_image)

    return send_file(io.BytesIO(output_image), mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
