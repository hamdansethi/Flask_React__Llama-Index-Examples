import os
from multiprocessing.managers import BaseManager
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

# initialize manager connection
# NOTE: you might want to handle the password in a less hardcoded way
manager = BaseManager(('', 5602), b'password')
manager.register('query_index')
manager.register('insert_into_index')
manager.register('get_documents_list')
manager.connect()


@app.route("/query", methods=["GET"])
def query_index():
    global manager
    query_text = request.args.get("text", None)
    if query_text is None:
        return "No text found, please include a ?text=blah parameter in the URL", 400

    response = manager.query_index(query_text)._getvalue()

    response_json = {
        "text": str(response),
        "sources": []
    }

    for x in response.source_nodes:
        node = x.node  # This accesses the actual node
        metadata = node.metadata or {}

        response_json["sources"].append({
            "text": node.text,
            "similarity": round(x.score, 2),
            "doc_id": node.node_id,
            "start": metadata.get("start", None),
            "end": metadata.get("end", None),
        })

    return make_response(jsonify(response_json)), 200


@app.route("/uploadFile", methods=["POST"])
def upload_file():
    global manager
    if 'file' not in request.files:
        return "Please send a POST request with a file", 400

    filepath = None
    try:
        uploaded_file = request.files["file"]
        filename = secure_filename(uploaded_file.filename)

        # ✅ Ensure the documents folder exists
        os.makedirs('documents', exist_ok=True)

        filepath = os.path.join('documents', os.path.basename(filename))
        uploaded_file.save(filepath)

        # ✅ Debug log
        print(f"[INFO] Saved file to {filepath}")

        # ✅ Call into the manager
        if request.form.get("filename_as_doc_id", None) is not None:
            manager.insert_into_index(filepath, doc_id=filename)
        else:
            manager.insert_into_index(filepath)

        print("[INFO] File inserted into index successfully.")

    except Exception as e:
        # ✅ Print full stack trace for debugging
        import traceback
        traceback.print_exc()

        # Cleanup temp file
        if filepath is not None and os.path.exists(filepath):
            os.remove(filepath)

        return f"Error: {e}", 500

    # Cleanup temp file after insertion
    if filepath is not None and os.path.exists(filepath):
        os.remove(filepath)

    return "File inserted!", 200



@app.route("/getDocuments", methods=["GET"])
def get_documents():
    document_list = manager.get_documents_list()._getvalue()

    return make_response(jsonify(document_list)), 200
    

@app.route("/")
def home():
    return "Hello, World! Welcome to the llama_index docker image!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5601)
