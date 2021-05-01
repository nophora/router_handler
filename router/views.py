from django.http import HttpResponse, JsonResponse
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient
from datetime import datetime
import random
import uuid
from bson import json_util, ObjectId


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


'''
client = MongoClient(
    'mongodb+srv://zips:zips@zips.rcqrf.mongodb.net/<dbname>?retryWrites=true&w=majority')
db = client.get_database('zips_db')
'''
print('xxxx!!!!!!!xxxx')


def info_view(request, *args, **kwargs):
    if request.method == 'GET':
        return JsonResponse({'info': 'the zips api will be than in two mounts from now'})
    else:
        return JsonResponse({error: '404'})


@csrf_exempt
def createProfile_view(request, *args, **kwargs):

    if request.method == 'POST':
        bytecode = request.body.decode('utf-8')
        data = json.loads(bytecode)
        check = pyload = data['payload']
        if data['type'] == 'create' and len(check['use_image']) > 10 and len(check['user_cover']) >= 10 and len(check['user_name']) >= 4 and len(check['user_lastname']) >= 4 and len(check['user_email']) >= 8 and len(check['user_digits']) >= 8 and len(check['user_password']) >= 6:
            print('creating!!!!!!!')
            pyload = data['payload']
            db_profile = db.user_profiles
            db_account = db.user_account
            x = datetime.now()
            f = pyload['user_name']
            l = pyload['user_lastname']
            meta = request.META
            randoms = random.randint(1000, 1000000)
            randoms_two = str(uuid.uuid4())
            user = {
                'username': meta['USERNAME'],
                'userdomain': meta['USERDOMAIN'],
                'computername': meta['COMPUTERNAME'],
                'os': meta['OS'],
                'os_id': meta['PROCESSOR_IDENTIFIER'],
                'user-agent': meta['HTTP_USER_AGENT'],
                'ip_address': meta['REMOTE_ADDR']
            }
            in_id = f"account{f[0:3]}{randoms}{pyload['user_name']}x{x}x{pyload['user_lastname']}{l[0:3]}{randoms_two}"
            initial_profile = {
                'initial_id': in_id,
                'use_image': pyload['user_lastname'],
                'user_name': pyload['user_name'],
                'user_lastname': pyload['user_lastname'],
                'user_email': pyload['user_email'],
                'user_digits': pyload['user_digits'],
                'user_password': pyload['user_password'],
                'user_iQcode': pyload['user_iQcode'],
                'user_logDevices': [user],
                'init_date': {'year': x.year, 'mouth': x.month, 'date': x.day, 'time': {'hour': x.hour, 'min': x.minute}}
            }

            initiate_accout = {
                'initial_id': in_id,
                'account': [{
                    'initial_id': in_id,
                    'use_image': pyload['user_lastname'],
                    'user_cover':pyload['user_lastname'],
                    'user_name': pyload['user_name'],
                    'user_lastname': pyload['user_lastname'],
                    'hide_email': 'false',
                    'hide_digits':'false',
                    'user_email':pyload['user_email'],
                    'user_digits':pyload['user_digits'],
                    'user_iQcode': pyload['user_iQcode'],
                    'init_date': {'year': x.year, 'mouth': x.month, 'date': x.day, 'time': {'hour': x.hour, 'min': x.minute}}
                }],
                'friends': [],
                'send_request': [],
                'received_request': [],
                'post_url': [],
                'data': [],
                'chats': [],
            }
            db_profile.insert_one(json.loads(json_util.dumps(initial_profile)))
            db_account.insert_one(json.loads(json_util.dumps(initiate_accout)))
            done_profile = db_profile.find_one({'initial_id': in_id})
            print(done_profile)
            print('||||||||||||||')
            print(initiate_accout)
            a = JSONEncoder().encode(done_profile)
            return JsonResponse([a], safe=False)
        elif data['type'] == 'image' and len(check['use_image']) > 10:
            print('image uplouding!!!!!')
            db_profile = db.user_profiles
            pyload = data['payload']
            user_id = data['initial_id']
            uncode = json.loads(json_util.dumps(pyload))
            db_profile.update_one({'initial_id': user_id}, {'$set': uncode})
            done_profile = db_profile.find_one({'initial_id': user_id})
            print(done_profile)
            a = JSONEncoder().encode(done_profile)
            return JsonResponse([a], safe=False)
        elif data['type'] == 'user_cover' and len(check['user_cover']) >= 10:
            print('cover uploading!!!!!')
            db_profile = db.user_profiles
            pyload = data['payload']
            user_id = data['initial_id']
            uncode = json.loads(json_util.dumps(pyload))
            db_profile.update_one({'initial_id': user_id}, {'$set': uncode})
            done_profile = db_profile.find_one({'initial_id': user_id})
            print(done_profile)
            a = JSONEncoder().encode(done_profile)
            return JsonResponse([a], safe=False)
        elif data['type'] == 'user_name' and len(check['user_name']) >= 4:
            print('user_name uplouding!!!!!')
            db_profile = db.user_profiles
            pyload = data['payload']
            user_id = data['initial_id']
            uncode = json.loads(json_util.dumps(pyload))
            db_profile.update_one({'initial_id': user_id}, {'$set': uncode})
            done_profile = db_profile.find_one({'initial_id': user_id})
            print(done_profile)
            a = JSONEncoder().encode(done_profile)
            return JsonResponse([a], safe=False)
        elif data['type'] == 'user_lastname' and len(check['user_lastname']) >= 4:
            print('user_lastname uplouding!!!!!')
            db_profile = db.user_profiles
            pyload = data['payload']
            user_id = data['initial_id']
            uncode = json.loads(json_util.dumps(pyload))
            db_profile.update({'initial_id': user_id}, {'$set': uncode})
            done_profile = db_profile.find_one({'initial_id': user_id})
            print(done_profile)
            a = JSONEncoder().encode(done_profile)
            return JsonResponse([a], safe=False)
        elif data['type'] == 'email' and len(check['user_email']) >= 8:
            print('email uplouding!!!!!')
            db_profile = db.user_profiles
            pyload = data['payload']
            user_id = data['initial_id']
            uncode = json.loads(json_util.dumps(pyload))
            db_profile.update_one({'initial_id': user_id}, {'$set': uncode})
            done_profile = db_profile.find_one({'initial_id': user_id})
            print(done_profile)
            a = JSONEncoder().encode(done_profile)
            return JsonResponse([a], safe=False)
        elif data['type'] == 'number' and len(check['user_digits']) >= 8:
            print('number uplouding!!!!!')
            db_profile = db.user_profiles
            pyload = data['payload']
            user_id = data['initial_id']
            uncode = json.loads(json_util.dumps(pyload))
            db_profile.update_one({'initial_id': user_id}, {'$set': uncode})
            done_profile = db_profile.find_one({'initial_id': user_id})
            print(done_profile)
            a = JSONEncoder().encode(done_profile)
            return JsonResponse([a], safe=False)
        elif data['type'] == 'user_password' and len(check['user_password']) >= 6:
            print('user_password uplouding!!!!!')
            db_profile = db.user_profiles
            pyload = data['payload']
            user_id = data['initial_id']
            uncode = json.loads(json_util.dumps(pyload))
            db_profile.update_one({'initial_id': user_id}, {'$set': uncode})
            done_profile = db_profile.find_one({'initial_id': user_id})
            print(done_profile)
            a = JSONEncoder().encode(done_profile)
            return JsonResponse([a], safe=False)
        else:
            pass
    else:
        return JsonResponse({error: '404'})


@ csrf_exempt
def hideauth_view(request, *args, **kwargs):
    if request.method == 'POST':
        bytecode = request.body.decode('utf-8')
        data = json.loads(bytecode)
        check = data['payload']
        if data['type'] == 'hide_email' and check['hide_email'] == 'true' or check['hide_email'] == 'false':
            db_profile = db.user_account
            pylaod = data['payload']
            user_id = data['initial_id']
            done_wait = db_profile.find_one({'initial_id': user_id})
            wait_obj = done_wait
            wait = done_wait['account']
            wt = wait[0]
            wt.update(pylaod)
            add = {'account': [wt]}
            wait_obj.update(add)
            uncode = json.loads(json_util.dumps(wait_obj))
            db_profile.update_one({'initial_id': user_id}, {'$set': uncode})
            done_account = db_profile.find_one({'initial_id': user_id})
            print(done_account)
            a = JSONEncoder().encode(done_account)
            return JsonResponse([a], safe=False)
        elif data['type'] == 'hide_number' and check['hide_digits'] == 'true' or check['hide_digits'] == 'false':
            db_profile = db.user_account
            pylaod = data['payload']
            user_id = data['initial_id']
            done_wait = db_profile.find_one({'initial_id': user_id})
            wait_obj = done_wait
            wait = done_wait['account']
            wt = wait[0]
            wt.update(pylaod)
            add = {'account': [wt]}
            wait_obj.update(add)
            uncode = json.loads(json_util.dumps(wait_obj))
            db_profile.update_one({'initial_id': user_id}, {'$set': uncode})
            done_account = db_profile.find_one({'initial_id': user_id})
            print(done_account)
            a = JSONEncoder().encode(done_account)
            return JsonResponse([a], safe=False)
        else:
            pass
    else:
        return JsonResponse({error: '404'})


@ csrf_exempt
def getProfile_view(request, *args, **kwargs):
    if request.method == 'POST':
        bytecode = request.body.decode('utf-8')
        data = json.loads(bytecode)
        check = data['payload']
        if data['type'] == 'login' and len(check['email']) >= 8 and len(check['password']) >= 6 and check['password'] != '123456':
            db_profile = db.user_profiles
            is_data = data['payload']
            email = is_data['email'],
            password = is_data['password']
            done_account = db_profile.find_one('email', email)
            if isinstance(done_account, dict) == True:
                psd = done_account['password']
                send = done_account if psd == password else {
                    'errow': 'wrong password'}
                a = JSONEncoder().encode(send)
                return JsonResponse([a], safe=False)
            else:
                return JsonResponse(['account may be duplecated'], safe=False)
        elif data['type'] == 'logout' and len(data['initial_id']) >= 10:
            db_profile = db.user_profiles
            done_account = db_profile.find_one(
                'initial_id', data['initial_id'])
            out = {'log': 'logout'} if isinstance(
                done_account, dict) == True else {'log': 'errow ocare try again later'}
            return JsonResponse([out], safe=False)
        else:
            pass
    else:
        return JsonResponse({'errow': '404'})


@ csrf_exempt
def sendrequest_view(request, *args, **kwargs):
    if request.method == 'POST':
        bytecode = request.body.decode('utf-8')
        data = json.loads(bytecode)
        pyload = data['payload']
        collect = pyload['collect']
        zero = collect[0]
        if data['type'] == 'send_request':
            # USER OPARATION
            db_account = db.user_account
            done_account = db_account.find_one(
                {'initial_id': data['initial_id']})
            you = JSONEncoder().encode(done_account)
            have_account = you['account']
            you_zero = have_account[0]
            add = {'send_request': you['send_request'] + collect}
            you.update(add)
            uncode = json.loads(json_util.dumps(you))
            db_account.update_one(
                {'initial_id': data['initial_id']}, {'$set': uncode})
            # FRIEND OPARATION
            other_account = db_account.find_one(
                {'initial_id': zero['initial_id']})
            other = JSONEncoder().encode(other_account)
            assign = [{
                'initial_id': you_zero['initial_id'],
                'use_image':you_zero['user_lastname'],
                'user_cover':you_zero['user_lastname'],
                'user_name': you_zero['user_name'],
                'user_lastname': you_zero['user_lastname'],
            }]
            add_other = {
                'received_request': other['received_request'] + assign}
            other.update(add_other)
            o_uncode = json.loads(json_util.dumps(other))
            db_account.update_one(
                {'initial_id': zero['initial_id']}, {'$set': o_uncode})
            send_account = db_account.find_one(
                {'initial_id': data['initial_id']})
            you_send = JSONEncoder().encode(send_account)
            return JsonResponse([you_send], safe=False)
        elif data['type'] == 'accept_request':
            # USER OPARATION
            db_account = db.user_account
            done_account = db_account.find_one(
                {'initial_id': data['initial_id']})
            you = JSONEncoder().encode(done_account)
            have_account = you['account']
            you_zero = have_account[0]
            filt_out = []
            for talue in you['received_request']:
                if talue['initial_id'] != zero['initial_id']:
                    filt_out += [talue]
            add = {'received_request': filt_out,
                   'friends': you['friends']+collect}
            you.update(add)
            uncode = json.loads(json_util.dumps(you))
            db_account.update_one(
                {'initial_id': data['initial_id']}, {'$set': uncode})
            # FRIEND OPARATION
            other_account = db_account.find_one(
                {'initial_id': zero['initial_id']})
            other = JSONEncoder().encode(other_account)
            assign = [{
                'initial_id': you_zero['initial_id'],
                'use_image':you_zero['user_lastname'],
                'user_cover':you_zero['user_lastname'],
                'user_name': you_zero['user_name'],
                'user_lastname': you_zero['user_lastname'],
            }]
            filt_sendout = []
            for values in you['send_request']:
                if values['initial_id'] != data['initial_id']:
                    filt_sendout += [values]

            add_other = {
                'send_request': filt_sendout, 'friends': other['friends'] + assign}
            other.update(add_other)
            o_uncode = json.loads(json_util.dumps(other))
            db_account.update_one(
                {'initial_id': zero['initial_id']}, {'$set': o_uncode})
            send_account = db_account.find_one(
                {'initial_id': data['initial_id']})
            you_send = JSONEncoder().encode(send_account)
            return JsonResponse([you_send], safe=False)
        elif data['type'] == 'reject_request':
            # USER OPARATION
            db_account = db.user_account
            done_account = db_account.find_one(
                {'initial_id': data['initial_id']})
            you = JSONEncoder().encode(done_account)
            have_account = you['account']
            you_zero = have_account[0]
            filt_out = []
            for malue in you['received_request']:
                if malue['initial_id'] != zero['initial_id']:
                    filt_out += [malue]
            add = {'received_request': filt_out}
            you.update(add)
            uncode = json.loads(json_util.dumps(you))
            db_account.update_one(
                {'initial_id': data['initial_id']}, {'$set': uncode})
            # FRIEND OPARATION
            other_account = db_account.find_one(
                {'initial_id': zero['initial_id']})
            other = JSONEncoder().encode(other_account)
            assign = [{
                'initial_id': you_zero['initial_id'],
                'use_image':you_zero['user_lastname'],
                'user_cover':you_zero['user_lastname'],
                'user_name': you_zero['user_name'],
                'user_lastname': you_zero['user_lastname'],
            }]
            filt_sendout = []
            for values in you['send_request']:
                if values['initial_id'] != data['initial_id']:
                    filt_sendout += [values]

            add_other = {
                'send_request': filt_sendout}
            other.update(add_other)
            o_uncode = json.loads(json_util.dumps(other))
            db_account.update_one(
                {'initial_id': zero['initial_id']}, {'$set': o_uncode})
            send_account = db_account.find_one(
                {'initial_id': data['initial_id']})
            you_send = JSONEncoder().encode(send_account)
            return JsonResponse([you_send], safe=False)
        elif data['type'] == 'un_friend':
            # USER OPARATION
            db_account = db.user_account
            done_account = db_account.find_one(
                {'initial_id': data['initial_id']})
            you = JSONEncoder().encode(done_account)
            have_account = you['account']
            you_zero = have_account[0]
            filt_out = []
            for salue in you['friends']:
                if salue['initial_id'] != zero['initial_id']:
                    filt_out += [salue]

            add = {'friends': filt_out}
            you.update(add)
            uncode = json.loads(json_util.dumps(you))
            db_account.update_one(
                {'initial_id': data['initial_id']}, {'$set': uncode})
            # FRIEND OPARATION
            other_account = db_account.find_one(
                {'initial_id': zero['initial_id']})
            other = JSONEncoder().encode(other_account)
            assign = [{
                'initial_id': you_zero['initial_id'],
                'use_image':you_zero['user_lastname'],
                'user_cover':you_zero['user_lastname'],
                'user_name': you_zero['user_name'],
                'user_lastname': you_zero['user_lastname'],
            }]
            filt_sendout = []
            for values in you['friends']:
                if values['initial_id'] != data['initial_id']:
                    filt_sendout += [values]

            add_other = {
                'friends': filt_sendout}
            other.update_one(add_other)
            o_uncode = json.loads(json_util.dumps(other))
            db_account.update(
                {'initial_id': zero['initial_id']}, {'$set': o_uncode})
            send_account = db_account.find_one(
                {'initial_id': data['initial_id']})
            you_send = JSONEncoder().encode(send_account)
            return JsonResponse([you_send], safe=False)
        else:
            pass
    else:
        return JsonResponse({'errow': '404'})


@ csrf_exempt
def createpost_view(request, *args, **kwargs):
    if request.method == 'POST':
        bytecode = request.body.decode('utf-8')
        data = json.loads(bytecode)
        pyload = data['payload']
        if data['type'] == 'post':
            # your account update
            db_account = db.user_account
            done_account = db_account.find_one(
                {'initial_id': data['initial_id']})
            you = JSONEncoder().encode(done_account)
            have_account = you['account']
            you_zero = have_account[0]
            randoms = random.randint(1000, 1000000)
            randoms_two = str(uuid.uuid4())
            x = datetime.now()
            f = you_zero['user_name']
            l = you_zero['user_lastname']
            in_id = f"post{f[0:3]}{randoms}{f}x{x}x{l}{l[0:3]}{randoms_two}"
            add = {'post_url': you['post_url'] + [in_id]}
            you.update(add)
            uncode = json.loads(json_util.dumps(you))
            db_account.update_one(
                {'initial_id': data['initial_id']}, {'$set': uncode})
            assign = [{
                'initial_id': you_zero['initial_id'],
                'use_image':you_zero['user_lastname'],
                'user_cover':you_zero['user_lastname'],
                'user_name': you_zero['user_name'],
                'user_lastname': you_zero['user_lastname'],
            }]
            # friends updates
            frinds = []
            for value in you['friends']:
                frinds += [value['initial_id']]
            find_them = list(db_account.find())
            other = JSONEncoder().encode(find_them)
            value_account = [d for d in other if d['initial_id'] in frinds]
            # foreach account add post
            for accountz in value_account:
                dates = accountz
                ispost = {'post_url': accountz['post_url']+[in_id]}
                dates.update_one(ispost)
                uncode = json.loads(json_util.dumps(dates))
                db_account.update_one(
                    {'initial_id': accountz['initial_id']}, {'$set': uncode})
            # create post
            db_post = db.user_posts
            post = {
                'post_id': in_id,
                'user': assign,
                'allow_share': pyload['allow_share'],
                'share': frinds,
                'rate': [],
                'share_rate': 0,
                'type': pyload['type'],
                'filter': pyload['filter'],
                'data': pyload['data'],
                'coments': [],
                'date': {'year': x.year, 'mouth': x.month, 'date': x.day, 'time': {'hour': x.hour, 'min': x.minute}}
            }
            db_post.insert_one(json.loads(json_util.dumps(post)))
            return JsonResponse(['post succesfully'], safe=False)
        else:
            return JsonResponse(['error ocare in you post'], safe=False)
    else:
        return JsonResponse({'errow': '404'}, safe=False)

# DELETE POST HERE AFTER CREATE


@ csrf_exempt
def deletepost_view(request, *args, **kwargs):
    if request.method == 'POST':
        bytecode = request.body.decode('utf-8')
        data = json.loads(bytecode)
        pyload = data['payload']
        if data['type'] == 'deletepost':
            # your account update
            db_account = db.user_account
            db_post = db.user_posts
            done_account = db_account.find_one(
                {'initial_id': data['initial_id']})
            you = JSONEncoder().encode(done_account)
            url = []
            for value in you['post_url']:
                if value != pyload['post_id']:
                    url += [value]
            upturl = {'post_url': url}
            you.update(upturl)
            uncode = json.loads(json_util.dumps(you))
            db_account.update_one(
                {'initial_id': data['initial_id']}, {'$set': uncode})
            find_them = list(db_account.find())
            other = JSONEncoder().encode(find_them)
            value_account = [
                d for d in other if d['initial_id'] in pyload['share']]
            for accountz in value_account:
                dates = accountz
                loopurl = []
                for valuex in you['post_url']:
                    if valuex != pyload['post_id']:
                        loopurl += [valuex]
                ispost = {'post_url': loopurl}
                dates.update(ispost)
                loopurl.clear()
                uncode = json.loads(json_util.dumps(dates))
                db_account.update_one(
                    {'initial_id': accountz['initial_id']}, {'$set': uncode})
            db_post.delete_one({'post_id': pyload['post_id']})
            return JsonResponse(['post deleted'], safe=False)
    else:
        return JsonResponse({'errow': '404'}, safe=False)


@ csrf_exempt
def getpost_view(request, *args, **kwargs):
    if request.method == 'POST':
        bytecode = request.body.decode('utf-8')
        data = json.loads(bytecode)
        pyload = data['payload']
        if data['type'] == 'getpost':
            db_account = db.user_account
            db_post = db.user_posts
            done_account = db_account.find_one(
                {'initial_id': data['initial_id']})
            you = JSONEncoder().encode(done_account)
            posts = you['post_url']
            find_them = list(db_post.find())
            other = JSONEncoder().encode(find_them)
            value_post = [d for d in other if d['post_id'] in you['post_url']]
            updat = {'data': value_post}
            you.update(updat)
            send = JSONEncoder().encode(you)
            return JsonResponse([send], safe=False)
    else:
        return JsonResponse({'errow': '404'}, safe=False)


@ csrf_exempt
def ratepost_view(request, *args, **kwargs):
    if request.method == 'POST':
        bytecode = request.body.decode('utf-8')
        data = json.loads(bytecode)
        pyload = data['payload']
        if data['type'] == 'ratepost':
            db_account = db.user_account
            db_post = db.user_posts
            done_account = db_account.find_one(
                {'initial_id': data['initial_id']})
            you = JSONEncoder().encode(done_account)
            have_account = you['account']
            you_zero = have_account[0]
            assign = [{
                'initial_id': you_zero['initial_id'],
                'use_image':you_zero['user_lastname'],
                'user_cover':you_zero['user_lastname'],
                'user_name': you_zero['user_name'],
                'user_lastname': you_zero['user_lastname'],
            }]
            done_post = db_post.find_one(
                {'post_id': pyload['post_id']})
            post = JSONEncoder().encode(done_post)
            rate = {'rate': post['rate'] + assign}
            post.update(rate)
            uncode = json.loads(json_util.dumps(post))
            db_post.update_one(
                {'post_id': pyload['post_id']}, {'$set': uncode})
            done_send = db_post.find_one(
                {'post_id': pyload['post_id']})
            send = JSONEncoder().encode(done_send)
            return JsonResponse([send], safe=False)
        elif data['type'] == 'un_ratepost':
            db_post = db.user_posts
            done_post = db_post.find_one(
                {'post_id': pyload['post_id']})
            post = JSONEncoder().encode(done_post)
            were = []
            for value in post['rate']:
                if value['initial_id'] != data['initial_id']:
                    were += [value]
            rate = {'rate': were}
            post.update(rate)
            uncode = json.loads(json_util.dumps(post))
            db_post.update_one(
                {'post_id': pyload['post_id']}, {'$set': uncode})
            done_send = db_post.find_one(
                {'post_id': pyload['post_id']})
            send = JSONEncoder().encode(done_send)
            return JsonResponse([send], safe=False)
        else:
            pass
    else:
        return JsonResponse({'errow': '404'}, safe=False)


@ csrf_exempt
def sharepost_view(request, *args, **kwargs):
    if request.method == 'POST':
        bytecode = request.body.decode('utf-8')
        data = json.loads(bytecode)
        pyload = data['payload']
        if data['type'] == 'share':
            db_account = db.user_account
            db_post = db.user_posts
            done_account = db_account.find_one(
                {'initial_id': data['initial_id']})
            you = JSONEncoder().encode(done_account)
            done_post = db_post.find_one(
                {'post_id': pyload['post_id']})
            post = JSONEncoder().encode(done_post)
            port = post['user']
            zero = port[0]
            new_friends = []
            for user in you['friends']:
                if user['initial_id'] != zero['initial_id']:
                    new_friends += [user]
            only_id = []
            for only in new_friends:
                only_id += [only['initial_id']]
            resultout = [d for d in only_id if d not in post['share']]
            udate = {'share': post['share'] + resultout,
                     'share_rate': post['share_rate'] + 1}
            post.update(udate)
            uncode = json.loads(json_util.dumps(post))
            db_post.update_one(
                {'post_id': pyload['post_id']}, {'$set': uncode})
            find_them = list(db_account.find())
            other = JSONEncoder().encode(find_them)
            value_account = [d for d in other if d['initial_id'] in only_id]
            for accountz in value_account:
                dates = accountz
                ispost = {'post_url': accountz['post_url']+[post['post_id']]}
                dates.update(ispost)
                uncode = json.loads(json_util.dumps(dates))
                db_account.update_one(
                    {'initial_id': accountz['initial_id']}, {'$set': uncode})
            done_send = db_post.find_one(
                {'post_id': pyload['post_id']})
            send = JSONEncoder().encode(done_send)
            return JsonResponse([send], safe=False)
    else:
        return JsonResponse({'errow': '404'}, safe=False)


@ csrf_exempt
def comment_reply_view(request, *args, **kwargs):
    if request.method == 'POST':
        bytecode = request.body.decode('utf-8')
        data = json.loads(bytecode)
        pyload = data['payload']
        if data['type'] == 'comment':
            db_account = db.user_account
            db_post = db.user_posts
            done_account = db_account.find_one(
                {'initial_id': data['initial_id']})
            you = JSONEncoder().encode(done_account)
            done_post = db_post.find_one(
                {'post_id': pyload['post_id']})
            post = JSONEncoder().encode(done_post)
            port = you['account']
            zero = port[0]
            assign = [{
                'initial_id': zero['initial_id'],
                'use_image':zero['user_lastname'],
                'user_cover':zero['user_lastname'],
                'user_name': zero['user_name'],
                'user_lastname': zero['user_lastname'],
            }]
            randoms = random.randint(1000, 1000000)
            randoms_two = str(uuid.uuid4())
            x = datetime.now()
            f = zero['user_name']
            l = zero['user_lastname']
            in_id = f"comment{f[0:3]}{randoms}{f}x{x}x{l}{l[0:3]}{randoms_two}"
            create_post = [{
                'comment_id': in_id,
                'user': assign,
                'data': pyload['data'],
                'sticker': pyload['sticker'],
                'reply': [],
                'rate': [],
                'date':{'year': x.year, 'mouth': x.month, 'date': x.day, 'time': {'hour': x.hour, 'min': x.minute}}
            }]
            commt = {'coments': post['coments'] + create_post}
            post.update(commt)
            uncode = json.loads(json_util.dumps(post))
            db_post.update_one(
                {'post_id': pyload['post_id']}, {'$set': uncode})
            sendp = db_post.find_one(
                {'post_id': pyload['post_id']})
            send = JSONEncoder().encode(sendp)
            return JsonResponse([send], safe=False)
        elif data['type'] == 'reply':
            db_account = db.user_account
            db_post = db.user_posts
            done_account = db_account.find_one(
                {'initial_id': data['initial_id']})
            you = JSONEncoder().encode(done_account)
            done_post = db_post.find_one(
                {'post_id': pyload['post_id']})
            post = JSONEncoder().encode(done_post)
            port = you['account']
            zero = port[0]
            assign = [{
                'initial_id': zero['initial_id'],
                'use_image':zero['user_lastname'],
                'user_cover':zero['user_lastname'],
                'user_name': zero['user_name'],
                'user_lastname': zero['user_lastname'],
            }]
            randoms = random.randint(1000, 1000000)
            randoms_two = str(uuid.uuid4())
            x = datetime.now()
            f = zero['user_name']
            l = zero['user_lastname']
            in_id = f"reply{f[0:3]}{randoms}{f}x{x}x{l}{l[0:3]}{randoms_two}"
            create_reply = [{
                'reply_id': in_id,
                'user': assign,
                'data': pyload['data'],
                'sticker': pyload['sticker'],
                'rate': [],
                'date':{'year': x.year, 'mouth': x.month, 'date': x.day, 'time': {'hour': x.hour, 'min': x.minute}}
            }]
            comment_out = []
            for value in post['comments']:
                if value['comment_id'] != pyload['comment_id']:
                    comment_out += [value]
            comment_split = {}
            for value in post['comments']:
                if value['comment_id'] == pyload['comment_id']:
                    comment_split = value
            replyup = {'reply': comment_split['reply'] + create_reply}
            comment_split.update(replyup)
            comz = {'coments': comment_out + [comment_split]}
            post.update(comz)
            uncode = json.loads(json_util.dumps(post))
            db_post.update_one(
                {'post_id': pyload['post_id']}, {'$set': uncode})
            sendp = db_post.find_one(
                {'post_id': pyload['post_id']})
            send = JSONEncoder().encode(sendp)
            return JsonResponse([send], safe=False)
        else:
            pass
    else:
        return JsonResponse({'errow': '404'}, safe=False)


@ csrf_exempt
def rate_comment_view(request, *args, **kwargs):
    if request.method == 'POST':
        bytecode = request.body.decode('utf-8')
        data = json.loads(bytecode)
        pyload = data['payload']
        if data['type'] == 'comment_rate':
            db_post = db.user_posts
            db_account = db.user_account
            done_account = db_account.find_one(
                {'initial_id': data['initial_id']})
            you = JSONEncoder().encode(done_account)
            have_account = you['account']
            you_zero = have_account[0]
            assign = [{
                'initial_id': you_zero['initial_id'],
                'use_image':you_zero['user_lastname'],
                'user_cover':you_zero['user_lastname'],
                'user_name': you_zero['user_name'],
                'user_lastname': you_zero['user_lastname'],
            }]
            done_post = db_post.find_one(
                {'post_id': pyload['post_id']})
            post = JSONEncoder().encode(done_post)
            port = post['coments']
            not_comment = []
            for values in port:
                if values['comment_id'] != pyload['comment_id']:
                    found_comment += [values]
            for value in port:
                if value['comment_id'] == pyload['comment_id']:
                    not_comment += [{
                        'comment_id': value['comment_id'],
                        'user': value['user'],
                        'data': value['data'],
                        'sticker': value['sticker'],
                        'reply': value['reply'],
                        'rate': value['rate']+assign,
                        'date':value['date'],
                    }]
            comz = {'coments': not_comment}
            post.update(comz)
            uncode = json.loads(json_util.dumps(post))
            db_post.update_one(
                {'post_id': pyload['post_id']}, {'$set': uncode})
            done_send = db_post.find_one(
                {'post_id': pyload['post_id']})
            send = JSONEncoder().encode(done_send)
            return JsonResponse([send], safe=False)
        elif data['type'] == 'comment_unrate':
            db_post = db.user_posts
            db_account = db.user_account
            done_account = db_account.find_one(
                {'initial_id': data['initial_id']})
            you = JSONEncoder().encode(done_account)
            have_account = you['account']
            you_zero = have_account[0]
            done_post = db_post.find_one(
                {'post_id': pyload['post_id']})
            post = JSONEncoder().encode(done_post)
            port = post['coments']
            not_comment = []
            for values in port:
                if values['comment_id'] != pyload['comment_id']:
                    found_comment += [values]
            comment_filter = {}
            for value in port:
                if value['comment_id'] == pyload['comment_id']:
                    comment_filter = value
            rate = []
            for rater in rate_filter['rate']:
                if rater['initial_id'] != you_zero['initial_id']:
                    rate += [rater]
            unrate = {'rate': rate}
            rate_filter.update(unrate)
            comz = {'coments': not_comment+[comment_filter]}
            post.update(comz)
            uncode = json.loads(json_util.dumps(post))
            db_post.update_one(
                {'post_id': pyload['post_id']}, {'$set': uncode})
            done_send = db_post.find_one(
                {'post_id': pyload['post_id']})
            send = JSONEncoder().encode(done_send)
            return JsonResponse([send], safe=False)
        elif data['type'] == 'delete':
            db_post = db.user_posts
            done_post = db_post.find_one(
                {'post_id': pyload['post_id']})
            post = JSONEncoder().encode(done_post)
            port = post['coments']
            found_comment = {}
            user = found_comment['user']
            zero_one = user[0]
            for value in port:
                if value['comment_id'] == pyload['comment_id']:
                    found_comment = value
            if zero_one['initial_id'] == data['initial_id']:
                not_comment = []
                for delet in port:
                    if delet['comment_id'] != pyload['comment_id']:
                        not_comment += [delet]
                comz = {'coments': not_comment}
                post.update(comz)
                uncode = json.loads(json_util.dumps(post))
                db_post.update_one(
                    {'post_id': pyload['post_id']}, {'$set': uncode})
                done_send = db_post.find_one(
                    {'post_id': pyload['post_id']})
                send = JSONEncoder().encode(done_send)
                return JsonResponse([send], safe=False)
        else:
            pass
    else:
        return JsonResponse({'errow': '404'}, safe=False)


@ csrf_exempt
def rate_reply_view(request, *args, **kwargs):
    if request.method == 'POST':
        bytecode = request.body.decode('utf-8')
        data = json.loads(bytecode)
        pyload = data['payload']
        if data['type'] == 'reply_rate':
            db_post = db.user_posts
            db_account = db.user_account
            done_account = db_account.find_one(
                {'initial_id': data['initial_id']})
            you = JSONEncoder().encode(done_account)
            have_account = you['account']
            you_zero = have_account[0]
            assign = [{
                'initial_id': you_zero['initial_id'],
                'use_image':you_zero['user_lastname'],
                'user_cover':you_zero['user_lastname'],
                'user_name': you_zero['user_name'],
                'user_lastname': you_zero['user_lastname'],
            }]
            done_post = db_post.find_one(
                {'post_id': pyload['post_id']})
            post = JSONEncoder().encode(done_post)
            # DEALING WITH COMMENTS
            port = post['coments']
            not_comment = []
            for values in port:
                if values['comment_id'] != pyload['comment_id']:
                    found_comment += [values]
            comAndreply = {}
            for value in port:
                if value['comment_id'] == pyload['comment_id']:
                    reply_com = value
            # DEALG WITH REPLYS
            reply_not = []
            for value in comAndreply['reply']:
                if value['reply_id'] != pyload['reply_id']:
                    reply_not += [value]
            reply_find = {}
            for valuer in comAndreply['reply']:
                if valuer['reply_id'] == pyload['reply_id']:
                    reply_find = valuer
            # MAKE UPDATES1
            reply_f = {'rate': reply_find['rate'] + assign}
            reply_find.update(reply_f)
            # MAKE UPDATES2
            comz = {'reply': reply_not + [reply_find]}
            comAndreply.update(comz)
            # MAKE UPDATES3
            postcom = {'coments': not_comment+[comAndreply]}
            post.update(postcom)
            uncode = json.loads(json_util.dumps(post))
            db_post.update_one(
                {'post_id': pyload['post_id']}, {'$set': uncode})
            done_send = db_post.find_one(
                {'post_id': pyload['post_id']})
            send = JSONEncoder().encode(done_send)
            return JsonResponse([send], safe=False)
        elif data['type'] == 'reply_unrate':
            db_post = db.user_posts
            db_account = db.user_account
            done_account = db_account.find_one(
                {'initial_id': data['initial_id']})
            you = JSONEncoder().encode(done_account)
            have_account = you['account']
            you_zero = have_account[0]
            done_post = db_post.find_one(
                {'post_id': pyload['post_id']})
            post = JSONEncoder().encode(done_post)
            # DLING WITH COMMENTS
            port = post['coments']
            not_comment = []
            for values in port:
                if values['comment_id'] != pyload['comment_id']:
                    found_comment += [values]
            comment_filter = {}
            for value in port:
                if value['comment_id'] == pyload['comment_id']:
                    comment_filter = value
            # DEALING WITH REPLYS
            reply_not = []
            for replys in comment_filter['reply']:
                if replys['reply_id'] != pyload['reply_id']:
                    reply_not += [replys]
            reply_find = {}
            for replyz in comment_filter['reply']:
                if replyz['reply_id'] == pyload['reply_id']:
                    reply_find = replyz
            # FILTER REPLYS RATE
            reply_notid = []
            for replyt in reply_find['rate']:
                if replyt['reply_id'] != data['initial_id']:
                    reply_notid += [replyt]
            # UPDATE REPLYS1
            updt = {'rate': reply_notid}
            reply_find.update(updt)
            # UPDATE COMMENTS REPLY2
            uptcomz = {'reply': reply_not + [reply_find]}
            comment_filter.update(uptcomz)
            # UPDATE FIND COMMENT IN POST
            uptcompt = {'coments': not_comment + [comment_filter]}
            post.update(uptcompt)
            uncode = json.loads(json_util.dumps(post))
            db_post.update_one(
                {'post_id': pyload['post_id']}, {'$set': uncode})
            done_send = db_post.find_one(
                {'post_id': pyload['post_id']})
            send = JSONEncoder().encode(done_send)
            return JsonResponse([send], safe=False)
        elif data['type'] == 'reply_delete':
            db_post = db.user_posts
            done_post = db_post.find_one(
                {'post_id': pyload['post_id']})
            post = JSONEncoder().encode(done_post)
            # DEALING WITH COMMENTS
            port = post['coments']

            not_comment = []
            for values in port:
                if values['comment_id'] != pyload['comment_id']:
                    found_comment += [values]
            comment_filter = {}
            for value in port:
                if value['comment_id'] == pyload['comment_id']:
                    comment_filter = value

            # CHEACK ID
            reply_find = {}
            userof = ['user']
            userzero = userof[0]
            for replyz in comment_filter['reply']:
                if replyz['reply_id'] == pyload['reply_id']:
                    reply_find = replyz

            if userzero['initial_id'] == data['initial_id']:
                # REPLY OUT
                reply_not = []
                for replys in comment_filter['reply']:
                    if replys['reply_id'] != pyload['reply_id']:
                        reply_not += [replys]
                # UPDATE COMMENTS REPLY1
                uptcomz = {'reply': reply_not}
                comment_filter.update(uptcomz)
                # UPDATE FIND COMMENT IN POST
                uptcompt = {'coments': not_comment + [comment_filter]}
                post.update(uptcompt)
                uncode = json.loads(json_util.dumps(post))
                db_post.update_one(
                    {'post_id': pyload['post_id']}, {'$set': uncode})
                done_send = db_post.find_one(
                    {'post_id': pyload['post_id']})
                send = JSONEncoder().encode(done_send)
                return JsonResponse([send], safe=False)
        else:
            pass
    else:
        return JsonResponse({'errow': '404'}, safe=False)
