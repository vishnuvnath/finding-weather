from django.shortcuts import render

# Create your views here.
def home (request):
    weather = None
    if 'city' in request.GET:
        city = request.GET.get('city')
        html_content = get_html_content(city)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        weather = dict()
        weather['region'] = soup.find('div',attrs={'id':'wob_loc'}).text
        weather['dayhour'] = soup.find('div', attrs={'id': 'wob_dts'}).text
        weather['status'] = soup.find('span', attrs={'id': 'wob_dc'}).text
        weather['temp'] = soup.find('span', attrs={'id': 'wob_dc'}).text
    return render(request,'home.html',{'weather': weather})
def get_html_content (city):
    import requests
    city = city.replace('','+')
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'https://www.google.com/search?q=weather+in+{city}').text
    return html_content