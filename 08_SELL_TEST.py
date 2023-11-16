import requests

def test_sell():
    rreply = requests.post('http://localhost:5000/sell/', json={"title": "The Boy in the Striped Pyjamas","author":"John Boyne","year_of_publication":2006})
    print(rreply.status_code)
    print(rreply.json())


test_sell()