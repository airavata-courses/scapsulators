admin_user_name = 'shmoha@iu.edu'
admin_password = 'Scapsulators2022!'


# register_users()
users = [
    {
        'username': 'alice',
        'first_name': 'Alice',
        'last_name': 'Aron',
        'password': '12345678',
        'email': 'alice@gmail.com'
    },
    {
        'username': 'audrey',
        'first_name': 'Audrey',
        'last_name': 'Aron',
        'password': '12345678',
        'email': 'audrey@gmail.com'
    },
    {
        'username': 'sophia',
        'first_name': 'Sophia',
        'last_name': 'Aron',
        'password': '12345678',
        'email': 'sophia@gmail.com'
    },
    {
        'username': 'abelota',
        'first_name': 'Abelota',
        'last_name': 'Aron',
        'password': '12345678',
        'email': 'abelota@gmail.com'
    },
    {
        'username': 'abigaill',
        'first_name': 'Abigaill',
        'last_name': 'Aron',
        'password': '12345678',
        'email': 'abigaill@gmail.com'
    },
    {
        'username': 'adalee',
        'first_name': 'Adalee',
        'last_name': 'Aron',
        'password': '12345678',
        'email': 'adalee@gmail.com'
    }
]




# create_groups()
groups = [
    {
        'name': 'Admin',
        'description': 'Group for gateway read only admins',
        'owner_id': admin_user_name
    },
    {
        'name': 'Read Only Admin',
        'description': 'Group for gateway admins',
        'owner_id': admin_user_name
    },
    {
        'name': 'Gateway User',
        'description': 'Group  for gateway users',
        'owner_id': admin_user_name
    }
]



# allocate_users_to_groups()
user_group_mapping = [
    {
        'group_name': 'Admin',
        'username': 'alice'
    },
    {
        'group_name': 'Admin',
        'username': 'audrey'
    },
    {
        'group_name': 'Read Only Admin',
        'username': 'sophia'
    },
    {
        'group_name': 'Read Only Admin',
        'username': 'abelota'
    },
    {
        'group_name': 'Gateway User',
        'username': 'abigaill'
    },
    {
        'group_name': 'Gateway User',
        'username': 'adalee'
    }
]




# allocate_child_group_to_parent_group
child_gr_parent_gr_mapping = [
    {
        "child_name": 'Admin',
        "parent_name": 'Read Only Admin'
    }
]





# create_permissions()
permissions = [
    {
        'id': 'READ',
        'name': 'READ',
        'description': 'Read permission'
    },
    {
        'id': 'WRITE',
        'name': 'WRITE',
        'description': 'WRITE permission'
    }
]






# create_entity_types()
entity_types = [
    {
        'id': 'PROJECT',
        'name': 'PROJECT',
        'description': 'PROJECT entity type'
    },
    {
        'id': 'EXPERIMENT',
        'name': 'EXPERIMENT',
        'description': 'EXPERIMENT entity type'
    }
]




# register_resources()
resources = [
    {
        'name': 'SEAGRD_EXP',
        'description': 'Register an experiment',
        'user_id': admin_user_name,
        'type': 'EXPERIMENT'
    }
]