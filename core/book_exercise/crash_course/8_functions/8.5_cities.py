def describe_city(city_name, county_name='australia'):
    country_list = ['usa', 'uk', 'ussr']
    if county_name in country_list:
        print(f"{city_name.title()} is in {county_name.upper()}.")
    else:
        try:
            print(f"{city_name.title()} is in {county_name.title()}.")
        except AttributeError:
            print(f"{city_name} are in {county_name.title()}.")


describe_city('sydeny')
describe_city('Reykjavik', 'Iceland')
describe_city('washington', county_name='usa')
describe_city(city_name='Varanasi', county_name='India')
describe_city(['sydeny', 'melburn', 'pearth', 'canberra'])
describe_city({'sydeny', 'melburn', 'pearth', 'canberra'})
describe_city(city_name=['mumbai', 'manglore', 'delhi', 'dwarka'], county_name='India')

describe_city(city_name=input("Enter city name: "), county_name=input("Enter country name: "))
