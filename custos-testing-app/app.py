from flask import Flask, request, make_response
from config import users, admin_user_name, admin_password, child_gr_parent_gr_mapping, entity_types, groups, permissions, resources, user_group_mapping
from utils.custos_endpoints import Custos
import http

app = Flask(__name__)
c = Custos(admin_user_name, admin_password)


@app.route('/', methods=['GET', 'POST'])
def landing_page():
    return 'Skeleton REST application to perform load-testing of c Architecture.'


@app.route('/verify_user', methods=['GET', 'POST'])
def verify_user():
    response = make_response()
    try:
        response.data = c.verify_user(admin_user_name, admin_password)
        response.status_code = http.HTTPStatus.OK
    except Exception as e:
        response.status_code = http.HTTPStatus.BAD_REQUEST
        response.data = f'Request:{request.data}.\nSomething went wrong in verify_user(): {e}'
    finally:
	    return response


@app.route('/register_users', methods=['GET', 'POST'])
def register_users():
    response = make_response()
    try:
        response.data = c.register_users(users)
        response.status_code = http.HTTPStatus.OK
    except Exception as e:
        response.status_code = http.HTTPStatus.BAD_REQUEST
        response.data = f'Request:{request.data}.\nSomething went wrong in register_users(): {e}'
    finally:
    	return response



@app.route('/create_groups', methods=['GET', 'POST'])
def create_groups():
    response = make_response()
    try:
        response.data = c.create_groups(groups)
        response.status_code = http.HTTPStatus.OK
    except Exception as e:
        response.status_code = http.HTTPStatus.BAD_REQUEST
        response.data = f'Request:{request.data}.\nSomething went wrong in create_groups(): {e}'
    finally:
    	return response


@app.route('/allocate_users_to_groups', methods=['GET', 'POST'])
def allocate_users_to_groups():
    response = make_response()
    try:
        response.data = c.allocate_users_to_groups(user_group_mapping)
        response.status_code = http.HTTPStatus.OK
    except Exception as e:
        response.status_code = http.HTTPStatus.BAD_REQUEST
        response.data = f'Request:{request.data}.\nSomething went wrong in allocate_users_to_groups(): {e}'
    finally:
    	return response


@app.route('/allocate_child_group_to_parent_group', methods=['GET', 'POST'])
def allocate_child_group_to_parent_group():
    response = make_response()
    try:
        response.data = c.allocate_child_group_to_parent_group(child_gr_parent_gr_mapping)
        response.status_code = http.HTTPStatus.OK
    except Exception as e:
        response.status_code = http.HTTPStatus.BAD_REQUEST
        response.data = f'Request:{request.data}.\nSomething went wrong in allocate_child_group_to_parent_group(): {e}'
    finally:
        return response


@app.route('/create_permissions', methods=['GET', 'POST'])
def create_permissions():
    response = make_response()
    try:
        response.data = c.create_permissions(permissions)
        response.status_code = http.HTTPStatus.OK
    except Exception as e:
        response.status_code = http.HTTPStatus.BAD_REQUEST
        response.data = f'Request:{request.data}.\nSomething went wrong in create_permissions(): {e}'
    finally:
	    return response


@app.route('/create_entity_types', methods=['GET', 'POST'])
def create_entity_types():
    response = make_response()
    try:
        response.data = c.create_entity_types(entity_types)
        response.status_code = http.HTTPStatus.OK
    except Exception as e:
        response.status_code = http.HTTPStatus.BAD_REQUEST
        response.data = f'Request:{request.data}.\nSomething went wrong in create_entity_types(): {e}'
    finally:
	    return response


@app.route('/register_resources', methods=['GET', 'POST'])
def register_resources():
    response = make_response()
    try:
        response.data = c.register_resources(resources)
        response.status_code = http.HTTPStatus.OK
    except Exception as e:
        response.status_code = http.HTTPStatus.BAD_REQUEST
        response.data = f'Request:{request.data}.\nSomething went wrong in register_resources(): {e}'
    finally:
	    return response


@app.route('/share_resource_with_group', methods=['GET', 'POST'])
def share_resource_with_group():
    response = make_response()
    gr_sharings = [{
        "entity_id": c.resource_ids[0],
        "permission_type": "READ",
        "type": "EXPERIMENT",
        "group_name": 'Read Only Admin'
    }]
    try:
        response.data = c.share_resource_with_group(gr_sharings)
        response.status_code = http.HTTPStatus.OK
    except Exception as e:
        response.data = f'Request:{request.data}.\nSomething went wrong in share_resource_with_group(): {e}'
        response.status_code = http.HTTPStatus.BAD_REQUEST
    finally:
	    return response


@app.route('/share_resource_with_user', methods=['GET', 'POST'])
def share_resource_with_user():
    response = make_response()
    sharings = [
        {
            "entity_id": c.resource_ids[0],
            "permission_type": "READ",
            "type": "EXPERIMENT",
            "user_id": "abigaill"
        }
    ]
    try:
        response.data = c.share_resource_with_user(sharings)
        response.status_code = http.HTTPStatus.OK
    except Exception as e:
        response.status_code = http.HTTPStatus.BAD_REQUEST
        response.data = f'Request:{request.data}.\nSomething went wrong in share_resource_with_user(): {e}'
    finally:
	    return response


@app.route('/check_user_permissions', methods=['GET', 'POST'])
def check_user_permissions():
    response = make_response()
    try:
        response.data = c.check_user_permissions(users)
        response.status_code = http.HTTPStatus.OK
    except Exception as e:
        response.status_code = http.HTTPStatus.BAD_REQUEST
        response.data = f'Request:{request.data}.\nSomething went wrong in check_user_permissions(): {e}'
    finally:
	    return response




if __name__=='__main__':
    app.run(host='0.0.0.0', port='5005', use_reloader=False)