#!/usr/bin/python
# -*-coding:Utf-8 -*


import urllib2
import time
import json


def get_ctf() :
  URL_API = "https://ctftime.org/api/v1/"

  limit_nb_event = 100
  start_timestamp = int(time.time())
  end_timestamp = start_timestamp + 60*60*24*7*2 # 2 weeks
  URI_EVENTS = "events/?limit=" + str(limit_nb_event)  + "&start=" + str(start_timestamp) + "&finish=" + str(end_timestamp)

  URL_EVENTS = URL_API + URI_EVENTS
  events_response = urllib2.urlopen(URL_EVENTS).read()
  results_json = json.loads(events_response)
  i = 0
  len_events = len(results_json)
  events = []

  while i < len_events :

    organizer_ident = results_json[i]["organizers"][0]["id"]
    organizer_name = results_json[i]["organizers"][0]["name"]
    on_site = results_json[i]["onsite"]
    finish = results_json[i]["finish"]
    description = results_json[i]["description"]
    title = results_json[i]["title"]
    weight = results_json[i]["weight"]
    url = results_json[i]["url"]
    ctfformat = results_json[i]["format"]
    start = results_json[i]["start"]
    participants = results_json[i]["participants"]
    ident = results_json[i]["id"]
    duration_hours = results_json[i]["duration"]["hours"]
    duration_days = results_json[i]["duration"]["days"]
    ctftime_url = results_json[i]["ctftime_url"]
    ctf_ident = results_json[i]["ctf_id"]
    location = results_json[i]["location"]

    event =  "CTF : " + title + " , " + str(start) + " - " + str(duration_days) + " d " + str(duration_hours) + " h , " + ctfformat + " , " + url
    events.append(event)


    i += 1

  return events
