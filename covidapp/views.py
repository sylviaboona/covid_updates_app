from django.shortcuts import render
import requests
import json

# Thorough check the end-point url from the API provider.
# from dotenv import load_dotenv
# import os

# load_dotenv()  # take environmnet vaiables fomr .env

# Environment variables

# https://rapidapi.com/api-sports/api/covid-193/

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': '4489f5ed8amshefe5bd8f55e643fp1fb7e9jsn5c49884fc091',
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()


# Create your views here.
def covid_stats_view(request):
    mylist = []
    noofresults = int(response['results'])

    for x in range(0, noofresults):

        mylist.append(response['response'][x]['country'])

    if request.method == 'POST':
        selectedcountry = request.POST['selectedcountry']

        # Getting  cases for each country
        for x in range(0, noofresults):
            if selectedcountry == response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = int(total) - int(active)-int(recovered)

        context = {'selectedcountry': selectedcountry, 'mylist': mylist, 'new': new, 'active': active,
                   'critical': critical, 'recovered': recovered, 'deaths': deaths, 'total': total}
        return render(request, 'covidapp/covid_stats.html', context)

    noofresults = int(response['results'])
    mylist.append(response['response'][x]['country'])
    context = {'mylist': mylist}
    return render(request, 'covidapp/covid_stats.html', context)
