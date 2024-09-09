import pytest
import subprocess
import os
from src.geoloc_util import get_info_with_zip, get_info_with_city_state


@pytest.mark.parametrize("zipcodes", ["12345", "10001"])
def test_get_loc_by_zipcode(zipcodes):
    loc_info = get_info_with_zip(zipcodes)
    assert loc_info.get('zip') == zipcodes


@pytest.mark.parametrize("city, state", [("Madison", "WI"), ("Chicago", "IL")])
def test_get_loc_by_city_state(city, state):
    loc_info = get_info_with_city_state(city, state)
    assert loc_info[0].get('name') == city


dir = os.path.dirname(os.path.dirname(__file__))
cli = ["python", "geoloc_util.py", "--location"]
testcases = [("12345", "12345"),
             ("Madison, WI", "Madison")]


@pytest.mark.parametrize("arguments, expected", testcases)
def test_single_loc(arguments, expected):
    cli.append(arguments)
    result = subprocess.run(cli, capture_output=True, shell=True, cwd=dir + "\src")
    output = result.stdout.decode("utf-8")
    print("output ", output)
    assert expected in output


def test_multi_loc1():
    arguments = ["Madison, WI", "12345"]
    expected_state = "Madison"
    full_cmd = cli + arguments
    print('FULL CMD: ', full_cmd)
    result = subprocess.run(full_cmd, capture_output=True, shell=True, cwd=dir + "\src")
    output = result.stdout.decode("utf-8")
    assert arguments[1] in output
    assert expected_state in output


def test_multi_loc2():
    arguments = ["Madison, WI", "12345", "Chicago, IL", "10001"]
    expected_state1 = "Madison"
    expected_state2 = "Chicago"
    full_cmd = cli + arguments
    print('FULL CMD: ', full_cmd)
    result = subprocess.run(full_cmd, capture_output=True, shell=True, cwd=dir + "\src")
    output = result.stdout.decode("utf-8")
    assert arguments[1] in output
    assert arguments[3] in output
    assert expected_state1 in output
    assert expected_state2 in output
