import requests

cookies = {
    'JSESSIONID': '15EADBCEE24B711048249761A82C5035',
    'SERVERID': 'amwebuse1b|aYZug|aYZud',
}
"SERVERID=amwebuse1b|aYZwK|aYZwC; JSESSIONID=073A9A94CF60E5F7F17229E8978F683C"

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://md.itic.occinc.com/excavatorTickets',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    # 'Cookie': 'JSESSIONID=15EADBCEE24B711048249761A82C5035; SERVERID=amwebuse1b|aYZug|aYZud',
}
url = "https://md.itic.occinc.com/excavatorTicketView?ienc=XMah5PSf8nUNd8/0qy7Ln4RWjRB2Z/mLDXTLUWJj1Xk="
response = requests.get(
    url,
    cookies=cookies,
    headers=headers,
)

print(response.text)
