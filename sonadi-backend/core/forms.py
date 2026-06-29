from django import forms
from django.core.exceptions import ValidationError
import re

from .models import (
    ContactMessage,
    Testimonial,
    Volunteer,
    AdoptionRequest,
)

# ------------------------------------------------------------------
# 🔸 Custom Validators
# ------------------------------------------------------------------
def validate_name(value):
    if not re.fullmatch(r"[A-Za-z ]+", value):
        raise ValidationError("Enter a valid name. Only letters and spaces are allowed.")


def validate_phone(value):
    if not value.isdigit():
        raise ValidationError("Phone number must contain digits only.")
    if len(value) != 10:
        raise ValidationError("Enter a valid 10-digit mobile number.")


def validate_email(value):
    if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", value):
        raise ValidationError("Enter a valid email address.")


def validate_message(value):
    if not value.strip():
        raise ValidationError("Message field cannot be empty.")


# ------------------------------------------------------------------
# 🔸 Contact Form
# ------------------------------------------------------------------
class ContactForm(forms.ModelForm):
    name = forms.CharField(
        validators=[validate_name],
        error_messages={"required": "Please enter your name."},
    )
    phone = forms.CharField(
        validators=[validate_phone],
        error_messages={"required": "Please enter your mobile number."},
    )
    email = forms.EmailField(
        validators=[validate_email],
        error_messages={"required": "Please enter your email address."},
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"class": "input-field", "placeholder": " "}),
        validators=[validate_message],
        error_messages={"required": "Please enter a message."},
    )

    class Meta:
        model = ContactMessage
        fields = ["name", "email", "phone", "message"]
        widgets = {
            "name":  forms.TextInput(attrs={"class": "input-field", "placeholder": " "}),
            "email": forms.EmailInput(attrs={"class": "input-field", "placeholder": " "}),
            "phone": forms.TextInput(attrs={"class": "input-field", "placeholder": " "}),
        }


# ------------------------------------------------------------------
# 🔸 Testimonial Form (File Upload)
# ------------------------------------------------------------------
class TestimonialForm(forms.ModelForm):
    name = forms.CharField(
        validators=[validate_name],
        error_messages={"required": "Please enter your name."},
    )
    phone = forms.CharField(
        validators=[validate_phone],
        error_messages={"required": "Please enter your mobile number."},
    )
    email = forms.EmailField(
        validators=[validate_email],
        error_messages={"required": "Please enter your email address."},
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"class": "input-field", "placeholder": " "}),
        validators=[validate_message],
        error_messages={"required": "Please enter your testimonial message."},
    )

    class Meta:
        model = Testimonial
        fields = [
            "title",
            "message",
            "name",
            "animal_name",
            "email",
            "phone",
            "image",   # Use Django's ImageField
        ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add placeholder so floating labels work via :not(:placeholder-shown)
        for field_name in ["title", "name", "animal_name", "email", "phone"]:
            if field_name in self.fields:
                self.fields[field_name].widget.attrs.setdefault("placeholder", " ")
        # Style the image field properly
        self.fields["image"].widget.attrs.update({
            "class": "form-control",
            "accept": "image/*"
        })
        self.fields["image"].required = False


# ------------------------------------------------------------------
# 🔸 Volunteer Form
# ------------------------------------------------------------------
class VolunteerForm(forms.ModelForm):
    name = forms.CharField(
        validators=[validate_name],
        error_messages={"required": "Please enter your name."},
    )
    phone = forms.CharField(
        validators=[validate_phone],
        error_messages={"required": "Please enter your mobile number."},
    )
    email = forms.EmailField(
        validators=[validate_email],
        error_messages={"required": "Please enter your email address."},
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"class": "input-field", "placeholder": " "}),
        validators=[validate_message],
        error_messages={"required": "Please tell us why you want to volunteer."},
    )

    class Meta:
        model = Volunteer
        fields = ["name", "email", "phone", "message"]
        widgets = {
            "name":  forms.TextInput(attrs={"class": "input-field", "placeholder": " "}),
            "email": forms.EmailInput(attrs={"class": "input-field", "placeholder": " "}),
            "phone": forms.TextInput(attrs={"class": "input-field", "placeholder": " "}),
        }


# ------------------------------------------------------------------
# 🔸 Adoption Request Form
# ------------------------------------------------------------------
class AdoptionForm(forms.ModelForm):
    name = forms.CharField(
        validators=[validate_name],
        error_messages={"required": "Please enter your name."},
    )
    phone = forms.CharField(
        validators=[validate_phone],
        error_messages={"required": "Please enter your mobile number."},
    )
    email = forms.EmailField(
        validators=[validate_email],
        error_messages={"required": "Please enter your email address."},
    )
    reason = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "placeholder": " "}),
        validators=[validate_message],
        error_messages={"required": "Please explain why you want to adopt."},
    )

    class Meta:
        model = AdoptionRequest
        fields = [
            "name",
            "email",
            "phone",
            "reason",
            "animal_name",
            "animal_age",
            "animal_gender",
            "animal_breed",
            "animal_personality",
        ]
        widgets = {
            "name":         forms.TextInput(attrs={"placeholder": " "}),
            "email":        forms.EmailInput(attrs={"placeholder": " "}),
            "phone":        forms.TextInput(attrs={"placeholder": " "}),
            "animal_name":  forms.TextInput(attrs={"placeholder": " "}),
            "animal_age":   forms.TextInput(attrs={"placeholder": " "}),
            "animal_gender":forms.TextInput(attrs={"placeholder": " "}),
            "animal_breed": forms.TextInput(attrs={"placeholder": " "}),
            "animal_personality": forms.TextInput(attrs={"placeholder": " "}),
        }
