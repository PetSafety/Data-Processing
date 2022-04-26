from flask import Blueprint, jsonify, request
from sqlalchemy import exc

from database_singleton import Singleton
from project.api.utils.creation_utils import Utils
from project.api.models import DadosEmbarcado

data_processing_blueprint = Blueprint("data_processing_blueprint", __name__)
db = Singleton().database_connection()
utils = Utils()


@data_processing_blueprint.route("/ping", methods=["GET"])
def pong():
    return jsonify({"message": "works!"}), 200

@data_processing_blueprint.route("/process_data", methods=["POST"])
def process_data():
    request_data = request.get_json()

    error_response = {"status": "fail", "message": "Invalid payload."}

    dados_processamento = DadosEmbarcado(
        request_data['temperatura'],
        request_data['ruido'],
        request_data['video'],
        request_data['idCaixa']
        )
    response = {"status": "success", "data": {"request": request_data}}

    try:
        db.session.add(dados_processamento)
        db.session.commit()

        response = {"status": "success", "data": {"request": dados_processamento.to_json()}}

        return jsonify(response), 201
    except exc.IntegrityError as e:
        db.session.rollback()
        return jsonify(error_response), 400

@data_processing_blueprint.route("/get_processed_data", methods=["GET"])
def get_processed_data():

    try:
        response = {
            "status": "success",
            "data": {
                "processed_datas": [data.to_json() for data in DadosEmbarcado.query.all()]
            },
        }
        return response, 200
    except Exception as err:
        return jsonify(err), 404
