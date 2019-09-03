#!/usr/bin/python
# coding=UTF-8
'''
@Author: recar
@Date: 2019-09-03 18:00:12
@LastEditTime: 2019-09-03 19:19:07
'''
# 对域名的curd

from flask import request, jsonify, current_app
from app.models import Domain
from . import domain_blueprint
from app.utils.response_util import success_response, faild_response, error_response
from sqlalchemy import or_, desc
import json

@domain_blueprint.route("/domain/", methods=['GET'])
def get_domain(page_index=1):
    try:
        per_page = current_app.config['ARTISAN_POSTS_PER_PAGE']
        pagination = Domain.query.order_by(desc(Domain.id)).paginate(page_index, per_page=per_page, error_out=False)
        datas = pagination.items
        domain_all_count = Domain.query.count()
        return_data = {
            "data": datas,
            "domain_all_count": domain_all_count,
            "page_index": page_index,
            "per_page": per_page
        }
        response = success_response(return_data)
        return response
    except Exception as e:
        response = error_response(str(e))
        return response

@domain_blueprint.route("/domain/", methods=['POST'])
def add_domain():
    data = json.loads(request.get_data())
    domain = data.get("domain", "")
    name = data.get("name", "")
    if domain and name:
        try: 
            domain = Domain(
                domain =domain,
                name =name,
            )
            db.session.add(domain)
            db.session.commit()
        except Exception as e:
            response = error_response(str(e))
    else:
        response = faild_response(20004)

