from rest_framework.renderers import JSONRenderer
from django.shortcuts import render, HttpResponse, redirect
from chairmanapp.models import *
from django.core.mail import send_mail
import random
from django.conf import settings
from .paytm import generate_checksum, verify_checksum

from .serializer import *
# Create your views here.



def societymember_profile(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        sid = Societymember.objects.get(user_id=uid)
        if request.POST:
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            sid.firstname = firstname
            sid.lastname = lastname
            sid.save()

            context = {
                'uid': uid,
                'sid': sid
            }
            return render(request, 'societymemberapp/profile.html', context)

        else:
            context = {
                'uid': uid,
                'sid': sid
            }
            return render(request, 'societymemberapp/profile.html', context)

    else:
        return redirect('login')


def societymember_pass_change(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        sid = Societymember.objects.get(user_id=uid)

        if request.POST:
            currentpassword = request.POST['currentpassword']
            newpassword = request.POST['newpassword']
            if uid.password == currentpassword:
                uid.password = newpassword
                uid.save()
                return redirect('logout')
            else:
                pass
            context = {
                'uid': uid,
                'sid': sid
            }
            return render(request, 'societymemberapp/profile.html', context)

        else:
            context = {
                'uid': uid,
                'sid': sid,
            }
            return render(request, "societymemberapp/profile.html", context)
    else:
        return redirect('login')


def notice_list_society(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        sid = Societymember.objects.get(user_id=uid)

        nall = Notice.objects.all()
        context = {
            'uid': uid,
            'sid': sid,
            'nall': nall
        }
        return render(request, 'societymemberapp/notice-list-society.html', context)
    else:
        context = {
            'uid': uid,
            'sid': sid,
        }
        return render(request, 'societymemberapp/notice-list-society.html', context)


def notice_detail_views_society(request, pk):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        sid = Societymember.objects.get(user_id=uid)

        nid = Notice.objects.filter(id=pk)
        context = {
            'uid': uid,
            'sid': sid,
            'nall': nid
        }
        return render(request, 'societymemberapp/notice-detail-view-society.html', context)
    else:
        context = {
            'uid': uid,
            'sid': sid,
        }
        return render(request, 'societymemberapp/notice-detail-view-society.html', context)


def add_complaint(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        sid = Societymember.objects.get(user_id=uid)

        if request.method == 'POST':
            complaint_title = request.POST['complaint_title']
            complaint_discription = request.POST['complaint_discription']

            cop = Complaint.objects.create(
                user_id=uid,
                complaint_title=complaint_title,
                complaint_discription=complaint_discription
            )

            context = {
                'uid': uid,
                'sid': sid,
                'msg': 'Complaint added successfully'
            }
            return render(request, 'societymemberapp/add-complaint.html', context)

        else:
            context = {
                'uid': uid,
                'sid': sid,
            }
            return render(request, 'societymemberapp/add-complaint.html', context)
    else:
        redirect('login')


def all_complaint(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        sid = Societymember.objects.get(user_id=uid)
        call = Complaint.objects.all()

        context = {
            'uid': uid,
            'sid': sid,
            'msg': 'Complaint added successfully',
            'call': call
        }
        return render(request, 'societymemberapp/all-complaint.html', context)

    else:
        redirect('login')


def add_events(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        sid = Societymember.objects.get(user_id=uid)

        if request.method == 'POST':
            events_title = request.POST['events_title']
            events_discription = request.POST['events_discription']

            cop = Event.objects.create(
                user_id=uid,
                events_title=events_title,
                events_discription=events_discription
            )

            context = {
                'uid': uid,
                'sid': sid,
                'msg': 'Events added successfully'
            }
            return render(request, 'societymemberapp/add-events.html', context)

        else:
            context = {
                'uid': uid,
                'sid': sid,
            }
            return render(request, 'societymemberapp/add-events.html', context)
    else:
        redirect('login')


def all_events(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        sid = Societymember.objects.get(user_id=uid)
        eall = Event.objects.all()

        context = {
            'uid': uid,
            'sid': sid,
            'eall': eall
        }
        return render(request, 'societymemberapp/all-events.html', context)

    else:
        redirect('login')


def member_maintenance(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        sid = Societymember.objects.get(user_id=uid)
        mall = Maintenance.objects.filter(member_id=sid)

        total = 0
        for s in mall:
            total += int(s.amount)

        context = {
            'uid': uid,
            'sid': sid,
            'mall': mall,
            'total': total
        }
        return render(request, 'societymemberapp/member-maintenance.html', context)

    else:
        redirect('login')


def maintenance_payment(request, pk):
    mid = Maintenance.objects.get(id=pk)
    print('amount', mid.amount)
    sid = Societymember.objects.get(id = mid.member_id.id)
    transaction = Transaction.objects.create(made_by=sid, amount=mid.amount)
    transaction.save()
    # merchant_key = settings.PAYTM_SECRET_KEY

    # params = (
    #     ('MID', settings.PAYTM_MERCHANT_ID),
    #     ('ORDER_ID', str(transaction.order_id)),
    #     ('CUST_ID', str(transaction.made_by.email)),
    #     ('TXN_AMOUNT', str(transaction.amount)),
    #     ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
    #     ('WEBSITE', settings.PAYTM_WEBSITE),
    #     # ('EMAIL', request.user.email),
    #     # ('MOBILE_N0', '9911223388'),
    #     ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
    #     ('CALLBACK_URL', 'http://127.0.0.1:8000/callback/'),
    #     # ('PAYMENT_MODE_ONLY', 'NO'),
    # )

    # paytm_params = dict(params)
    # checksum = generate_checksum(paytm_params, merchant_key)

    # transaction.checksum = checksum
    # transaction.save()

    # paytm_params['CHECKSUMHASH'] = checksum
    # print('SENT: ', checksum)
    # return render(request, 'payments/redirect.html', context=paytm_params)
    return render(request, 'societymemberapp/member-maintenance.html')




def Get_all_societymembers(request):
    if 'email' in request.session:
        soc_all = Societymember.objects.all()      
        soc_serialize = SerializeSocietymember(soc_all, many = True)
        json_data = JSONRenderer().render(soc_serialize.data)
        return HttpResponse(json_data, content_type='application/json')
    
    else:
        redirect('login')
