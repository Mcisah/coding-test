# coding-test

Graphql Api built with Django and Graphene-django for a coding callenge:

Query:
```
query Calculate($input:RequiredInput!){
  calculatePrice(arg:$input)
}
```


Input:
```
{
  "input": {
    "type": "sell",
    "margin": 0.2,
    "exchangeRate": 0.0028
  }
}
```

