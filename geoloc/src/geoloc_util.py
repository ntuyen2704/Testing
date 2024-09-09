import requests
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--location', type=str, nargs='+',
                        help='Please enter the location')
    arguments = parser.parse_args()
    return arguments


def get_info_with_city_state(city_name, state_code):
    apikey = "f897a99d971b5eef57be6fafa0d83239"
    url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": [city_name, state_code],
        "limit": 1,
        "appid": apikey
    }
    headers = {'content-type': 'application/json'}
    try:
        r = requests.get(url, headers=headers, params=params)
        r.raise_for_status()
        response = r.json()
        print("INFO for {} {}: {} \n".format(city_name, state_code, response))
        return response
    except Exception as e:
        print(f"Failed to get the geoloc by {city_name, state_code} with error: {e}")
        return


def get_info_with_zip(zipcode):
    apikey = "f897a99d971b5eef57be6fafa0d83239"
    url = "http://api.openweathermap.org/geo/1.0/zip"
    headers = {'content-type': 'application/json'}
    params = {
        "zip": zipcode,
        "appid": apikey,
    }
    try:
        r = requests.get(url, headers=headers, params=params)
        r.raise_for_status()
        response = r.json()
        print("INFO for {}: {} \n".format(zipcode, response))
        return response
    except Exception as e:
        print(f"Failed to get the geoloc by zipcode {zipcode} with error: {e}")
        return

def main():
    args = parse_args()
    if not args.location:
        print("Please specify a location")
        exit()
    locations = args.location
    if locations == ['[]']:
        print("Please enter at least 1 location")
    for loc in locations:
        if loc.isnumeric():
            get_info_with_zip(loc)
        else:
            loc_info = [s.strip() for s in loc.split(',')]
            get_info_with_city_state(loc_info[0], loc_info[1])

if __name__ == '__main__':
    main()