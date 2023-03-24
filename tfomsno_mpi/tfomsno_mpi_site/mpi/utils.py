from pathlib import Path

import requests
from lxml import etree

from django.template import Context, Template
from django.conf import settings


class SOAPGetPersonData(object):
    template_dir = settings.BASE_DIR / "mpi/templates/soap"
    mixin_template_soap = ""
    mixin_cleaned_data = {}

    def mixin_get_data(self):
        template_file = Path(self.template_dir, self.mixin_template_soap)
        with open(template_file) as f:
            template = Template(f.read().strip().replace("\n", ""))
        context = Context(self.mixin_cleaned_data)
        return template.render(context)
    
    def mixin_send_request(self):
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzZXNzaW9uLWlkIjoiMWMxYjYwMGUtNmY5OC00NGJhLWI1OWUtODRjYmY4ZjhkZGY4In0._l4OLEQfVwEf_tfSU8ohXkbUe5ZIkg-5eqSHDxR6_jY"
        url = "http://10.255.87.30/api/t-foms/integration/ws/wsdl/mpiPersonInfoServiceWs.wsdl"
        headers = {
            "Content-Type": "text/xml; charset=utf-8",
            "X-Auth-Token": token,
        }
        body = str(self.mixin_get_data()).encode("utf-8")
        print(body)
        response = requests.post(url, data=body, headers=headers)
        return response.text
    
    def mixin_parse_response(self):
        root = etree.Element("body")
        tags = [tag for tag in root]
        return tags