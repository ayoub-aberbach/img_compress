import os
from pathlib import Path
from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify, send_from_directory
from utils import compress_image


app = Flask(__name__)
CORS(app, methods=["GET, POST", "OPTIONS"], allow_headers=["Content-Type", "Accept"])


@app.route("/compress", methods=["GET", "POST"])
@cross_origin(methods=["GET", "POST"])
def compress():
    """
    Compress an uploaded images.

    **Request Body:**
    - `img_file`: An uploaded image file in one of the supported formats (Stored locally).

    **Supported Formats:**
    - png, jpg, jpeg.

    **Responses:**
    - 200: Successful compression, returns the compressed image.
    - 403: Unsupported file type.
    - 404: File not found.
    - 406: Empty request body.
    - 500: Internal server error.
    """
    try:
        if request.content_length == 44:
            return jsonify({"failed": "Empty request."}), 406

        if "img_file" not in request.files:
            return jsonify({"failed": "File not found."}), 404

        file = request.files["img_file"]
        file.save(os.path.join("uploads", str(file.filename)))

        extensions: list = [".jpeg", ".png", ".jpg"]
        saved_path = os.path.join("uploads", str(file.filename))

        if os.path.splitext(saved_path)[1].lower() not in extensions:
            os.remove(os.path.join("uploads", str(file.filename)))
            return jsonify({"failed": "Unsupported Extension"}), 403

        compressed_img = compress_image(file.filename, "uploads", "compressed")
        os.remove(os.path.join("uploads", str(file.filename)))

        return jsonify({"success": True, "image_url": compressed_img}), 200
    except Exception as error:
        return jsonify({"server": str(error)}), 500


@app.route("/download/<filepath>")
@cross_origin(methods=["GET"])
def download(filepath: Path):
    """
    Download the selected compressed image based on given path.

    **Request Params:**
    - `filepath`: An existed image file path.

    **Responses:**
    - 200: Successful download, returns the compressed image path to download.
    - 403: The file have been deleted or a wrong path was given.
    """
    existed_path = os.path.join("compressed", filepath)

    if not os.path.exists(existed_path):
        return jsonify({"message": "Unable to find the given file."}), 403
    
    return send_from_directory("compressed", filepath), 200
    


@app.route("/delete/<cmp_image>", methods=["GET", "POST"])
@cross_origin(methods=["GET", "POST"])
def deleteCompressed(cmp_image: Path):
    """
    Deletes an image after based on an existed path

    **Request Params:**
    - `cmp_image`: An existed image file path.

    **Responses:**
    - 200: Successful file deletion, returns a message.
    - 403: The file have been deleted or a wrong path was given.
    """
    existed_path = os.path.join("compressed", cmp_image)

    if os.path.exists(existed_path):
        os.remove(existed_path)
        return jsonify({"message": "Deleted"}), 200

    return jsonify({"message": "Unable to find the given file."}), 403


if __name__ == "__main__":
    app.run(debug=True)
