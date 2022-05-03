import json
import random, string
from custos.clients.user_management_client import UserManagementClient
from custos.clients.group_management_client import GroupManagementClient
from custos.clients.resource_secret_management_client import ResourceSecretManagementClient
from custos.clients.sharing_management_client import SharingManagementClient
from custos.clients.identity_management_client import IdentityManagementClient
from custos.transport.settings import CustosServerClientSettings
import custos.clients.utils.utilities as utl
from google.protobuf.json_format import MessageToJson


class Custos:
    def __init__(self, admin_username, admin_password):
        # read settings
        self.custos_settings = CustosServerClientSettings(custos_host='custos.scigap.org',
                        custos_port='31499', 
                        custos_client_id='custos-nvceqrnlbg6ftlvhsim4-10003424',
                        custos_client_sec='cA2lzsWR2p1BAdVUx3eORw8GPQbSHyRdJfk1fpKh'
                        )
        # create custos user management client
        self.user_management_client = UserManagementClient(self.custos_settings)
        # create custos group management client
        self.group_management_client = GroupManagementClient(self.custos_settings)
        # create custos resource secret client
        self.resource_secret_client = ResourceSecretManagementClient(self.custos_settings)
        # create sharing management client
        self.sharing_management_client = SharingManagementClient(self.custos_settings)
        # create identity management client
        self.identity_management_client = IdentityManagementClient(self.custos_settings)
        # obtain base 64 encoded token for tenant
        self.b64_encoded_custos_token = utl.get_token(custos_settings=self.custos_settings)
        self.created_groups = {}
        self.admin_user_name = admin_username
        self.admin_password = admin_password
        self.resource_ids = []
        print('Successfully configured all custos clients')



    def verify_user(self, login_user_id, login_user_password):
        print('Login user '+ login_user_id)
        login_reponse = self.identity_management_client.token(token=self.b64_encoded_custos_token, username=login_user_id, password=login_user_password, grant_type='password')
        login_reponse = MessageToJson(login_reponse)
        print('Login response: ', login_reponse)
        response = self.user_management_client.get_user(token=self.b64_encoded_custos_token, username=login_user_id)
        print(' Updating user profile...  ')
        self.user_management_client.update_user_profile(
            token=self.b64_encoded_custos_token,
            username=response.username,
            email=response.email,
            first_name=response.first_name,
            last_name=response.last_name)
        return f'User {login_user_id} successfully logged in and updated profile'



    def register_users(self, users):
        usernames = []
        for user in users:
              i = random.randint(0,10)
              username = f'{user["username"]}{i}'
              usernames.append(username)
              self.user_management_client.register_user(token=self.b64_encoded_custos_token,
                                                 username=username,
                                                 first_name=f'{user["first_name"]}{i}',
                                                 last_name=user['last_name'],
                                                 password=user['password'],
                                                 email=f"{user['email']}{i}",
                                                 is_temp_password=False)
              self.user_management_client.enable_user(token=self.b64_encoded_custos_token, username=user['username'])
        return f'Registered users: {[usernames]}'



    def create_groups(self, groups):
        for group in groups:
                grResponse = self.group_management_client.create_group(
                    token=self.b64_encoded_custos_token,
                    name=group['name'],
                    description=group['description'],
                    owner_id=group['owner_id'])
                resp = MessageToJson(grResponse)
                print(resp)
                respData = json.loads(resp)
                print('Created group id of '+ group['name'] + ': ' +respData['id'] )
                self.created_groups[respData['name']] = respData['id']
        return f'Created groups: {groups}'

    
    def allocate_users_to_groups(self, user_group_mapping):
        for usr_map in user_group_mapping:
                group_id = self.created_groups[usr_map['group_name']]
                print('Assigning user ' + usr_map['username'] + ' to group ' + usr_map['group_name'])
                val = self.group_management_client.add_user_to_group(token=self.b64_encoded_custos_token,
                                                            username=usr_map['username'],
                                                            group_id=group_id,
                                                            membership_type='Member')
                resp = MessageToJson(val)
                print(resp)
        return f'Allocated users to groups: {user_group_mapping}'


    def allocate_child_group_to_parent_group(self, gr_gr_mapping):
        for gr_map in gr_gr_mapping:
                child_id = self.created_groups[gr_map['child_name']]
                parent_id = self.created_groups[gr_map['parent_name']]
                print('Assigning child group ' + gr_map['child_name'] + ' to parent group ' + gr_map['parent_name'])
                self.group_management_client.add_child_group(
                    token=self.b64_encoded_custos_token,
                    parent_group_id=parent_id,
                    child_group_id=child_id)
        return f'Allocated child group to parent group: {gr_gr_mapping}'


    def create_permissions(self, permissions):
        for perm in permissions:
                self.sharing_management_client.create_permission_type(token=self.b64_encoded_custos_token,
                                                            client_id=self.custos_settings.CUSTOS_CLIENT_ID,
                                                            id=perm['id'],
                                                            name=perm['name'],
                                                            description=perm['description'])
        return f'Created permissions {perm}'
    

    def create_entity_types(self, entity_types):
        for type in entity_types:
                self.sharing_management_client.create_entity_type(token=self.b64_encoded_custos_token,
                                                        client_id=self.custos_settings.CUSTOS_CLIENT_ID,
                                                        id=type['id'],
                                                        name=type['name'],
                                                        description=type['description'])
        return f'Creating entity types {entity_types}'



    def register_resources(self, resources):
        for resource in resources:
            id =  resource['name'].join(random.choice(string.ascii_letters) for x in range(5))
            self.resource_ids.append(id)
            resource['id']=id
            print('Register resources ' + resource['name'] + ' generated ID : '+resource['id'] )
            self.sharing_management_client.create_entity(token=self.b64_encoded_custos_token,
                                                    client_id=self.custos_settings.CUSTOS_CLIENT_ID,
                                                    id=resource['id'],
                                                    name=resource['name'],
                                                    description=resource['description'],
                                                    owner_id=resource['user_id'],
                                                    type=resource['type'],
                                                    parent_id='')
        return f'Registered resources: {resources}'



    def share_resource_with_group(self, gr_sharings):
        for shr in gr_sharings:
                group_id = self.created_groups[shr['group_name']]
                print('Sharing entity ' + shr['entity_id'] + ' with group ' + shr['group_name'] + ' with permission ' + shr['permission_type'])
                self.sharing_management_client.share_entity_with_groups(token=self.b64_encoded_custos_token,
                                                                client_id=self.custos_settings.CUSTOS_CLIENT_ID,
                                                                entity_id=shr['entity_id'],
                                                                permission_type=shr['permission_type'],
                                                                group_id=group_id)
        return f'Shared entities with groups {gr_sharings}'


    def share_resource_with_user(self, sharings):
        for shr in sharings:
                print('Sharing entity ' + shr['entity_id'] + ' with user ' + shr['user_id'] + ' with permission ' + shr['permission_type'])
                self.sharing_management_client.share_entity_with_users(token=self.b64_encoded_custos_token,
                                                                client_id=self.custos_settings.CUSTOS_CLIENT_ID,
                                                                entity_id=shr['entity_id'],
                                                                permission_type=shr['permission_type'],
                                                                user_id=shr['user_id']
                                                                )
        return f'Shared resources with users: {sharings}'


    def check_user_permissions(self, users):
        accesses = {}
        for user in users:
                access = self.sharing_management_client.user_has_access(token=self.b64_encoded_custos_token,
                                                                client_id=self.custos_settings.CUSTOS_CLIENT_ID,
                                                                entity_id=self.resource_ids[0],
                                                                permission_type='READ',
                                                                user_id=user["username"])
                accesses[user["username"]] = access
                print(f'Access for user {user["username"]}: {access}')
        return f'Users have access: {accesses}'