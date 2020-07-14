# settings.py
from dotenv import load_dotenv
load_dotenv()


# OR, the same with increased verbosity
#load_dotenv(verbose=True)


# OR, explicitly providing path to '.env'
# from pathlib import Path  # python3 only
# env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path)

import os
print(os.getenv('SENDGRID_API_KEY'))
print(os.getenv("ACCESS_TOKEN"))
print(os.getenv("SENDINBLUE_API_KEY"))