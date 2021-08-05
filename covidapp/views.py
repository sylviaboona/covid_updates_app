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
    country_list = []
    total_no_of_results = int(response['results'])

    for x in range(0, total_no_of_results):

        country_list.append(response['response'][x]['country'])

    if request.method == 'POST':
        selected_country = request.POST['selectedcountry']

        # Getting  cases for each country
        for x in range(0, total_no_of_results):
            if selected_country == response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = int(total) - int(active)-int(recovered)

        context = {'selectedcountry': selected_country, 'country_list': country_list, 'new': new, 'active': active,
                   'critical': critical, 'recovered': recovered, 'deaths': deaths, 'total': total}
        return render(request, 'covidapp/covid_stats.html', context)

    total_no_of_results = int(response['results'])
    country_list.append(response['response'][x]['country'])
    context = {'country_list': country_list}
    return render(request, 'covidapp/covid_stats.html', context)
