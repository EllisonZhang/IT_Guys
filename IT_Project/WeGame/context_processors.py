import requests 

def add_variable_to_context(request):
    headers = {
      'Accept': 'application/json',
      'user-key': 'dde43976f970861f82bb8e3ea9cf06f8'
    }
    r = requests.post("https://api-v3.igdb.com/genres?fields=name,slug,updated_at,url&limit=8", headers=headers)
    categories = r.json()
    return {
        'categories': categories
    }