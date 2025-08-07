from flask import Flask, request, jsonify
from src.core.analyzer import CodeAnalyzer
from src.core.embeddings import EmbeddingGenerator
from src.core.generator import DocumentationGenerator

app = Flask(__name__)

@app.route('/api/analyze', methods=['POST'])
def analyze_code():
    data = request.json
    code = data.get('code', '')
    analyzer = CodeAnalyzer()
    analysis_result = analyzer.analyze_code(code)
    return jsonify(analysis_result)

@app.route('/api/generate-docs', methods=['POST'])
def generate_docs():
    data = request.json
    embeddings = data.get('embeddings', [])
    generator = DocumentationGenerator()
    docs = generator.generate_docs(embeddings)
    return jsonify(docs)

if __name__ == '__main__':
    app.run(debug=True)