"""
Author- Suraj Prakash Patil
Date- 11/06/2024

"""


from flask import Blueprint, request, jsonify, abort
from . import db
from .models import Data
from .auth import basic_auth_required

main = Blueprint('main', __name__)

@main.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(main.root_path, 'static'), 'favicon.ico')



@main.route('/data', methods=['POST'])
@basic_auth_required
def create_data():
    data = request.get_json()
    if not data:
        abort(400, description="Invalid JSON")
    new_data = Data(content=data)
    db.session.add(new_data)
    db.session.commit()
    return jsonify({'id': new_data.id}), 201

@main.route('/data/<int:id>', methods=['GET'])
@basic_auth_required
def get_data(id):
    data = Data.query.get_or_404(id)
    return jsonify(data.content), 200

@main.route('/data/<int:id>', methods=['PUT'])
@basic_auth_required
def update_data(id):
    data = Data.query.get_or_404(id)
    new_content = request.get_json()
    if not new_content:
        abort(400, description="Invalid JSON")
    data.content = new_content
    db.session.commit()
    return jsonify({'message': 'Data updated'}), 200

@main.route('/data/<int:id>', methods=['DELETE'])
@basic_auth_required
def delete_data(id):
    data = Data.query.get_or_404(id)
    db.session.delete(data)
    db.session.commit()
    return jsonify({'message': 'Data deleted'}), 200



'''
from flask import Blueprint, request, jsonify, abort
from . import db
from .models.py import Data

main = Blueprint('main', __name__)

@main.route('/data', methods=['POST'])
def create_data():
    data = request.get_json()
    if not data:
        abort(400, description="Invalid JSON")
    new_data = Data(content=data)
    db.session.add(new_data)
    db.session.commit()
    return jsonify({'id': new_data.id}), 201

@main.route('/data/<int:id>', methods=['GET'])
def get_data(id):
    data = Data.query.get_or_404(id)
    return jsonify(data.content), 200

@main.route('/data/<int:id>', methods=['PUT'])
def update_data(id):
    data = Data.query.get_or_404(id)
    new_content = request.get_json()
    if not new_content:
        abort(400, description="Invalid JSON")
    data.content = new_content
    db.session.commit()
    return jsonify({'message': 'Data updated'}), 200

@main.route('/data/<int:id>', methods=['DELETE'])
def delete_data(id):
    data = Data.query.get_or_404(id)
    db.session.delete(data)
    db.session.commit()
    return jsonify({'message': 'Data deleted'}), 200



###################################################
from .auth import basic_auth_required

# Add the decorator to each route
@main.route('/data', methods=['POST'])
@basic_auth_required
def create_data():
    # Function body remains the same

@main.route('/data/<int:id>', methods=['GET'])
@basic_auth_required
def get_data(id):
    # Function body remains the same

@main.route('/data/<int:id>', methods=['PUT'])
@basic_auth_required
def update_data(id):
    # Function body remains the same

@main.route('/data/<int:id>', methods=['DELETE'])
@basic_auth_required
def delete_data(id):
    # Function body remains the same
'''