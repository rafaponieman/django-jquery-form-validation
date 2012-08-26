from django.template.defaulttags import register
from django import forms
from django.core import validators
from django.utils.encoding import force_unicode
from json import JSONEncoder

@register.simple_tag
def validation_rules(form):
    """
    This will render a Django form into a jquery validate ruleset.

    Usage::

        {% validation_rules form %}

    """
    if not isinstance(form, forms.BaseForm):
        raise TypeError(_("Expected Django Form instance"))
    
    rules = {}
    
    for field_name in form.fields:
        field_rules = {}
        
        # Required
        if hasattr(form.fields[field_name], 'required'):
            if form.fields[field_name].required == True:
                field_rules['required'] = True
        
        if(isinstance(form.fields[field_name], forms.TimeField)):
            field_rules['time'] = True
        
        if(isinstance(form.fields[field_name], forms.DateField)):
            field_rules['date'] = True
        
        for validator in form.fields[field_name].validators:
            # Min length
            if(isinstance(validator, validators.MinLengthValidator)):
                if form.fields[field_name].min_length != None:
                    field_rules['minlength'] = form.fields[field_name].min_length

            # Max length
            if(isinstance(validator, validators.MaxLengthValidator)):
                if form.fields[field_name].max_length != None:
                    field_rules['maxlength'] = form.fields[field_name].max_length
            
            # Regular expression
            # Email fields have a regex validator, in this case, we want to use the built-in
            # regex validator in jquery validate, and not Django's regex
            if(isinstance(validator, validators.RegexValidator) and not isinstance(form.fields[field_name], forms.EmailField)):
                field_rules['regexp'] = validator.regex.pattern
            
            # Email
            if(isinstance(validator, validators.EmailValidator)):
                field_rules['email'] = True
        
        rules[field_name] = field_rules
    
    return JSONEncoder().encode(rules)

@register.simple_tag
def validation_messages(form):
    """
    This will render the validation messages .

    Usage::

        {% validation_messages form %}

    """
    if not isinstance(form, forms.BaseForm):
        raise TypeError(_("Expected Django Form instance"))
    
    messages = {}
    
    for field_name in form.fields:
        field_messages = {}
        
        # Required
        if hasattr(form.fields[field_name], 'required'):
            if form.fields[field_name].required == True:
                field_messages['required'] = force_unicode(form.fields[field_name].error_messages.get('required'))
        
        if(isinstance(form.fields[field_name], forms.TimeField)):
            field_messages['time'] = force_unicode(form.fields[field_name].error_messages.get('invalid'))
        
        if(isinstance(form.fields[field_name], forms.DateField)):
            field_messages['date'] = force_unicode(form.fields[field_name].error_messages.get('invalid'))
        
        for validator in form.fields[field_name].validators:
            # Min length
            if(isinstance(validator, validators.MinLengthValidator)):
                if form.fields[field_name].min_length != None:
                    field_messages['min_length'] = force_unicode(form.fields[field_name].error_messages.get('invalid'))
            
            # Max length
            if(isinstance(validator, validators.MaxLengthValidator)):
                if form.fields[field_name].max_length != None:
                    field_messages['max_length'] = force_unicode(form.fields[field_name].error_messages.get('invalid'))
            
            # Regular expression
            if(isinstance(validator, validators.RegexValidator) and not isinstance(form.fields[field_name], forms.EmailField)):
                field_messages['regexp'] = force_unicode(form.fields[field_name].error_messages.get('invalid'))
            
            # Email
            if(isinstance(validator, validators.EmailValidator)):
                field_messages['email'] = force_unicode(form.fields[field_name].error_messages.get('invalid'))

        messages[field_name] = field_messages
    
    return JSONEncoder().encode(messages)