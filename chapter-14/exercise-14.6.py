#!/usr/bin/env python
# encoding: utf-8
"""
exercise-14.6.py

Created by Terry Bates on 2014-06-01.
Copyright (c) 2014 http://the-awesome-python-blog.posterous.com. All rights reserved.
"""

import sys
import os
import urllib
import re
from bs4 import BeautifulSoup


def get_city_list(city_tags):
    list_of_cities = []
    # Iterate over list of BS4 elements
    for tag in city_tags:
        # Convert the tag from a BS4 element to a string
        tag = str(tag)
        # Split on the "<strong>" tag, then on subsequest "<a>"
        tag = tag.split("<strong>")[1].split("<a")[0]
        # Strip off trailing ","
        tag = tag.replace(",", "")
        print "Our tag", tag
        print "tag type", type(tag)
        # Append to the City list
        list_of_cities.append(tag)
    return list_of_cities


def scraper(zip_code):
    # Create string for scraped html
    scraped_html = str()
    # Validate input string. This should five digits
    if re.search("^\\d{5}$", zip_code):
        url_to_scrape = 'http://www.uszip.com/zip/' + zip_code
        conn = urllib.urlopen(url_to_scrape) 
        # Read the entire set of output in connection via readlines()
        for line in conn:            
            scraped_html += line.strip()
          
        # After scraping the HTML and dumping into a variable, we use bs4
        # to parse and locate the sections of HTML that contain the population.
        soup = BeautifulSoup(scraped_html)
        # Locate the 'dl' tag containing data of interest
        dl_data_tag = soup.find("dl", class_ = "zip-stats zipstats-left")

        # Find all tags that contain city data, could be more than one.
        city_tags  = soup.find_all("dt", class_ = "l2 fw")

        # Locate tags that indicate the cities associated with the zip code
        city_list = get_city_list(city_tags)
        
        # Obtain population from soup object, cast into a string.
        pop_tag = str(soup.dl.dd)
        # Split on "span" then "<dd> to obtain raw population count"
        population = pop_tag.split("<span")[0].replace("<dd>","")
        
        return city_list, population
    else:
        print "%s is not a valid zip code." % zip_code


def main():
    # Prompt user for zip code
    zip_code = raw_input("Please enter zip code: ")
    town_names, population = scraper(zip_code)
    print "Towns"
    print "#" * 5
    for town in town_names:
        print town
    print
    print "Population"
    print "#" * len('Population')
    print population

if __name__ == '__main__':
    main()

