# Vector Search Project

This project provides a vector search system where you can upload files (PDF, DOCX, PPTX), embed them using `BertModel` and `BertTokenizer` from the `transformers` library, index them with FAISS, and store their metadata and embeddings in a MongoDB database. The project supports searching through uploaded documents by embedding a query and finding the closest matching files.

## Table of Contents
1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [MongoDB Setup](#mongodb-setup)
5. [Usage](#usage)
6. [Sample Data](#sample-data)
7. [Contributing](#contributing)
8. [License](#license)

---

## Features
- 📁 Upload multiple file types: PDF, DOCX, PPTX
- 🤖 File embedding using `BertModel` (bert-large-uncased)
- 🔍 Efficient search with FAISS (Facebook AI Similarity Search)
- 💾 Metadata and embeddings stored in MongoDB
- 📝 Sample dataset provided for testing

---

## Requirements

The following dependencies should be installed:

- Common dependencies (likely pre-installed):
  - `subprocess`
  - `os`
  - `glob`
  - `mimetypes`
  - `datetime`
  
- Installable dependencies:
  - `PyPDF2`
  - `docx`
  - `pptx`
  - `transformers`
  - `torch`
  - `numpy`
  - `re`
  - `pymongo`
  - `faiss`

---

## Installation

To get started, clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/your-username/vector-search.git
cd vector-search
```

Install the Python dependencies using pip:

```bash
pip install PyPDF2 python-docx python-pptx transformers torch numpy pymongo faiss-cpu
```

> **Note:** Ensure `faiss` is installed correctly based on your CPU or GPU environment. For GPU support, use `faiss-gpu`.

---

## MongoDB Setup

This project uses MongoDB to store the file embeddings and metadata. Follow these steps to set up MongoDB locally:

1. Download and install the [MongoDB Community Server](https://www.mongodb.com/try/download/community).
2. Follow the installation wizard to complete the setup.
3. Download [MongoDB Compass](https://www.mongodb.com/try/download/compass) for an easy-to-use GUI.
4. Open MongoDB Compass and connect to the default local server using this connection string:
   ```
   mongodb://localhost:27017/
   ```
5. Create a new database and collection to store the embeddings and metadata.

---

## Usage

The project provides a command-line interface where users can either upload files or search the indexed documents.

### Upload Files

To upload a group of files (PDF, DOCX, PPTX), run the following command:

```bash
python main.py
```

Choose the `upload` option, and provide the path to the folder containing the files. The system will extract the text, embed it using `BertModel`, and store the embeddings and metadata in MongoDB.

### Search Files

To search through the uploaded files, run the same command:

```bash
python main.py
```

Choose the `search` option, and enter a query. The system will embed the query and find the closest matching documents using FAISS.

---

## Sample Data

This repository includes a `Samples` folder containing test files (PDF, DOCX, PPTX) to help you get started. You can upload these files as a demo or use your own set of files.

---

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

For major changes, please open an issue first to discuss what you would like to change.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
