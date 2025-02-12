import requests
import json

# Define your GraphQL endpoint
url = "https://offer-api-prd.delta.com/prd/rm-offer-gql"

# Define headers (authentication if required)
headers = {
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9,en-IN;q=0.8',
  'airline': 'DL',
  'applicationid': 'DC',
  'authorization': 'GUEST',
  'channelid': 'DCOM',
  'content-type': 'application/json',
  'origin': 'https://www.delta.com',
  'referer': 'https://www.delta.com/',
  'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Microsoft Edge";v="132"',
  'sec-ch-ua-mobile': '?0',
  'sec-fetch-site': 'same-site',
  'transactionid': '646509b9-58da-41de-b010-00a125075031_1738818639319',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0',
  'x-app-type': 'shop'
}

# Define your query and variables
query = """
query ($offerSearchCriteria: OfferSearchCriteriaInput!) {
  gqlSearchOffers(offerSearchCriteria: $offerSearchCriteria) {
    offerResponseId
    gqlOffersSets {
      offers {
        offerId
        additionalOfferProperties {
          offered
          soldOut
          lowestFare
          totalTripStopCnt
          discountAvailable
        }
        offerPricing {
          discountsApplied {
            code
            pct
          }
          originalTotalAmt {
            currencyEquivalentPrice {
              currencyAmt
              roundedCurrencyAmt
              formattedCurrencyAmt
            }
            milesEquivalentPrice {
              mileCnt
            }
          }
          totalAmt {
            currencyEquivalentPrice {
              currencyAmt
              roundedCurrencyAmt
              formattedCurrencyAmt
            }
            milesEquivalentPrice {
              mileCnt
            }
          }
          promotionalPrices {
            code
            pct
            price {
              milesEquivalentPrice {
                mileCnt
              }
              currencyEquivalentPrice {
                currencyAmt
                roundedCurrencyAmt
                formattedCurrencyAmt
              }
            }
          }
        }
      }
      itineraryDepartureDate
    }
    offerDataList {
      pricingOptions {
        pricingOptionDetail {
          currencyCode
        }
      }
      flexReturnDates
      responseProperties {
        tripTypeText
        discountInfo {
          discountPct
          discountTypeCode
          nonDiscountedOffersAvailable
        }
        promotionsInfo {
          promotionalCode
          promotionalPct
        }
      }
    }
  }
}
"""

variables = {
    "offerSearchCriteria": {
        "productGroups": [{"productCategoryCode": "FLIGHTS"}],
        "customers": [{"passengerTypeCode": "ADT", "passengerId": "1"}],
        "offersCriteria": {
            "resultsPageNum": 4,
            "pricingCriteria": {"priceableIn": ["MILES"]},
            "preferences": {"nonStopOnly": False, "refundableOnly": False},
            "flightRequestCriteria": {
                "sortByBrandId": "BE",
                "searchOriginDestination": [{
                    "departureLocalTs": "2025-02-28T00:00:00",
                    "destinations": [{"airportCode": "WAS"}],
                    "origins": [{"airportCode": "PAR"}],
                    "calenderDateRequest": {"daysBeforeCnt": 3, "daysAfterCnt": 3}
                }]
            }
        }
    }
}           

# Send the request
try:
    response = requests.post(
        url,
        headers=headers,
        json={"query": query, "variables": variables}
    )
    response.raise_for_status()  # Raise HTTP errors
    data = response.json()
    
    if "errors" in data:
        print("GraphQL Errors:", data["errors"])
    else:
        print("Result:", data["data"])
except requests.exceptions.RequestException as e:
    print("HTTP Error:", e)