import requests


class Transmission:

  session_id_header_name = 'X-Transmission-Session-Id'

  def __init__(self, host='diskstation.local', port = 9091, auth = ('admin', 'admin')):
    self.url = 'http://{host}:{port}/transmission/rpc'.format(host = host, port = port)
    self.auth = auth
    self. session_id = None

  def get_custom_headers(self):
    return {} if self.session_id is None else {self.session_id_header_name: self.session_id}

  def get(self):

    custom_headers = self.get_custom_headers()
    response = requests.get(self.url, auth = self.auth, headers = custom_headers)
    if response.status_code == 409 and self.session_id is None:
      self.session_id = response.headers[self.session_id_header_name]
      return self.get()
    #elif response.status_code != 200:

    return response

t = Transmission()
print(t.get().__dict__)

