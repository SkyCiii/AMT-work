from flask import Flask, request, jsonify, render_template

from app import app, db
from models import Record

@app.route("/")
def index():
    return render_template('table.html', title='AMT Table')

@app.route("/record", methods=['POST'])
def add_record():
    req_data = request.form
    asset_num = req_data['asset_num']
    tmc_num = req_data['tmc_num']
    pallet_id = req_data['pallet_id']
    name = req_data['name']
    eng_name = req_data['eng_name']
    vendor = req_data['vendor']
    sn = req_data['sn']
    model_num = req_data['model_num']
    size = req_data['size']
    limitations = req_data['limitations']
    location = req_data['location']
    work_station = req_data['work_station']
    
    record = Record(
        asset_num = asset_num,
        tmc_num = tmc_num,
        pallet_id = pallet_id,
        name = name,
        eng_name = eng_name,
        vendor = vendor,
        sn = sn,
        model_num = model_num,
        size = size,
        limitations = limitations,
        location = location,
        work_station = work_station
    )
    db.session.add(record)
    db.session.commit()
    return 'Create Succeeded', 200

@app.route("/record", methods=['GET'])
def get_records():
    records = Record.query.all()
    records_data = [
        {
            'id': record.id,
            'asset_num': record.asset_num,
            'tmc_num': record.tmc_num,
            'pallet_id': record.pallet_id,
            'name': record.name,
            'eng_name': record.eng_name,
            'vendor': record.vendor,
            'sn': record.sn,
            'model_num': record.model_num,
            'size': record.size,
            'limitations': record.limitations,
            'location': record.location,
            'work_station': record.work_station,
        }
        for record in records
    ]
    return jsonify(records_data), 200


@app.route('/record/<int:record_id>', methods=['GET'])
def get_record(record_id):
    record = Record.query.filter_by(id=record_id).first()
    record_data = {
        'id': record.id,
        'asset_num' : record.asset_num,
        'tmc_num' : record.tmc_num,
        'pallet_id' : record.pallet_id,
        'name' : record.name,
        'eng_name' : record.eng_name,
        'vendor': record.vendor,
        'sn': record.sn,
        'model_num': record.model_num,
        'size': record.size,
        'limitations': record.limitations,
        'location': record.location,
        'work_station': record.work_station,
    }
    return jsonify(record_data), 200


@app.route('/record/<int:record_id>', methods=['PUT'])
def update_record(record_id):
    req_data = request.form
    record = Record.query.filter_by(id=record_id).first()

    record.asset_num = req_data['asset_num']
    record.tmc_num = req_data['tmc_num']
    record.pallet_id = req_data['pallet_id']
    record.name = req_data['name']
    record.eng_name = req_data['eng_name']
    record.vendor = req_data['vendor']
    record.sn = req_data['sn']
    record.model_num = req_data['model_num']
    record.size = req_data['size']
    record.limitations = req_data['limitations']
    record.location = req_data['location']
    record.work_station = req_data['work_station']

    db.session.add(record)
    db.session.commit()
    return 'Update Succeeded', 200


@app.route("/record/<int:record_id>", methods=["DELETE"])
def delete_record(record_id):
    record = Record.query.filter_by(id=record_id).first()
    db.session.delete(record)
    db.session.commit()
    return 'Delete Succeeded', 200