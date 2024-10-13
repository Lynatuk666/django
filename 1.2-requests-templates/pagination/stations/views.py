from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.conf import settings
import csv
bus_stations_list = []

with open(f"{settings.BUS_STATION_CSV}", "r",  newline='', encoding="UTF-8") as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        bus_stations_list.append(row)


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
      page_number = int(request.GET.get("page", 1))
    paginator = Paginator(bus_stations_list, 10)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
