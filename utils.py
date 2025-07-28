# utils.py
from kavenegar import *

def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('746B724372364A6F67394D7045723371585933756449576166756E6E54456550705964625A704C3479376F3D')
        params = {
            'sender': '2000660110',
            'receptor': phone_number,
            'message': f'کد تایید شما {code}'
        }
        response = api.sms_send(params)
        print(response)
        return response
    except APIException as e:
        print(e)
        return None
    except HTTPException as e:
        print(e)
        return None
        
        
    
    
