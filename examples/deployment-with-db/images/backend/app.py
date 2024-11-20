from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Database configuration from environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model definition
class KeyValue(db.Model):
    __tablename__ = 'key_value_pairs'
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(255), unique=True, nullable=False)
    value = db.Column(db.String(255), nullable=False)

# Create the table
with app.app_context():
    db.create_all()

# API endpoints
@app.route('/create', methods=['POST'])
def create():
    data = request.json
    if not data or 'key' not in data or 'value' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_pair = KeyValue(key=data['key'], value=data['value'])
    try:
        db.session.add(new_pair)
        db.session.commit()
        return jsonify({'message': 'Key-value pair created'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/read/<string:key>', methods=['GET'])
def read(key):
    pair = KeyValue.query.filter_by(key=key).first()
    if pair:
        return jsonify({'key': pair.key, 'value': pair.value}), 200
    return jsonify({'error': 'Key not found'}), 404

@app.route('/update', methods=['PUT'])
def update():
    data = request.json
    if not data or 'key' not in data or 'value' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    pair = KeyValue.query.filter_by(key=data['key']).first()
    if pair:
        pair.value = data['value']
        db.session.commit()
        return jsonify({'message': 'Key-value pair updated'}), 200
    return jsonify({'error': 'Key not found'}), 404

@app.route('/delete/<string:key>', methods=['DELETE'])
def delete(key):
    pair = KeyValue.query.filter_by(key=key).first()
    if pair:
        db.session.delete(pair)
        db.session.commit()
        return jsonify({'message': 'Key-value pair deleted'}), 200
    return jsonify({'error': 'Key not found'}), 404

# Run the server
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")
