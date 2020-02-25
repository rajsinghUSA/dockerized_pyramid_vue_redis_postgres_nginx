import pdb
import datetime
import json
from pyramid.view import view_config
from pyramid.response import Response

from testsite.models import DBSession
from testsite.models import User

######################################################################
#   Index View
# perm should be 'view'
@view_config(route_name='home')
def home(request):
    print("\n\nHey New Index view ", "on", datetime.datetime.now(), "\n\n")
#    print "accessed by: ", request.user.username if request.user else 'unauthenticated user @', request.remote_addr
    # print("on", datetime.datetime.now(), "\n\n")
 #   pdb.set_trace()
#    return Response('Authenticated: {0}'.format(unauthenticated_userid(request)))
    return Response('<body><h1>New Home page!</h1></body>')




@view_config(route_name='auth')
def auth(request):
    print("\nAuth view xxxxxxxxxxxxxxxxxxxxxxx on ", datetime.datetime.now(), "\n\n")
    data = request.json_body
    email = data['email']

    pdb.set_trace()
    
    if User.check_password(login, password):
        user = DBSession.query(User).filter(User.username == login).first()\
            or DBSession.query(User).filter(User.email == login).first()
        login = user.username
        headers = remember(request, login)

        result = HTTPFound(location=came_from, headers=headers)
        result.set_cookie('username', user.username)
        groups = [group.group_name for group in user.groups]
        result.set_cookie('permissions', ';'.join(groups))
        request.session.flash('Logged In')

        return result

    else:
        user = DBSession.query(User).filter(User.username == login).first()\
                or DBSession.query(User).filter(User.email == login).first()
        pdb.set_trace()
        if user is None:
            reg_route = request.route_url('registration_page')
            link = "<a class='registerlink' href='%s'>register</a>" % reg_route
            err_msg = "That username does not exist, but you can %s it." % link
            raise BadUsername(err_msg, came_from)
        else:
            profile_route = request.route_url('profile',
                                              username=user.username)
            profilelink = "<a href='%s'>%s</a>" % (profile_route, login)
            error_msg = "Incorrect password for %s" % profilelink
            raise BadPassword(error_msg, came_from)



    pdb.set_trace()

    user = DBSession.query(user)

    return {
            'result': 'ok',
            'token': request.create_jwt_token(user_id)
        }
#    print "accessed by: ", request.user.username if request.user else 'unauthenticated user @', request.remote_addr
    # print("on", datetime.datetime.now(), "\n\n")

#    return Response('Authenticated: {0}'.format(unauthenticated_userid(request)))
    #return Response('<body><h1>Auth endpoint!</h1></body>')
