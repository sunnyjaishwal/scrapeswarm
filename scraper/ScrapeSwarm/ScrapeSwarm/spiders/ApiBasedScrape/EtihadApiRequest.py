import requests
import json
import logging

from utility.BotResponse import BotResponse

class EtihadApiRequest:
    """
    A class to handle API requests to Etihad's flight search service.
    """

    def __init__(self, message):
        self.message = message
        self.url = "https://api-des.etihad.com/airlines/EY/v2/search/air-bounds"
        self.payload = {
            "commercialFareFamilies": ["ECONOMY", "BUSINESS"],
            "itineraries": [{
                "originLocationCode": message['body']['parameters']['sourceIata'],
                "destinationLocationCode": message['body']['parameters']['destinationIata'],
                "departureDateTime": message['body']['parameters']['departureDate'],
                "isRequestedBound": True
            }],
            "travelers": [{"passengerTypeCode": "ADT"}],
            "promotion": {"code": "", "airlineCode": "EY"},
            "searchPreferences": {"showMilesPrice": True, "showSoldOut": True},
            "corporateCodes": ["264154"]
        }
        self.headers = {
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'ama-client-ref': '4cc8decf-c7d8-4e8f-a980-a1d8af4a743e:16',
            'authorization': 'Bearer Umg7nBXsGzUaCTDdOQrR8SGv6F0G',
            'content-type': 'application/json',
            'origin': 'https://digital.etihad.com',
            'priority': 'u=1, i',
            'referer': 'https://digital.etihad.com/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
            'x-d-token': '3:rVTPlBIBj/jbr/DntL5Cpg==:7dzJNDNZ84mGNOFFvhyFO36CDEO8bsm8/nc89n9PbY8JmPotHghqxPcqgmswDGBNX294R/dCCwAdIDnWOZMK8FEAZ3YepDBAGcQeuMIGh5zpoTuAg96p7AL8TlfiRyw07Dtzv1vf3i5ikERQ9AJy5f8l0irssi57kylkyzz7bthRc/3i2JwLXNsvUu4AQoX4NASi46sRNTBDEg5tGAzB7vBMxzBXC6zaRaPnR2mPduH3BcTf+tURSWRbpvWX1S5FDFTVVNAHzxTJRc6k9n7YVdl5Cezc3D8RnzyRASlhATKxSjhVeR/4p2Dr1l50+vnHZxUoGMil0NoBdHhRZrVjhBoObu5Wzn8tdugdDZ8sci8871p178gZMXSs9gY13UqiMEV6nIIeLUj9i0GLSHp72AlFvEQqazOR9+mLyeZ239Q/jJUk9Zy7kKWzonnSbZrKC2psw0Qe0kvrYuHtGithI5uNdZAx7YlxlEDD1bYtWIRRllt3iZ9d/diZJRyI2aofVy+mSsfRu6Wj8viUCUNUCYbhPhjzqPInv1ReS0Ux1dAd9xAZ005dmZQa6NnRNIW8mk2u5GyU1O9jM7tNrshfDC1tRkO81KHIRKlI/c+b2R+s/ytPswjILmojJe6AJloeHis0AHfUmVuJbl9j+j2hc++uHX9IdO5hrDuxLLpZzfqTcWifqlCItEfMLcU+R2ZlX5fQUddfmg9UQNhaHpbl8RQygQE5jAB4HBd+xVF8kbik5/4pUhCWbOYMDHBjh0l9F8MkdBPzOip9PeJ1ZqssFRwfiYqfJZeWX+CSISW6N/m78iDDB/rA+sJGD8r0OWafG+I4yoEuaNtrO+kPM45uf0CiTU059rOgsn75jSyVzGj68UdJdyuYxF0fc+qL9FE7:fHcr4G3ksssEXoeJbsIpV6TP+qkK3GSKWivZjsg8y7c=',
            'Cookie': '_abck=17FC7E8A48DA965103AF91218E2B2923~-1~YAAQRQVaaOLgmauUAQAAOu12yw0s9d/0FBEFOtjWlF0MBN8ZGkC7re+b43FFIK0+lnPoCff9I93vG3Eja0kkCv0byp6n5oATpHOZFFw2R0A+cvzUTDBLY9REyWPcrNEewjRr7B2rsmL6u7WQbWH+L0OYYTLuh9jJV8Po0/+06B9fLskL8UwH5KuNVAIbNmI/spMGwg8toTA6UAlrPkVZFXHbqcEFQyOUuRlgRna0cRRU2i9nnEgRIWJGmHDm19fpwutwyXeDy2L9x1T+4/ZC3IBK1sijXyUQ3z6/IZ52x/xPnzLVeeg3T/I7IxOh5jqIgmcwSMHUKPknhrW2yRznxXTNzyWsQ2Lh2KoQ8TJbr9v3MwoZ3m0bYw1xH4CnFWABiB98HusCIaDZSYeJAs68G9GaiJC/zPVZxZiujS0YjQPPFkHUeMzj5KUzZW1tZFUX/sMHQVPxCjXsA/ZsiDia8OE04/uAT/apROTPaAAI/+eY9wps/2RVMRTlQiBXEPsSBMkCMw/6h7U3L2HfSswlcmeJ2ZL/sEP00YyFvsSPesIZBDiUzKw8qcSWYms1y/kjFFqpaB3oMXhNp8xUAvb5xn6NbbMiWDnmH2YsVKiJg4PyFiNdUWz4+NSGk/zd4nrTf4/Zw31ujxzV9Hicn7+1tuX0s50Cz+ZBnoba7q6zi2sBXFzuXqH/wA1+2yKfJX6iKj74LXE9qZC6VwTd8VDyb1J74HFWupxY15qjcBsz2xydnSyz3YAE0UyG2WqGRzy/TowvWPGJHhH56BAvkA==~0~-1~-1; ak_bmsc=F364D70AA512A85098DA3F1A934CCD09~000000000000000000000000000000~YAAQTmw/F0s8XdGUAQAAaw197xq/ZlAG4RoH5kzIGxIxBt1K9dR/RhmY1rE9cXpnlTYEjBPekhULvLLxJNPXSRFPZYHWVRP9WUvVkZETnHMjXfFTa3Xy8kTMUKgM7EFqoHQmuYuA2Ll/LzmL09T3pIfCpoeQ4lgOCxQyuaMV8srobZE65ekeH6kke8vs2SoNdbcFrDRgIcg5fcXwD8ibT0N9H+xkdta2LfhyKqVvP266G0JIQ4LE8LDrZ7XzqBRhzDmJX6S5aWBjSkRN9yAjjmVcD4CVG+fpCF8LxTcktLPFQgG+pLYOVFhWS1c+Eo/J9hRkoUxnkDRuvTC3hrE7d8jn4t/S3RfrTpa6Dg==; bm_sv=63B0073CA6C0A5DDBD7663F9D9D89650~YAAQTmw/F3vTYNGUAQAA3TW37xopIIEO2KO1VmlL2ptswblPkTQxQhlLOWPBvgv4KksARWQRFSY5Wgz9XEyHFPUd/AxcmAmM/MuEQTqjMBVfdk5IOPgbnSRxj8LPChQR4XOPdk/eAS4JHB06yL1P3dU6G9Rb2vZ5zNTzZVFaajkLkngW6CWY0LGgyz1gyW47DYaApqv/Ls+5UhcdOfRKQp3e0qR7zf65IA6BOECQhhUwe3dMZx2Oaxt1y5fR4Hka~1; incap_ses_1854_2864801=htDXNRlPjh3ok1Y+Xru6GUeBqWcAAAAA2CyIlPlaiwk0eo9zel2jJQ==; incap_ses_1855_2864801=VnvsdrQSzSmg55ED3Ui+GYCBqWcAAAAAmbRa6b3zpdQp7fZHclPIQw==; incap_ses_747_2864801=gYSpQ5mdk0Mlo4y0wuBdCkTpqWcAAAAAg2Btt3zyXRejxNbXZ8cymw==; nlbi_2864801=XRO0WODnhSmtYv0TI3VJigAAAADe8LXZ+jT4f8IwXNQxnsl7; visid_incap_2864801=3c/uwzJSQ66yr1om5nwsTkZMoGcAAAAAQUIPAAAAAAAOIgqCQpcp4zUJE7h3Wn1W'
        }

        self.bot_response = BotResponse()
        logging.basicConfig(level=logging.INFO)

    def send_request(self):
        """
        Sends a POST request to the Etihad API and processes the response.
        """
        try:
            response = requests.post(self.url, data=self.payload, headers=self.headers)
            logging.info(f"Response Status Code: {response.status_code}")
            self.process_response(response.json(), self.message)
        except requests.exceptions.HTTPError as http_err:
            self.bot_response.send_error_response({"error": f"HTTP error occurred: {http_err}"}, self.message)
            logging.error(f"HTTP error occurred: {http_err}")
        except Exception as err:
            self.bot_response.send_error_response({"error": f"An error occurred: {err}"}, self.message)
            logging.error(f"An error occurred: {err}")

    def process_response(self, response):
        """
        Processes the API response and formats the flight data.

        Args:
            response (dict): The JSON response from the API.

        Returns:
            list: A list of formatted flight data.
        """
        try:
            airBoundGroups = response['data']['airBoundGroups']
            formatted_groups = []

            for bound in airBoundGroups:
                response_dict = {
                    'source': bound['boundDetails']['originLocationCode'],
                    'destination': bound['boundDetails']['destinationLocationCode'],
                    'flightData': {
                        'prices': bound['airBounds'][0]['prices']['totalPrices'],
                        'milesConversion': bound['airBounds'][0]['prices']['milesConversion']
                    }
                }
                formatted_groups.append(response_dict)

            response_json = json.dumps(formatted_groups)
            self.bot_response.response_processor(response_json, self.message)
        except KeyError as key_err:
            logging.error(f"Key error occurred: {key_err}")
            self.bot_response.send_error_response({"error": f"Key error occurred: {key_err}"}, self.message)
        except Exception as err:
            self.bot_response.send_error_response({"error": f"An error occurred: {err}"}, self.message)
            logging.error(f"An error occurred: {err}")
