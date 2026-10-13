#!/usr/bin/env bash
# FDA Recalls API quick start (curl)
# Get a free key: https://rapidapi.com/crisp-point-studio-crisp-point-studio-default/api/live-fda-product-food-recalls

curl --request GET \
  --url 'https://live-fda-product-food-recalls.p.rapidapi.com/api/recalls?search=salmonella&limit=10' \
  --header 'X-RapidAPI-Key: YOUR_RAPIDAPI_KEY' \
  --header 'X-RapidAPI-Host: live-fda-product-food-recalls.p.rapidapi.com'
