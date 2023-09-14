import re
import json
from datetime import datetime

import requests
from bs4 import BeautifulSoup

base_url = "https://index.minfin.com.ua/ua/russian-invading/casualties"


def get_url():
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.select('div[class=ajaxmonth] h4[class=normal] a')
    urls = ["/"]
    prefix = "/month.php?month="
    for tag_a in content:
        urls.append(prefix + re.search(r"\d{4}-\d{2}", tag_a["href"]).group())  # \d decimal {4} times
    return urls


def spider(urls):
    data = []
    for url in urls:
        response = requests.get(base_url + url)
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.select('ul[class=see-also] li[class=gold]')  # combined css selectors with speciall attributes
        for element in content:
            result = {}
            date = element.find('span', attrs={"class": "black"}).text  # find one result
            try:
                date = datetime.strptime(date, "%d.%m.%Y").isoformat()
            except ValueError:
                print(f"error for {date}")
                continue

            result.update({"date": date})
            losses = element.find('div').find('div').find('ul')
            for l in losses:
                title, quantity, *rest = l.text.split('—')
                title = title.strip()
                quantity = re.search(r"\d+", quantity).group()  # + match 1 or more repetitions
                result.update({title: quantity})
            data.append(result)
    return data


if __name__ == '__main__':
    urls_for_parser = get_url()
    r = spider(urls_for_parser)
    with open('moskali.json', 'w', encoding='utf-8') as fd:
        json.dump(r, fd, ensure_ascii=False)  #  converts the Python objects into appropriate json objects




# curl 'https://rozetka.com.ua/ua/' \
#   -H 'authority: rozetka.com.ua' \
#   -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
#   -H 'accept-language: en,en-US;q=0.9,uk;q=0.8' \
#   -H 'cache-control: no-cache' \
#   -H 'cookie: cart-modal=old; ab-auto-portal=old; promo-horizontal-filters=verticalFilters; ab-catalog-tile-description=old; social-auth=old; ab_tile_filter=old; xab_segment=48; xl_uid=Cgo8MmTnnPQaf8zS0rqTAg==; uid=Cgo9D2TnnPQqW15biK4gAg==; _gcl_au=1.1.446003088.1692900601; visitor_city=1; _ga=GA1.3.664391036.1692900601; _uss-csrf=noWminAkO50knD7lMcYYeXLBWYN4NyCxqG9xfdFBehWJQOcn; ussapp=sdXPJeiSDrPuf3Ooz5_r8qxSx28FMTUx-KLwDlrg; afclid=31193029001692900602; __exponea_etc__=f81cbb89-e5df-452f-91ed-12b48904d29c; _fbp=fb.2.1692900608024.626711701; _hjSessionUser_3494164=eyJpZCI6ImRkMjY1ZTZlLWM0YzAtNWY1Zi1hNzI3LTJiZWEyNzg4ZWQ3OCIsImNyZWF0ZWQiOjE2OTI5MDA2MDE0NzQsImV4aXN0aW5nIjp0cnVlfQ==; __utmz_gtm=utmcsr=localhost|utmccn=(referral)|utmcmd=referral; xab_tests=%7B%22ab-catalog-backend%22%3A%22old%22%2C%22cart-modal%22%3A%22old%22%2C%22ab-auto-portal%22%3A%22old%22%2C%22filter-tabs%22%3A%22old%22%2C%22ab-catalog-delivery-terms%22%3A%22old%22%2C%22ab-catalog-selection-filters%22%3A%22old%22%2C%22promo-horizontal-filters%22%3A%22verticalFilters%22%2C%22ab-catalog-tile-description%22%3A%22old%22%2C%22fingerprint%22%3A%22off%22%2C%22skip-add-phone%22%3A%22off%22%2C%22social-auth%22%3A%22old%22%2C%22ab-ch-contact-form%22%3A%22new%22%2C%22ab-ch-d-p-tg-form%22%3A%22off%22%2C%22ab_ch_seller_btn%22%3A%22off%22%2C%22ab_tile_filter%22%3A%22old%22%2C%22ab-login-one-tap%22%3A%22off%22%2C%22ab_ch_req_email%22%3A%22off%22%2C%22ab-code-filter%22%3A%22old%22%2C%22ab-p-fan%22%3A%22off%22%7D; cf_clearance=qo2XB2ln4vWwkkYOvAIENtsYy6zcVj0rlM_CUvKe7Ao-1694624126-0-1-8680bef5.88db5388.d181e115-0.2.1694624126; _hjIncludedInSessionSample_3494164=0; _hjSession_3494164=eyJpZCI6IjQxY2I0OWJkLTVlOTAtNGM5YS1iNjdlLTQ5MTk0ZDQ0N2I5NCIsImNyZWF0ZWQiOjE2OTQ2MjQxMjYyNDQsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; _gid=GA1.3.1652095763.1694624127; __exponea_time2__=-0.08624720573425293; __cf_bm=IrC8WIX1W2jXJ2x9XmBw9H.C_Hv1bDtj2cYn4z2Xqt0-1694625085-0-AVZWqMgiluZ0OnQQcqyHeA+2e1nXGuf/5UxxA1mxHqz7DjNrOBvikN3+MJDHAOf584LTb46D1vfsaQ5rMtIXsHY=; slang=ua; _ga_3X15VBC9L9=GS1.3.1694624127.5.1.1694625403.8.0.0; cto_bundle=lMN34V9mRFY1dEhJRXowRzNkS2F3bTl3MjdIWGY4REslMkZLNFZUMXNDRFhtV1ZHMW41MjlkaGtnQlh2ajdzQlJuaSUyRmslMkZxczJtNzY0dk1QRTJxbXIyVDNvaHN1dXJQQ3FPVmNmenRDU0RJS3FIUFdYem9sWWJpdSUyRmlLMEZWdUVXUHV6RkM4UUZPR1NWbnlGUndNRGN6bjJiVVdWaCUyQjVqZXNhTjVSZ0RHcUdqJTJCb05heFQ0eENZYXo4V3FnempBN1k5b0t2amh2dzViTnVSM2hmd0NGeXhYdkdVYmp3JTNEJTNE' \
#   -H 'pragma: no-cache' \
#   -H 'sec-ch-ua: "Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: document' \
#   -H 'sec-fetch-mode: navigate' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'sec-fetch-user: ?1' \
#   -H 'service-worker-navigation-preload: true' \
#   -H 'upgrade-insecure-requests: 1' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36' \
#   --compressed