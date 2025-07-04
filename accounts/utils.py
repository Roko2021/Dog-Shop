import random
from django.core.mail import EmailMessage
from .models import User,OneTimePassword
from django.conf import settings

def generateOTP():
    otp=''
    for i in range(6):
        otp +=str(random.randint(1,9))
    return otp

def send_code_to_user(email):
    subject='One time passcode for Email Verification'
    otp_code=generateOTP()
    user = User.objects.get(email=email)
    current_site="my_Auth.com"
    email_body=f"Hi {user.first_name} thanks for signing up on {current_site} and this is otp:{otp_code}"
    from_email=settings.DEFAULT_FROM_EMAIL
    OneTimePassword.objects.create(user=user,code=otp_code)
    d_email=EmailMessage(subject=subject,body=email_body,from_email=from_email,to=[email])
    # d_email.send(fail_silently=True)
    try:
        d_email.send(fail_silently=False)  # جعل fail_silently=False لتتمكن من اكتشاف الأخطاء
    except Exception as e:
        # يمكنك هنا إضافة تسجيل للأخطاء أو إخطار
        print(f"Error sending email: {e}")

def send_normal_email(data):
    email=EmailMessage(
        subject=data['email_subject'],
        body=data['email_body'],
        from_email=settings.EMAIL_HOST_USER,
        to=[data['to_email']]
    )

