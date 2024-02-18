from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, CreateView, UpdateView, View
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from exam.models import *
from exam2.models import *
from exam3.models import *
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMessage
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from django.contrib import messages

from django.http import JsonResponse
from .forms import FeedbackForm


# Create your views here.


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def post(self, request, *args, **kwargs):
        log_form = LoginForm(data=request.POST)
        if log_form.is_valid():
            un = log_form.cleaned_data.get('username')
            ps = log_form.cleaned_data.get('password')
            user = authenticate(request, username=un, password=ps)
            if user:
                login(request, user)
                return redirect('h')
            else:
                return render(request, 'login.html', {"form": log_form, 'error': "Invalid credentials"})
        return render(request, 'login.html', {"form": log_form})


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = TestResult.objects.filter(user=self.request.user)
        return context


class RegView(CreateView):
    template_name = 'reg.html'
    model = CustUser
    form_class = RegForm
    success_url = reverse_lazy('log')

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class Profile(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #   id=kwargs.get('pk')
        context['data'] = CustUser.objects.get(id=self.request.user.id)
        return context


class ProfileUpdateView(UpdateView):
    template_name = "profileupdate.html"
    model = CustUser
    form_class = StudentFormProfile
    success_url = reverse_lazy('pro')


class ChangePasswordView(FormView):
    template_name = "changeps.html"
    form_class = ChangePasswordForm

    def post(self, request, *args, **kwargs):
        form_data = ChangePasswordForm(data=request.POST)
        if form_data.is_valid():
            current = form_data.cleaned_data.get("current_password")
            new = form_data.cleaned_data.get("new_password")
            confirm = form_data.cleaned_data.get("confirm_password")
            user = authenticate(request, username=request.user.username, password=current)
            if user:
                if new == confirm:
                    user.set_password(new)
                    user.save()
                    logout(request)
                    return redirect("log")
                else:
                    return redirect("cp")
            else:
                return redirect("cp")
        else:
            return render(request, "changepassword.html", {"form": form_data})


class LogOut(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("log")


class ScoreTable(TemplateView):
    template_name = 'score_table.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #   id=kwargs.get('pk')
        context['data'] = CustUser.objects.get(id=self.request.user.id)
        context['score'] = TestResult.objects.filter(user=self.request.user)
        return context


class ProgressCard(TemplateView):
    template_name = 'progress.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #   id=kwargs.get('pk')
        context['data'] = CustUser.objects.get(id=self.request.user.id)
        context['score'] = TestResult.objects.filter(user=self.request.user)

        return context


@login_required
def send_certificate_email(request):
    user = request.user

    # Render HTML content
    html_content = render_to_string('score_table.html', {'data': user, 'score': user.scores})

    # Attach the certificate to the email
    email = EmailMessage(
        'Your Certificate',
        'Congratulations! You have successfully generated your certificate.',
        'shibilmsk1@gmail.com',  # Replace with your email address
        [user.email],  # Send to the authenticated user's email address\
        html_message=html_content,
        fail_silently=False,
    )

    # Attach the certificate to the email

    # Send the email
    email.send()
    return HttpResponse('Email sent successfully.')

def htmlcertificate(request):
    return render(request, 'htmlcertificate.html')
def pythoncertificate(request):
    return render(request, 'pythoncertificate.html')
def phpcertificate(request):
    return render(request, 'phpcertificate.html')


@login_required
def generate_certificate(request):
    # Your existing code for generating the certificate
    user = request.user

    # Load the existing certificate PNG template
    template_path = 'C:/Users/HP/PycharmProjects/Personalized E-Learning4/Personalized E-Learning/E_Learning/accounts/static/images/htmlcertificate.png'  # Replace with the path to your font file

    # Create a response object to store the PNG
    response = HttpResponse(content_type='image/png')
    response['Content-Disposition'] = f'filename={user.username}_certificate.png'

    # Open the existing certificate image
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)

    # Specify the font and size for the text overlay
    font_size = 80
    font_path = 'C:/Users/HP/PycharmProjects/Personalized E-Learning4/Personalized E-Learning/E_Learning/accounts/static/images/Roboto-Medium.ttf'  # Replace with the path to your font file
    font = ImageFont.truetype(font_path, font_size)

    # Overlay the user's name onto the certificate
    name_position = (700, 680)  # Adjust the position as needed(horizontal,vertical)
    uppercase_name = user.get_full_name().upper()
    draw.text(name_position, uppercase_name, fill="black", font=font)

    # You can add more overlay text or images as needed
    #     # Save the modified image to BytesIO
    img_byte_array = BytesIO()
    img.save(img_byte_array, format='PNG')
    # Save the modified image to the response
    img.save(response, format='PNG')
    return response


@login_required
def send_certificate_email(request):
    # Your existing code for sending the certificate via email
    user = request.user

    # Load the existing certificate PNG template
    template_path = 'C:/Users/HP/PycharmProjects/Personalized E-Learning4/Personalized E-Learning/E_Learning/accounts/static/images/htmlcertificate.png'  # Replace with the path to your font file

    # Open the existing certificate image using Pillow
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)

    # Specify the font and size for the text overlay
    font_size = 80
    font_path = 'C:/Users/HP/PycharmProjects/Personalized E-Learning4/Personalized E-Learning/E_Learning/accounts/static/images/Roboto-Medium.ttf'  # Replace with the path to your font file
    font = ImageFont.truetype(font_path, font_size)

    # Overlay the user's name onto the certificate
    name_position = (700, 680)  # Adjust the position as needed
    uppercase_name = user.get_full_name().upper()
    draw.text(name_position, uppercase_name, fill="black", font=font)

    # You can add more overlay text or images as needed

    # Save the modified image to BytesIO
    img_byte_array = BytesIO()
    img.save(img_byte_array, format='PNG')

    # Attach the certificate to the email
    email = EmailMessage(
                'Your Certificate',
                'Congratulations! You have successfully generated your certificate.',
                'shibilmsk1@gmail.com',  # Replace with your email address
                [user.email],  # Send to the authenticated user's email address
            )
    # Attach the certificate to the email
    email.attach('certificate.png', img_byte_array.getvalue(), 'image/png')
    # Add a success message

    # Send the email
    email.send()

    # Return a response indicating the certificate has been sent
    return HttpResponse('Certificate sent to your email.')
@login_required
def download_certificate(request):
    # Your existing code for generating the certificate
    user = request.user

    # Load the existing certificate PNG template
    template_path = 'C:/Users/HP/PycharmProjects/Personalized E-Learning4/Personalized E-Learning/E_Learning/accounts/static/images/htmlcertificate.png'  # Replace with the path to your font file


    # Create a response object to store the PNG
    response = HttpResponse(content_type='image/png')
    response['Content-Disposition'] = f'filename={request.user.username}_certificate.png'
    # Open the existing certificate image
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)

    # Specify the font and size for the text overlay
    font_size = 80
    font_path = 'C:/Users/HP/PycharmProjects/Personalized E-Learning4/Personalized E-Learning/E_Learning/accounts/static/images/Roboto-Medium.ttf'  # Replace with the path to your font file
    font = ImageFont.truetype(font_path, font_size)

    # Overlay the user's name onto the certificate
    name_position = (700, 680)  # Adjust the position as needed(horizontal,vertical)
    uppercase_name = user.get_full_name().upper()
    draw.text(name_position, uppercase_name, fill="black", font=font)

    # Save the modified image to BytesIO

    messages.success(request, 'Certificate downloaded successfully.')
    # Save the modified image to the response
    img.save(response, format='PNG')
    # Add a success message

    return response
#for python section
@login_required
def generate_pythoncertificate(request):
    # Your existing code for generating the certificate
    user = request.user

    # Load the existing certificate PNG template
    template_path = 'C:/Users/HP/PycharmProjects/Personalized E-Learning4/Personalized E-Learning/E_Learning/accounts/static/images/pythoncertificate.png'  # Replace with the path to your font file

    # Create a response object to store the PNG
    response = HttpResponse(content_type='image/png')
    response['Content-Disposition'] = f'filename={user.username}_certificate.png'

    # Open the existing certificate image
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)

    # Specify the font and size for the text overlay
    font_size = 80
    font_path = 'C:/Users/HP/PycharmProjects/Personalized E-Learning4/Personalized E-Learning/E_Learning/accounts/static/images/Roboto-Medium.ttf'  # Replace with the path to your font file
    font = ImageFont.truetype(font_path, font_size)

    # Overlay the user's name onto the certificate
    name_position = (700, 680)  # Adjust the position as needed(horizontal,vertical)
    uppercase_name = user.get_full_name().upper()
    draw.text(name_position, uppercase_name, fill="black", font=font)

    # You can add more overlay text or images as needed
    #     # Save the modified image to BytesIO
    img_byte_array = BytesIO()
    img.save(img_byte_array, format='PNG')
    # Save the modified image to the response
    img.save(response, format='PNG')
    return response


@login_required
def send_pythoncertificate_email(request):
    # Your existing code for sending the certificate via email
    user = request.user

    # Load the existing certificate PNG template
    template_path = 'C:/Users/HP/PycharmProjects/Personalized E-Learning4/Personalized E-Learning/E_Learning/accounts/static/images/pythoncertificate.png'  # Replace with the path to your font file

    # Open the existing certificate image using Pillow
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)

    # Specify the font and size for the text overlay
    font_size = 80
    font_path = 'C:/Users/HP/PycharmProjects/Personalized E-Learning4/Personalized E-Learning/E_Learning/accounts/static/images/Roboto-Medium.ttf'  # Replace with the path to your font file
    font = ImageFont.truetype(font_path, font_size)

    # Overlay the user's name onto the certificate
    name_position = (700, 680)  # Adjust the position as needed
    uppercase_name = user.get_full_name().upper()
    draw.text(name_position, uppercase_name, fill="black", font=font)

    # You can add more overlay text or images as needed

    # Save the modified image to BytesIO
    img_byte_array = BytesIO()
    img.save(img_byte_array, format='PNG')

    # Attach the certificate to the email
    email = EmailMessage(
                'Your Certificate',
                'Congratulations! You have successfully generated your certificate.',
                'shibilmsk1@gmail.com',  # Replace with your email address
                [user.email],  # Send to the authenticated user's email address
            )
    # Attach the certificate to the email
    email.attach('certificate.png', img_byte_array.getvalue(), 'image/png')
    # Add a success message

    # Send the email
    email.send()

    # Return a response indicating the certificate has been sent
    return HttpResponse('Certificate sent to your email.')
@login_required
def download_pythoncertificate(request):
    # Your existing code for generating the certificate
    user = request.user

    # Load the existing certificate PNG template
    template_path = 'C:/Users/HP/PycharmProjects/Personalized E-Learning4/Personalized E-Learning/E_Learning/accounts/static/images/pythoncertificate.png'  # Replace with the path to your font file


    # Create a response object to store the PNG
    response = HttpResponse(content_type='image/png')
    response['Content-Disposition'] = f'filename={request.user.username}_certificate.png'
    # Open the existing certificate image
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)

    # Specify the font and size for the text overlay
    font_size = 80
    font_path = 'C:/Users/HP/PycharmProjects/Personalized E-Learning4/Personalized E-Learning/E_Learning/accounts/static/images/Roboto-Medium.ttf'  # Replace with the path to your font file
    font = ImageFont.truetype(font_path, font_size)

    # Overlay the user's name onto the certificate
    name_position = (700, 680)  # Adjust the position as needed(horizontal,vertical)
    uppercase_name = user.get_full_name().upper()
    draw.text(name_position, uppercase_name, fill="black", font=font)

    # Save the modified image to BytesIO

    messages.success(request, 'Certificate downloaded successfully.')
    # Save the modified image to the response
    img.save(response, format='PNG')
    # Add a success message

    return response

#for php section
@login_required
def generate_phpcertificate(request):
    # Your existing code for generating the certificate
    user = request.user

    # Load the existing certificate PNG template
    template_path = 'C:/Users/HP/PycharmProjects/Personalized E-Learning4/Personalized E-Learning/E_Learning/accounts/static/images/phpcertificate.png'  # Replace with the path to your font file

    # Create a response object to store the PNG
    response = HttpResponse(content_type='image/png')
    response['Content-Disposition'] = f'filename={user.username}_certificate.png'

    # Open the existing certificate image
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)

    # Specify the font and size for the text overlay
    font_size = 80
    font_path = 'C:/Users/HP/PycharmProjects/Personalized E-Learning4/Personalized E-Learning/E_Learning/accounts/static/images/Roboto-Medium.ttf'  # Replace with the path to your font file
    font = ImageFont.truetype(font_path, font_size)

    # Overlay the user's name onto the certificate
    name_position = (700, 680)  # Adjust the position as needed(horizontal,vertical)
    uppercase_name = user.get_full_name().upper()
    draw.text(name_position, uppercase_name, fill="black", font=font)

    # You can add more overlay text or images as needed
    #     # Save the modified image to BytesIO
    img_byte_array = BytesIO()
    img.save(img_byte_array, format='PNG')
    # Save the modified image to the response
    img.save(response, format='PNG')
    return response


@login_required
def send_phpcertificate_email(request):
    # Your existing code for sending the certificate via email
    user = request.user

    # Load the existing certificate PNG template
    template_path = 'C:/Users/HP/PycharmProjects/Personalized E-Learning4/Personalized E-Learning/E_Learning/accounts/static/images/phpcertificate.png'  # Replace with the path to your font file

    # Open the existing certificate image using Pillow
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)

    # Specify the font and size for the text overlay
    font_size = 80
    font_path = 'C:/Users/HP/PycharmProjects/Personalized E-Learning4/Personalized E-Learning/E_Learning/accounts/static/images/Roboto-Medium.ttf'  # Replace with the path to your font file
    font = ImageFont.truetype(font_path, font_size)

    # Overlay the user's name onto the certificate
    name_position = (700, 680)  # Adjust the position as needed
    uppercase_name = user.get_full_name().upper()
    draw.text(name_position, uppercase_name, fill="black", font=font)

    # You can add more overlay text or images as needed

    # Save the modified image to BytesIO
    img_byte_array = BytesIO()
    img.save(img_byte_array, format='PNG')

    # Attach the certificate to the email
    email = EmailMessage(
                'Your Certificate',
                'Congratulations! You have successfully generated your certificate.',
                'shibilmsk1@gmail.com',  # Replace with your email address
                [user.email],  # Send to the authenticated user's email address
            )
    # Attach the certificate to the email
    email.attach('certificate.png', img_byte_array.getvalue(), 'image/png')
    # Add a success message

    # Send the email
    email.send()

    # Return a response indicating the certificate has been sent
    return HttpResponse('Certificate sent to your email.')
@login_required
def download_phpcertificate(request):
    # Your existing code for generating the certificate
    user = request.user

    # Load the existing certificate PNG template
    template_path = 'C:/Users/HP/PycharmProjects/Personalized E-Learning4/Personalized E-Learning/E_Learning/accounts/static/images/phpcertificate.png'  # Replace with the path to your font file


    # Create a response object to store the PNG
    response = HttpResponse(content_type='image/png')
    response['Content-Disposition'] = f'filename={request.user.username}_certificate.png'
    # Open the existing certificate image
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)

    # Specify the font and size for the text overlay
    font_size = 80
    font_path = 'C:/Users/HP/PycharmProjects/Personalized E-Learning4/Personalized E-Learning/E_Learning/accounts/static/images/Roboto-Medium.ttf'  # Replace with the path to your font file
    font = ImageFont.truetype(font_path, font_size)

    # Overlay the user's name onto the certificate
    name_position = (700, 680)  # Adjust the position as needed(horizontal,vertical)
    uppercase_name = user.get_full_name().upper()
    draw.text(name_position, uppercase_name, fill="black", font=font)

    # Save the modified image to BytesIO

    messages.success(request, 'Certificate downloaded successfully.')
    # Save the modified image to the response
    img.save(response, format='PNG')
    # Add a success message

    return response



# views.py
def feedback(request):
    feedback_data = Feedback.objects.all()
    return render(request, 'thankyou.html', {'feedback_data': feedback_data})

# views.py


class submit_feedback(CreateView):
    template_name="feedback.html"
    model=Feedback
    form_class=FeedbackForm
    success_url=reverse_lazy("feedback")
    

# def submit_feedback(request):
#     if request.method == 'POST':
#         form = FeedbackForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request,"feedback.html",{"form":form})
#         else:
#             return HttpResponse({'message': 'Please fill in all fields correctly.'}, status=400)
#     else:
#         # If request method is not POST, return a method not allowed response
#         return HttpResponse({'error': 'Method not allowed.'}, status=405)


class Feedbacks(TemplateView):
    template_name="feedback.html"


def Contact(request):
    return render(request, "contactus.html")








