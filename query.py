import os
import pyopenstates

apikey = os.environ.get('API_KEY')

print(apikey)

pyopenstates.set_api_key(apikey)

metadata = pyopenstates.get_metadata('ny')

print(metadata)
