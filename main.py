import requests

url = 'https://formular.berlin.de/xima-forms-29/get/14963116144270000'

session_requests = requests.Session()
print(session_requests.cookies.get_dict())

r = session_requests.get(url)
print(session_requests.cookies.get_dict())

# fetch html to get the url 
# <input type="button" style="background-image: url(&quot;/xima-forms-29/resource/61539edd-c03d-4011-ad93-4cb542fb462a/images/speichern.gif&quot;); border-width: 1px;" class="R28 CBR28" tabindex="0" onclick="handleEvent(this, 2);" id="btnTerminBuchen" name="btnTerminBuchen" value="Termin buchen" hoverimg="URL('/xima-forms-29/resource/61539edd-c03d-4011-ad93-4cb542fb462a/images/speichern_a.gif')">

# redirect to 
# https://formular.berlin.de/xima-forms-29/nextpage/ + url 