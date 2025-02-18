from django.core.mail import send_mail
def sendMail(username,email,password):
            send_mail(
    "Welcome to our platform",
     f"Hello {username},\n\nWelcome to our platform. your password is {password}\n We are happy to have you as a new user.\n\nBest regards,\n\nThe team",
     from_email= "ma_missoum@esi.dz",
     recipient_list=[email],
    fail_silently=False,
)
