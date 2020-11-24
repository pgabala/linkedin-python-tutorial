import urllib.request
import json


def printResults(data):
    theJson = json.loads(data)

    if "title" in theJson["metadata"]:
        print (theJson["metadata"]["title"])
        print (theJson["metadata"]["count"])

def main():
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    webUrl = urllib.request.urlopen(urlData)
    print ("result code: " + str(webUrl.getcode()))

    if (webUrl.getcode() == 200):
        data = webUrl.read()
        printResults(data)
    else:
        print("received error")


if __name__ == '__main__':
    main()