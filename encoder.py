

def encode_url(url):
    new_url = ""
    url_list = url.split(".")
    for item in url_list:
        length = len(item)
        new_url += str(length) + item
    new_url += "0"
    return new_url

print(encode_url("dns.google.com"))