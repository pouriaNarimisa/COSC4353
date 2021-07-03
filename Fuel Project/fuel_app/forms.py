from django import forms

""" default Django Forms """
class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label='',
        widget=forms.TextInput(attrs={'class': 'form-group form-control', 'placeholder':'Username'}),
        error_messages={'required': "Enter a valid username"})
    password = forms.CharField(max_length=256, label='',
        widget=forms.TextInput(attrs={'class': 'form-group form-control', 'placeholder':'Password'}),
        error_messages={'required': 'Enter a valid password'})

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=20, label='',
        widget=forms.TextInput(attrs={'class': 'form-group form-control', 'placeholder':'Username'}),
        error_messages={'required': 'Please enter a valid username'})
    password = forms.CharField(max_length=256, label='',
        widget=forms.TextInput(attrs={'class': 'form-group form-control', 'placeholder':'Password'}))
    confirm_password = forms.CharField(max_length=256, label='',
        widget=forms.TextInput(attrs={'class': 'form-group form-control', 'placeholder':'Confirm password'}))

class QuoteForm(forms.Form):
    gallons = forms.IntegerField(label='Gallons Requested', min_value=0, required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control col-2 mx-auto', 'placeholder': 0}),  
        error_messages={'required': "Please enter a valid number of gallons."})
    address = forms.CharField(max_length=100, label='Delivery Address', required=True,
        widget=forms.TextInput(attrs={'class': 'form-control col-3 mx-auto', 'placeholder':'Address'}),
        error_messages={'required': 'Please enter a valid address'})
    date = forms.DateField(label='Delivery Date', required=True, 
        widget=forms.DateInput(attrs={'class': 'form-control col-2 mx-auto', 'type': 'date'}), 
        error_messages={'required': "Please select a date."})
    price = forms.FloatField(label='Price Per Gallon:',
        widget=forms.NumberInput(attrs={'class': 'form-control col-2 mx-auto', 'readonly': 'readonly'}))
    total_price = forms.FloatField(label='Total Amount Due:',
        widget=forms.NumberInput(attrs={'class': 'form-control col-2 mx-auto', 'readonly': 'readonly'}))

class ProfileForm(forms.Form):
    name = forms.CharField(label="Full Name*", max_length=50, required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    address_1 = forms.CharField(label="Address 1*", max_length=100, required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    address_2 = forms.CharField(label="Address 2", max_length=100, required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(label="City*", max_length=100, required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.ChoiceField(label="State*", required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=[('al','AL'), ('ak','AK'),('as','AK'), ('ar','AR'),('az','AZ'),('ca','CA'),('co','CO'), ('ct','CT'),('dc','DC'), ('de','DE'),('fl','FL'),('ga','GA'),('gu','GU'), ('hi','HI'),('ia','IA'), ('id','ID'),('il','IL'),('in','IN'),('ks','KS'),('ky','KY'),('la','LA'),('ma','MA'),('me','ME'),('md','MD'),('mi','MI'),('mn','MN'),('ms','MS'),('mo','MO'),('mp','MP'),('mt','MT'),('nc','NC'),('nd','ND'),('ne','NE'),('nh','NH'),('nj','NJ'),('nm','NM'),('nv','NV'),('ny','Ny'),('oh','OH'),('ok','OK'),('or','OR'),('pa','PA'),('pr','PR'),('ri','RI'),('sc','SC'),('sd','SD'),('tn','TN'),('tx','TX'),('ut','UT'),('va','VA'),('vi','VI'),('vt','VT'),('wa','WA'),('wi','WI'),('wv','WV'),('wy','WY')])
    zipcode = forms.IntegerField(label="Zip code*", min_value=0,max_value=999999999,required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'}))