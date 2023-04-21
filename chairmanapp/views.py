from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.core.mail import send_mail
import random
# Create your views here.

'''
models.objects.get(fieldname = htmlname) : fetch data from database (models)



uid = models.objects.get()
uid.fieldname = newvalue
uid.save()  --- for Update data

# To store data in model (similar like insert query)
uid = models.objects.create(fieldname = pythonname, fieldname = pythonname)


# fetch all data from model (without any condition)
models.objects.all()
'''


def index(request):
    if 'email' in request.session:

        uid = User.objects.get(email=request.session['email'])
        if uid.role == 'chairman':
            cid = Chairman.objects.get(user_id=uid)

            context = {
                'uid': uid,
                'cid': cid
            }
            return render(request, 'chairmanapp/index.html', context)

        else:
            sid = Societymember.objects.get(user_id=uid)
            uid = User.objects.get(email=request.session['email'])

            context = {
                'uid': uid,
                'sid': sid,

            }
            return render(request, 'societymemberapp/index.html', context)

    else:
        return redirect('login')


def login(request):
    if 'email' in request.session:
        return redirect('index')
    else:
        if request.method == 'POST':
            uemail = request.POST['email']
            upassword = request.POST['password']
            try:
                uid = User.objects.get(email=uemail)
                if uid.password == upassword:
                    if uid.role == 'chairman':
                        cid = Chairman.objects.get(user_id=uid)
                        request.session['email'] = uid.email
                        return redirect('index')
                    else:
                        # print('Society Member')
                        # return redirect('index')
                        sid = Societymember.objects.get(user_id=uid)
                        print(sid.firstname)
                        request.session['email'] = uid.email
                        return redirect('index')

                else:
                    context = {
                        'error': 'Invalid password'
                    }
                    return render(request, 'chairmanapp/login.html', context)

            except:
                context = {
                    'error': 'Invalid email'
                }
                return render(request, 'chairmanapp/login.html', context)
        else:
            print('Login page refresh')
            return render(request, 'chairmanapp/login.html')


def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return redirect('login')
    else:
        return redirect('login')


def chairman_profile(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(user_id=uid)
        if request.method == 'POST':
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            cid.firstname = firstname
            cid.lastname = lastname
            cid.save()

            context = {
                'uid': uid,
                'cid': cid
            }
            return render(request, 'chairmanapp/profile.html', context)
        else:
            context = {
                'uid': uid,
                'cid': cid
            }
            return render(request, 'chairmanapp/profile.html', context)

    else:
        return redirect('login')


def chairman_pass_change(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(user_id=uid)

        if request.method == 'POST':
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
                'cid': cid
            }
            return render(request, 'chairmanapp/profile.html', context)

        else:
            context = {
                'uid': uid,
                'cid': cid,
            }
            return render(request, "chairmanapp/profile.html", context)

    else:
        return redirect('login')


def add_societymember(request):

    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(user_id=uid)

        if request.method == 'POST':
            email = request.POST['email']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            block_no = request.POST['block_no']
            contact_no = request.POST['contact_no']
            gender = request.POST['gender']
            # occupation = request.POST['occupation']
            dob = request.POST['dob']
            # no_of_familymembers = request.POST['no_of_familymembers']
            # vehicle_details = request.POST['vehicle_details']
            # blood_group = request.POST['blood_group']
            # house_ownership = request.POST['house_ownership']
            city = request.POST['city']
            # l1 = ['1ghy3', 'f4bhj', 'pins4', 'lacv2', '12ca4']
            password = 123456

            uid = User.objects.create(
                email=email, role='societymember', password=password)
            # sid = Societymember(
            #     user_id = uid,
            #     firstname = firstname,
            #     lastname = lastname,
            #     contact_no = contact_no,
            #     block_no = block_no,
            #     gender=gender,
            #     no_of_familymembers = no_of_familymembers,
            #     dob=dob,
            #     occupation = occupation,
            #     vehicle_details = vehicle_details,
            #     blood_group = blood_group,
            #     house_ownership = house_ownership,
            #     city = city
            #     )
            # sid.save()

            sid = Societymember.objects.create(
                user_id=uid,
                firstname=firstname,
                lastname=lastname,
                block_no=block_no,
                contact_no=contact_no,
                gender=gender,
                dob=dob,
                city=city
            )

            if sid:
                send_mail('Digital Society passowrd', 'Your Password is : ' +
                          str(password), 'rajsangani0110@gmail.com', [email])
                msg = 'successfully society member created!!  Please check your gmail account for password'
                sall = Societymember.objects.all()

                context = {
                    'msg': msg,
                    'uid': uid,
                    'cid': cid,
                    'sall': sall
                }

                return render(request, 'chairmanapp/add-member.html', context)
            else:
                msg = 'Something went wrong!! Please Try again!'
                context = {
                    'msg': msg,
                    'uid': uid,
                    'cid': cid
                }

                return render(request, 'chairmanapp/add-member.html', context)

        else:
            context = {
                'uid': uid,
                'cid': cid
            }

            return render(request, 'chairmanapp/add-member.html', context)
    else:
        return redirect('login')


def all_societymember(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(user_id=uid)
        all_member = Societymember.objects.all()

        context = {
            'uid': uid,
            'cid': cid,
            'all_member': all_member,
        }
        return render(request, 'chairmanapp/all-member.html', context)

    else:
        return redirect('login')


def add_notice(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(user_id=uid)
        if request.method == 'POST':
            title = request.POST['title']
            discription = request.POST['discription']
            notice_Add = Notice.objects.create(
                user_id=uid, title=title, discription=discription)

            context = {
                'uid': uid,
                'cid': cid,

            }
            return render(request, 'chairmanapp/add-notice.html', context)
        else:
            context = {
                'uid': uid,
                'cid': cid,

            }
            return render(request, 'chairmanapp/add-notice.html', context)
    else:
        return redirect('login')


def notice_list(request):

    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(user_id=uid)

        nall = Notice.objects.all()
        context = {
            'uid': uid,
            'cid': cid,
            'nall': nall
        }
        return render(request, 'chairmanapp/notice-list.html', context)
    else:
        context = {
            'uid': uid,
            'cid': cid,
        }
        return render(request, 'chairmanapp/notice-list.html', context)


def notice_deatil_view(request, pk):

    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(user_id=uid)

        nid = Notice.objects.filter(id=pk)
        context = {
            'uid': uid,
            'cid': cid,
            'nall': nid
        }
        return render(request, 'chairmanapp/notice-detail-view.html', context)
    else:
        context = {
            'uid': uid,
            'cid': cid,
        }
        return render(request, 'chairmanapp/notice-detail-view.html', context)


def all_complaint_chairman_view(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(user_id=uid)
        call = Complaint.objects.all()
        sall = Societymember.objects.all()

        context = {
            'uid': uid,
            'cid': cid,
            'call': call,
            'sall': sall
        }
        return render(request, 'chairmanapp/all-complaint-chairman-view.html', context)

    else:
        redirect('login')


def all_events_chairman_view(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(user_id=uid)
        eall = Event.objects.all()
        sall = Societymember.objects.all()

        context = {
            'uid': uid,
            'cid': cid,
            'eall': eall,
            'sall': sall
        }
        return render(request, 'chairmanapp/all-events-chairman-view.html', context)

    else:
        redirect('login')


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        otp = random.randint(1111, 9999)
        try:
            uid = User.objects.get(email=email)
            uid.otp = otp
            uid.save()
            send_mail('Forgot Password', 'Your Forgot password OTP is' +
                      str(otp), 'rajsangani0110@gmail.com', [email])
            context = {
                'email': email
            }
            return render(request, 'chairmanapp/change-password-otp.html', context)
        except:
            context = {
                'error': 'Invalid email',
            }
            return render(request, 'chairmanapp/forgot-password.html', context)

    else:
        return render(request, 'chairmanapp/forgot-password.html')


def change_password_otp(request):
    if request.method == 'POST':
        email = request.POST['email']
        otp = int(request.POST['otp'])
        newpassword = request.POST['newpassword']
        confirmpassword = request.POST['confirmpassword']
        uid = User.objects.get(email=email)

        if uid.otp == otp:
            if newpassword == confirmpassword:
                uid.password = newpassword
                uid.save()
                context = {
                    'error': 'successfully changed password'
                }
                return render(request, 'chairmanapp/login.html', context)
            else:
                context = {
                    'error': 'Invalid password'
                }
                return render(request, 'chairmanapp/change-password-otp.html', context)

        else:
            context = {
                'error': 'Invalid OTP'
            }
            return render(request, 'chairmanapp/change-password-otp.html', context)
        

        
def add_maintenance(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(user_id=uid)

        if request.method == 'POST':
            title = request.POST['title']
            amount = request.POST['amount']
            duedate = request.POST['duedate']

            sall = Societymember.objects.all()

            for s in sall:
                sid = Societymember.objects.get(id = s.id)
                mid = Maintenance.objects.create(
                    user_id=uid,
                    member_id=sid,
                    title=title,
                    amount=amount,
                    duedate=duedate
                )  
                send_mail('Manintenance', 'Maintenance amount is' + str(amount), 'rajsangani0110@gmail.com', [sall.user_id.email])

            if mid:
                context = {
                    'uid': uid,
                    'msg': 'Successfully Added',
                    'cid': cid,

                }
                return render(request, 'chairmanapp/add-maintenance.html', context)
        else:

            context = {
                'uid': uid,
                'cid': cid,

            }
            return render(request, 'chairmanapp/add-maintenance.html', context)

    else:
        redirect('login')




def all_maintenance(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(user_id=uid)
        mall = Maintenance.objects.all()

        total = 0
        for s in mall:
            total += int(s.amount)
        
            
        context = {
            'uid': uid,
            'cid': cid,
            'mall' : mall,
            'total' : total
        }
        return render(request, 'chairmanapp/all-maintenance.html', context)

    else:
        redirect('login')

