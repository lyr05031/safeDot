"""
Scanning System (Web)
Provide Scanning Class and Methods for Web Scanning
"""
import requests
import json
from bs4 import BeautifulSoup as bS


class scanner:
    def __init__(self, md5):
        """
        Constructed Function
        """
        self.md5 = md5
        self.header = \
            {
                "User_Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69"
            }

    def dasheng_sandbox(self):
        """
        大圣沙箱 Engine
        POST
        """
        url = "https://mac-cloud.riskivy.com/api/sample/report"
        data = \
            {
                "page": "1",
                "pageSize": "10",
                "keyWord": "{}".format(self.md5),
                "scene": 2
            }
        self.header["content-type"] = "application/json; charset=UTF-8"
        data = json.dumps(data)
        res = requests.post(url, headers=self.header, data=data)
        del self.header["content-type"]
        res = json.loads(res.text)
        state = res["data"]["total"]
        if state != 0:
            level = res["data"]["items"][0]["level"]
            if level != None:
                if level > 0:
                    return 1  # is a virus
                else:
                    return 2  # not a virus
            else:
                return 3  # no data
        else:
            return 3  # no data

    def virus_total(self):
        """
        VirusTotal Engine
        Using Old Version of the Website
        POST
        """
        url = "https://www.virustotal.com/old-browsers/home/search"
        data = {"query": "{}".format(self.md5)}
        res = requests.post(url, headers=self.header, data=data)
        if res.status_code == 200:
            res = bS(res.text, "lxml")
            res = res.find_all("span", {"id": "detections"})[0]
            res = res.get_text()
            res = res.replace(" ", " ").replace("\n", " ").split("/")
            percent = int(res[0]) / int(res[1])
            if percent >= 0.10:
                return 1  # is a virus
            else:
                return 2  # not a virus
        else:
            return 3  # no data


if "__main__" == __name__:
    newScanner = scanner("67660b2243401bcb2a08e6bda7d8bc0b")
    print(newScanner.dasheng_sandbox(), newScanner.threat_book(), newScanner.virus_total())

# 微步改版, 已无法使用
"""
    def threat_book(self):
        ""
        微步 Engine
        POST
        ""
        url = "https://s.threatbook.cn/api/v3/webpage/search"
        self.header["content-type"] = "application/json"

        data = \
            {
                "md5": self.md5
            }
        data = json.dumps(data)
        res = requests.post(url, headers=self.header, data=data)
        del self.header["content-type"]
        res = json.loads(res.text)
        state = res["status_code"]
        if state == -1:
            return 3  # no data
        elif state == 0:
            percent = res["data"][0]["multi_engines"].split("/")[0]
            percent1 = res["data"][0]["threat_score"]
            if int(percent) >= 1 or percent1 >= 29:
                return 1  # is a virus
            else:
                return 2  # not a virus
"""