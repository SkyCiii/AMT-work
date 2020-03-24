from app import db

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    asset_num = db.Column(db.String(120), nullable=True)
    tmc_num = db.Column(db.String(120), nullable=True)
    pallet_id = db.Column(db.String(120), nullable=True)
    name = db.Column(db.String(120), nullable=True)
    eng_name = db.Column(db.String(120), nullable=True)
    vendor = db.Column(db.String(120), nullable=True)
    sn = db.Column(db.String(120), nullable=True)
    model_num = db.Column(db.String(120), nullable=True)
    size = db.Column(db.String(120), nullable=True)
    limitations = db.Column(db.String(120), nullable=True)
    location = db.Column(db.String(120), nullable=True)
    work_station = db.Column(db.String(120), nullable=True)
