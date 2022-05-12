#!/bin/bash
#!/usr/bin/python3

# usage
# ./cocktail.sh [drink]




curl -i "https://www.thecocktaildb.com/api/json/v1/1/search.php?s={$1}" > drink.txt

python3 cocktail.py 
