"""Delta Scraper"""
import requests
from response.BotResponse import BotResponse

class DeltaScraper:
    ''' Delta scraper'''
    def __init__(self, message):
        self.message = message
        self.bot_response = BotResponse()
        self.header = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-US,en;q=0.9,en-IN;q=0.8",
            "airline": "DL",
            "applicationid": "DC",
            "authorization": "GUEST",
            "channelid": "DCOM",
            "content-type": "application/json",
            "origin": "https://www.delta.com",
            "referer": "https://www.delta.com/",
            "sec-ch-ua": '"Not A(Brand";v="8", "Chromium";v="132", "Microsoft Edge";v="132"',
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-site": "same-site",
            "transactionid": "646509b9-58da-41de-b010-00a125075031_1738818639319",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0",
            "x-app-type": "shop",
            "Postman-Token": "3853b6ca-fdeb-49c8-9424-1eed9810480d",
            "Host": "offer-api-prd.delta.com",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Content-Length": "2866",
            "Cookie": "_abck=B0666EB889A57CA2293B3B11AD194CE7~-1~YAAQLG/ZF2ia4hKVAQAA1ix2Ng1cXZrNs4NcnilvSrfiUruJVGqYMv+gWDtw4462KaT8TDigJ0R59i+xlhxIF6mSgqfdA1P0SdzbW307JDZNotycuw9zeaufudg+3fd7ADGJRcLXhJWqSQZYjZ6heq78+DBUiEJCVxAmf/9/xObAQp7diIOmt4m7VUm2ciZ+TAMPfApu+Xmmt4eaC5LqpdoKi7L+IHgS2iJdb2BhmCtm7mXR/i5SCoGQiRXDKLq4WurLGxcaMxx0RshpIMvLIqjeaYvpc8aP/9hmRLSeMSH0kHupQK9e+xtNofO+1dIDvouSGvVlf7aiUAs3MG//1Zn8BgUOwLVhEkVSw6YQlCX5Yf2M631Vx5io1PRaCKqzFYiIS1p8fT8jei2/KADW61brkypcpsco255GXmjERQ7GXzAPPxOBTzYp16faXGUPPirhOEz4DS+K8iFlJ6jHMjHjpe/8EQSebYOFTfOhAJp9RFt+EJjJK6z4AT7MGQQ+aida0/t7CSoS0kMSK+yXzS1setnO3nBWE0lGHZucOv3KdEnrptr5F26Ox99fOakZi+riqNWbMg+k10C1mOSq3cyivmgQS7KyqmbVHxUNVUalkMmGqHeBwJqR1RYEOmImiW1q3au+iKqmfkUEvByVaepoAWcpSWDn/pkQKiqd1TFX6VwAdOYfNgH8tLkM3aPz1yPyUPEDWmwnPdTLL6AGyVBs2kU82VTS3OQny2CHssg/RJj55kl49MxuQkGWL5Bp5HwzRA7bIeOnQttBWTjW2HeAx03B6CI8uQ//5wIi4JGvNawvHsAUsUziAu9qYmutQZRVBOI+jsfR+ky8n6VPBpdwD6S8wDrlD74fKliHqTiv36J9KQPdQiODINlzYcp9M7YG3OWa~-1~-1~1738822103; bm_s=YAAQLG/ZF2ma4hKVAQAA1yx2NgKlYPDWKenzLJ7Tk5cCu/RF7f8bfg7FkxjQ0dTbb1eoNOa+3ipbn9YDhuVrjZi15bocsszZEqVOssrsFvteFyyy+pGiAEAaE2E5SUDEmCTuE4QB2irmrW4MHF2UqN2pIdkEzmu/wm6NnP619zt468G1brybK3rAKTWUtVVuHCxmDsg3Ed7m7qoFPj5Y+WNVGrWM1TA8BZLlgxllS0eAYlfkB/wjAzhJ6qeySjX8cPe60ydANLNg+O5EIHn7YrKQLPMqnwiFWXNXjbZuBsyqUtzyNLly1bzox/7fWEAjYkhNWVsEXS709wTmlr1B6F71oj2z3XF01Ybf24vR8RodCy/zCfwGAUu5QsuB9Y1L7219SOmVkRiJmmMuLD7r7kne+/iwX5tXcPqSpYFkwwiFYsDqnrFNKgwvl8KWyHAAPfraWM3YLTMqhucYbFWFoTjK",
        }
        self.api_url = "https://offer-api-prd.delta.com/prd/rm-offer-gql"

    def send_request(self):
        ''' Sending request to Delta Airline for flight data'''
        payload = "{\"query\":\"query ($offerSearchCriteria: OfferSearchCriteriaInput!) {\\n  gqlSearchOffers(offerSearchCriteria: $offerSearchCriteria) {\\n    offerResponseId\\n    gqlOffersSets {\\n      offers {\\n        offerId\\n        additionalOfferProperties {\\n          offered\\n          soldOut\\n          lowestFare\\n          totalTripStopCnt\\n          discountAvailable\\n        }\\n        offerPricing {\\n          discountsApplied {\\n            code\\n            pct\\n          }\\n          originalTotalAmt {\\n            currencyEquivalentPrice {\\n              currencyAmt\\n              roundedCurrencyAmt\\n              formattedCurrencyAmt\\n            }\\n            milesEquivalentPrice {\\n              mileCnt\\n            }\\n          }\\n          totalAmt {\\n            currencyEquivalentPrice {\\n              currencyAmt\\n              roundedCurrencyAmt\\n              formattedCurrencyAmt\\n            }\\n            milesEquivalentPrice {\\n              mileCnt\\n            }\\n          }\\n          promotionalPrices {\\n            code\\n            pct\\n            price {\\n              milesEquivalentPrice {\\n                mileCnt\\n              }\\n              currencyEquivalentPrice {\\n                currencyAmt\\n                roundedCurrencyAmt\\n                formattedCurrencyAmt\\n              }\\n            }\\n          }\\n        }\\n      }\\n      itineraryDepartureDate\\n    }\\n    offerDataList {\\n      pricingOptions {\\n        pricingOptionDetail {\\n          currencyCode\\n        }\\n      }\\n      flexReturnDates\\n      responseProperties {\\n        tripTypeText\\n        discountInfo {\\n          discountPct\\n          discountTypeCode\\n          nonDiscountedOffersAvailable\\n        }\\n        promotionsInfo {\\n          promotionalCode\\n          promotionalPct\\n        }\\n      }\\n    }\\n  }\\n}\",\"variables\":{\"offerSearchCriteria\":{\"productGroups\":[{\"productCategoryCode\":\"FLIGHTS\"}],\"customers\":[{\"passengerTypeCode\":\"ADT\",\"passengerId\":\"1\"}],\"offersCriteria\":{\"resultsPageNum\":4,\"pricingCriteria\":{\"priceableIn\":[\"MILES\"]},\"preferences\":{\"nonStopOnly\":false,\"refundableOnly\":false},\"flightRequestCriteria\":{\"sortByBrandId\":\"BE\",\"searchOriginDestination\":[{\"departureLocalTs\":\"2025-03-23T00:00:00\",\"destinations\":[{\"airportCode\":\"WAS\"}],\"origins\":[{\"airportCode\":\"PAR\"}],\"calenderDateRequest\":{\"daysBeforeCnt\":3,\"daysAfterCnt\":3}}]}}}}}"
        response = requests.post(url=self.api_url, data=payload, headers=self.header, timeout=300)
        self.bot_response.send_response(response)
