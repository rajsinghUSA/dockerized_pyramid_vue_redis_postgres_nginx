from testsite.models import DBSession
from testsite.models import User
from pyramid.security import Everyone, Authenticated, Allow, ALL_PERMISSIONS
from pyramid.security import authenticated_userid
from pyramid.decorator import reify

from pyramid.httpexceptions import HTTPForbidden
from sqlalchemy.orm.exc import NoResultFound

import pdb

#searches for each user's groups to return their principal for RootFactory
def groupfinder(username, request):
    print('****groupfinder****')
    pdb.set_trace()
    print("*********************************")
    print("security.py's GROUPFINDER at work for ", username)
    print("request from-->", request.url)
    print("Matched route: ", request.matched_route.name)
    print("User's IP address: ", request.remote_addr)

    if username[:5] == 'Guest':
        grouplist = [('group:guest')]
        return grouplist

    try:
        """print 'security.py doing a db query:\n' """
        user = DBSession.query(User).filter(User.username==username).one()
        grouplist = [('group:%s' % group.group_name) for group in user.groups]
        grouplist.append(('group:auth'))
    except NoResultFound as e:
        print("security.py returning none")
        return None

    return grouplist



def add_role_principals(userid, request):
    return ['role:%s' % role for role in request.jwt_claims.get('roles', [])]



#####################################################################
class RootFactory(object):                                        ###
    __acl__ = [                                                   ###
        (Allow, 'group:guest', 'view'),#(Allow, Everyone, 'view') ###
        (Allow, 'group:auth', ('view','auth')),                   ###
#        (Allow, 'group:owner', ('auth', 'owner')),               ###
        (Allow, 'group:admin', ('view', 'auth','admin')),         ###
        (Allow, 'group:superadmin', ALL_PERMISSIONS)              ###
    ]                                                             ###
                                                                  ###
                                                                  ###
    def __init__(self, request):
        # pdb.set_trace()                                           ###
        self.request = request                                    ###
#####################################################################
