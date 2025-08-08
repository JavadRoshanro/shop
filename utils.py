# utils.py
from kavenegar import *
from django.contrib.auth.mixins import UserPassesTestMixin

def send_otp_code(phone_number, code):
    pass
    # try:
    #     api = KavenegarAPI('746B724372364A6F67394D7045723371585933756449576166756E6E54456550705964625A704C3479376F3D')
    #     params = {
    #         'sender': '2000660110',
    #         'receptor': phone_number,
    #         'message': f'کد تایید شما {code}'
    #     }
    #     response = api.sms_send(params)
    #     print(response)
    #     return response
    # except APIException as e:
    #     print(e)
    #     return None
    # except HTTPException as e:
    #     print(e)
    #     return None
        
        
class IsAdminUserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin
    
    
