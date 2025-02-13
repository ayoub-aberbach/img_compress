# Image Compression API

A Flask-based API that provides image compression, download, and deletion functionalities. This API allows users to upload an image, compress it, and retrieve or delete the compressed file.

## Features
- Compress images in `JPEG`, `PNG`, and `JPG` formats.
- Download compressed images.
- Delete compressed images.
- Handles various errors like unsupported formats, missing files, and server issues.
- CORS-enabled for cross-origin requests.

## Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Run the API Server
```sh
python app.py
```

### API Endpoints

#### 1. Compress an Image
**Endpoint:** `POST /compress`

- **Request Body:**
  - `img_file`: Image file to be compressed.

- **Responses:**
  - `200`: Returns a JSON object with the compressed image URL.
  - `403`: Unsupported file type.
  - `404`: File not found.
  - `406`: Empty request body.
  - `500`: Internal server error.

#### 2. Download a Compressed Image
**Endpoint:** `GET /download/<filepath>`

- **Request Params:**
  - `filepath`: Name of the compressed image file.

- **Responses:**
  - `200`: Returns the compressed image file.
  - `403`: File not found.

#### 3. Delete a Compressed Image
**Endpoint:** `POST /delete/<cmp_image>`

- **Request Params:**
  - `cmp_image`: Name of the compressed image file.

- **Responses:**
  - `200`: File deleted successfully.
  - `403`: File not found.

## Project Structure
```
project-folder/
│── app.py                 # Main Flask application
│── utils.py               # Helper functions (image compression)
│── requirements.txt       # Python dependencies
│── uploads/               # Directory for uploaded images
│── compressed/            # Directory for compressed images
```

## Dependencies
- Flask
- Flask-CORS
- pathlib
- os

## License
This project is open-source and available under the MIT License.

## Contributing
Pull requests are welcome! Feel free to open an issue or suggest improvements.

