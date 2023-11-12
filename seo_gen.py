import xml.etree.ElementTree as ET
from xml.dom import minidom
import pandas as pd
import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

def create_sitemap(urls):
    # Create the root element
    root = ET.Element("urlset")
    root.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")

    # Create elements for each URL
    for url_data in urls:
        url_element = ET.SubElement(root, "url")
        
        loc_element = ET.SubElement(url_element, "loc")
        loc_element.text = url_data
        
        lastmod_element = ET.SubElement(url_element, "lastmod")
        lastmod_element.text = "2023-11-12"
        
        changefreq_element = ET.SubElement(url_element, "changefreq")
        changefreq_element.text = "weekly"

    # Create a string representation of the XML
    xml_str = ET.tostring(root, encoding="utf-8").decode("utf-8")

    # Use minidom to prettify the XML
    xml_str = minidom.parseString(xml_str).toprettyxml(indent="  ")

    # Write the XML to a file
    with open("sitemap.xml", "w", encoding="utf-8") as file:
        file.write(xml_str)


if __name__ == "__main__":
    # Replace this list with your actual URLs
    example_urls = [
    "https://hptuexam.web3o.cloud/",
    "https://hptuexam.web3o.cloud/allresultranklist.html",
    "https://hptuexam.web3o.cloud/pyq/",
    "https://hptuexam.web3o.cloud/result/",
    "https://hptuexam.web3o.cloud/rank/",
    "https://hptuexam.web3o.cloud/join/",
    "https://hptuexam.web3o.cloud/contact/",

    ]


    rank_read = pd.read_csv("rank.csv")

    n = 0
    all_arr = []
    for api in rank_read["roll"]:
        roll = str(rank_read["roll"][n])
        all_arr.append(roll)
        #print(new_json)
        #generate(new_json)
        #input("nnn")
        print(n)
        n = n +1
    new_data = ""

    for api2 in all_arr:
        url = "https://hptuexam.web3o.cloud/rank/"+str(api2)+""
        #html_data = "<a href='"+str(url)+"'></a>"
        example_urls.append(url)


    create_sitemap(example_urls)
