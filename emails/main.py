def send_mail(request):   

    # ---------------------------
    # Send Transactional Email\
    # ---------------------------
    from __future__ import print_function
    import time
    import sib_api_v3_sdk
    from sib_api_v3_sdk.rest import ApiException
    from pprint import pprint

    # A ccess environment variables    
    from dotenv import load_dotenv
    load_dotenv()
    import os
    api_key = os.getenv("SENDINBLUE_API_KEY") # os.environ.get("SENDINBLUE_API_KEY") 

    # Configure API key authorization: api-key
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = api_key

    # Uncomment below lines to configure API key authorization using: partner-key
    # configuration = sib_api_v3_sdk.Configuration()
    # configuration.api_key['partner-key'] = 'YOUR_API_KEY'

    # create an instance of the API class
    api_instance = sib_api_v3_sdk.SMTPApi(sib_api_v3_sdk.ApiClient(configuration))
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=[{"email":"johndoe@gmail.com","name":"John Doe"}], template_id=2, params={"name": "John", "surname": "Doe"}, headers={"X-Mailin-custom": "custom_header_1:custom_value_1|custom_header_2:custom_value_2|custom_header_3:custom_value_3", "charset": "iso-8859-1"}) # SendSmtpEmail | Values to send a transactional email

    try:
        # Send a transactional email
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
    except ApiException as e:
        print(f'Exception when calling SMTPApi->send_transac_email: {e}\n')
