from django import forms
from .models import Wallet

class WalletForm(forms.ModelForm):
    """
    WalletForm class is used for creating Wallet form
    """

    def __init__(self, *args, **kwargs):
        """
        __init__ method is used for Initialization of WalletForm class
        """

        try:
            super(WalletForm, self).__init__(*args, **kwargs)
            self.fields['user'].empty_label = None

            ## pop method is used for removing the user field from fomr
            self.fields.pop('user')
        except Exception as e:
            # logger.error('The error in WalletForm - __init__ method is :'+str(e))
            print(e)

    class Meta():
        model = Wallet
        fields = ('user','balance')