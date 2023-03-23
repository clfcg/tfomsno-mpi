from pathlib import Path

from django.template import Context, Template


class SendPersonData(object):
    mixin_data = {}

    def get_mixin_data(self, mixin_dict: dict):
        template = Template("""
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:mpip="http://ffoms.ru/types/mpiPersonInfoSchema" xmlns:com="http://ffoms.ru/types/commonTypes">
   <soapenv:Body>
      <mpip:getPersonDataRequest>
         <com:externalRequestId>1213313</com:externalRequestId>
         <mpip:personDataSearchParams>
            <mpip:personSearchInfo>
               <mpip:pcy>
                  <com:pcyType>{{ pcyType }}</com:pcyType>
                  <com:enp>{{ enp }}</com:enp>
                  <com:pcySer>{{ pcySer }}</com:pcySer>
                  <com:pcyNum>{{ pcyNum }}</com:pcyNum>
                  <com:tmpcertNum>{{ tmpcertNum }}</com:tmpcertNum>
               </mpip:pcy>
               <mpip:dudl>
                  <com:dudlSer>{{ dudlSer }}</com:dudlSer>
                  <com:dudlNum>{{ dudlNum }}</com:dudlNum>
                  <com:dudlType>{{ dudlType }}</com:dudlType>
               </mpip:dudl>
               <mpip:snilsDr>
                  <mpip:snils>{{ snils }}</mpip:snils>
                  <mpip:birthDay>{{ birthDay }}</mpip:birthDay>
               </mpip:snilsDr>
            </mpip:personSearchInfo>
            <mpip:surname>{{ surname }}</mpip:surname>
            <mpip:firstName>{{ firstname }}</mpip:firstName>
            <mpip:patronymic>{{ patronymic }}</mpip:patronymic>
            <mpip:show>{{ show }}</mpip:show>
            <mpip:dt>{{ dt }}</mpip:dt>
         </mpip:personDataSearchParams>
      </mpip:getPersonDataRequest>
   </soapenv:Body>
</soapenv:Envelope>
        """)
        context = Context(mixin_dict)
        return template.render(context)