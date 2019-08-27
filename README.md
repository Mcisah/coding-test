# coding-test

Graphql Api built with Django and Graphene-django for a coding challenge:

Hosted on [heroku](https://coding-test-bc.herokuapp.com)

**Setup**
- pip install -r requirements.txt
- /manage.py runserver


**Query**

Example:
```
query Calculate($input:RequiredInput!){
  calculatePrice(arg:$input)
}
```

**Input**

Example
```
{
  "input": {
    "type": "sell",
    "margin": 0.2,
    "exchangeRate": 0.0028
  }
}
```


**Testing**

To run tests:
- ./manage.py test