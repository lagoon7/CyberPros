#!/usr/bin/python
# -*- coding: utf-8 -*-
# Module & Framework Declarations
import pygeoip

# Object instance, opens database file
gi = pygeoip.GeoIP('./GeoLiteCity.dat')

#Custom Function
def printRecord(tgt):
    rec = gi.record_by_name(tgt)
    city = rec['city']
    #region = rec['region_name']
    country = rec['country_name']
    long = rec['longitude']
    lat = rec['latitude']
    print '[*] Target: ' + tgt + ' Geo-located. '
    #print '[+] '+str(city)+', '+str(region)+', '+str(country)
    print '[+] '+str(city)+', '+str(country)
    print '[+] Latitude: '+str(lat)+ ', Longitude: '+ str(long)

# Variable
tgt = '173.255.226.98'
# function call with argument
printRecord(tgt)

