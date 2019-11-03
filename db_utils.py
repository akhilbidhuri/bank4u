from app import db
from models import bank_branches
from sqlalchemy import *
from flask import jsonify

def getDet(ifsc):
    branch = bank_branches.query.filter_by(ifsc=ifsc).first()
    if branch!=None:
          branch = branch.serialize()
          return jsonify({'msg':'Success', 'data': branch}), 200
    
    return jsonify({'msg':"Invalid IFSC!!! Try again."}), 400

def getBranch(bank_name, city, offset, limit):
    offset = offset - 1
    branches = bank_branches.query.filter(bank_branches.bank_name==bank_name, bank_branches.city==city).offset(limit*offset).limit(limit)
    branches = branches.all()
    if len(branches) != 0:
        branches = [b.serialize() for b in branches]
        return jsonify({'msg':'Success', 'data': branches}), 200
    
    return jsonify({'msg':"Nothing Could be Found, may be Invalid input!!! Try again."}), 400

if __name__ == '__main__':
    branches = bank_branches.query.filter(bank_branches.bank_name=="HDFC BANK", bank_branches.city=="DELHI").offset(10).limit(10)
    branches = branches.all()
    for i in branches:
        print(i.ifsc, i.branch, i.city)
    