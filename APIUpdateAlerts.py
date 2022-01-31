import requests
import time
import os
import datetime

# API Update Alerts
# 28th January 2022 - Tenshi

'''
This script monitors the mojang api to check for version updates
If it detects an update it will alert you in a webhook
Checks run every 300s (5m)
'''


webHooks = [
    "Webhook1",
    "Webhook2 (optional)"
]


def writeVersion_release(version):
    f = open('APIVersion.txt', 'w')
    f.write(version)
    f.close()


def readVersion_release():
    if os.path.exists('APIVersion.txt'):
        f = open('APIVersion.txt', 'r')
        version = f.read()
        f.close()
        return version
    return None


def writeVersion_staging(version):
    f = open('APIVersionStaging.txt', 'w')
    f.write(version)
    f.close()


def readVersion_staging():
    if os.path.exists('APIVersionStaging.txt'):
        f = open('APIVersionStaging.txt', 'r')
        version = f.read()
        f.close()
        return version
    return None


def getVersion_release():
    r = requests.get("http://api.mojang.com/")
    if r.status_code == 200:
        return r.json()['Implementation-Version']
    else:
        return None


def getVersion_staging():
    r = requests.get("https://api-staging.mojang.com")
    if r.status_code == 200:
        return r.json()['Implementation-Version']
    else:
        return None


def report_release(oldVer, newVer):
    embedJson = {
        "content": "",
        "embeds": [
            {
                "title": "Release API Update Detected",
                "description": "The Mojang API has updated",
                "color": None,
                "fields": [
                    {
                        "name": "Old version",
                        "value": oldVer
                    },
                    {
                        "name": "New version",
                        "value": newVer
                    }
                ],
                "footer": {
                    "text": "Tenshi Update Detector"
                },
                "timestamp": str(datetime.datetime.utcnow())
            }
        ]
    }

    for webHook in webHooks:
        requests.post(webHook, json=embedJson)


def report_staging(oldVer, newVer):
    embedJson = {
        "content": "",
        "embeds": [
            {
                "title": "Staging API Update Detected",
                "description": "The Mojang Staging API has updated",
                "color": None,
                "fields": [
                    {
                        "name": "Old version",
                        "value": oldVer
                    },
                    {
                        "name": "New version",
                        "value": newVer
                    }
                ],
                "footer": {
                    "text": "Tenshi Update Detector"
                },
                "timestamp": str(datetime.datetime.utcnow())
            }
        ]
    }

    for webHook in webHooks:
        requests.post(webHook, json=embedJson)


def main():
    while True:
        curVer = readVersion_release()
        apiVer = getVersion_release()

        if apiVer != None:
            if curVer == None:
                print(
                    f"No current version data, logging {apiVer} to APIVersion.txt")
                writeVersion_release(apiVer)
            else:
                if apiVer != curVer:
                    print(
                        f"New Release API version {apiVer} has been detected")
                    report_release(curVer, apiVer)
                    writeVersion_release(apiVer)

        curVer = readVersion_staging()
        apiVer = getVersion_staging()

        if apiVer != None:
            if curVer == None:
                print(
                    f"No current version data, logging {apiVer} to APIVersion.txt")
                writeVersion_staging(apiVer)
            else:
                if apiVer != curVer:
                    print(
                        f"New Staging API version {apiVer} has been detected")
                    report_staging(curVer, apiVer)
                    writeVersion_staging(apiVer)

        time.sleep(300)


if __name__ == "__main__":
    main()
