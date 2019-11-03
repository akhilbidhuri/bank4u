from manage import db

class bank_branches(db.Model):

    ifsc = db.Column(db.String(), primary_key=True)
    bank_id = db.Column(db.Integer)
    branch = db.Column(db.String())
    address = db.Column(db.String())
    city = db.Column(db.String())
    district = db.Column(db.String())
    state = db.Column(db.String())
    bank_name = db.Column(db.String())

    def __init__(self, ifsc, bank_id, branch, address, city, district, state, bank_name):
        self.ifsc = ifsc
        self.branch = branch
        self.bank_id = bank_id
        self.address = address
        self.city = city
        self.district = district
        self.state = state
        self.bank_name = bank_name

    def __repr__(self):
        return '<id {}>'.format(self.bank_id)
    
    def serialize(self):
        return {
            'ifsc': self.ifsc, 
            'bank_id': self.bank_id,
            'branch': self.branch,
            'address':self.address,
            'city': self.city,
            'district' : self.district,
            'state' : self.state,
            'bank_name': self.bank_name
        }