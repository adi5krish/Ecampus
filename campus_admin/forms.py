from django import forms
from .models import Registers,FeeReceipt,Result


class RegistersForm(forms.ModelForm):
    class Meta:
        model = Registers
        fields = ['grade']

    def clean_grade(self):
        grade = self.cleaned_data['grade']
        length = len(grade)
        if length == 2:
            for i in range(0,length):
                if ord(grade[i])<65  or  ord(grade[i])>68:
                    raise forms.ValidationError("Invalid Data")
        else :
            raise forms.ValidationError("Invalid Data")


class FeeReceiptForm(forms.ModelForm):
    class Meta:
        model = FeeReceipt
        fields = ['receiptId','status']

    def clean_receiptId(self):
        receiptId = self.cleaned_data['receiptId']
        if FeeReceipt.objects.filter(receiptId = receiptId):
            raise forms.ValidationError("ReceiptId already exists")

'''
class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['SPI']

    def _clean_SPI(self):
        SPI = self.cleaned_data['SPI']
        if SPI <= 10 :
           length = len(SPI)
           if length <= 4 :
               for i in range(0, length):
                   if ord(SPI[i]) < 48 or ord(SPI[i]) > 57:
                       raise forms.ValidationError("Invalid Data")
        else:
            raise forms.ValidationError("Invalid Data")
'''