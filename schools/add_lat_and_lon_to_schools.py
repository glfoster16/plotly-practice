import requests
import pandas as pd
import time

API_KEY = #YOUR API KEY GOES HERE. Create a free account at https://www.geoapify.com. A free account gets 6000 geocodes daily

df = pd.read_csv("Baltimore_City_Schools.csv")

base_addresses = df['address'].to_numpy()

addresses = []
for address in base_addresses:
    addresses.append(address+", Baltimore, MD")

timeout = 20
maxAttempt = 150

def getLocations(locations):
    url = "https://api.geoapify.com/v1/batch/geocode/search?apiKey=" + API_KEY + "&filter=countrycode:us"
    response = requests.post(url, json = locations)
    result = response.json()

    # The API returns the status code 202 to indicate that the job was accepted and pending
    status = response.status_code
    if (status != 202):
        print('Failed to create a job. Check if the input data is correct.')
        return
    jobId = result['id']
    getResultsUrl = url + '&id=' + jobId

    time.sleep(timeout)
    result = getLocationJobs(getResultsUrl, 0)
    if (result):
        #print(result)
        print('You can also get results by the URL - ' + getResultsUrl)
        return result
    else:
        print('You exceeded the maximal number of attempts. Try to get results later. You can do this in a browser by the URL - ' + getResultsUrl)

def getLocationJobs(url, attemptCount):
    response = requests.get(url)
    result = response.json()
    status = response.status_code
    if (status == 200):
        print('The job is succeeded. Here are the results:')
        return result
    elif (attemptCount >= maxAttempt):
        return
    elif (status == 202):
        print('The job is pending...')
        time.sleep(timeout)
        return getLocationJobs(url, attemptCount + 1)


text_addresses = getLocations(addresses)


longitudes = [address['lon'] for address in text_addresses]
latitudes = [address['lat'] for address in text_addresses]

df['lon'] = longitudes
df['lat'] = latitudes

print(df)

df.to_csv("Baltimore_City_Schools_Lon_Lat_Added.csv")



# header = ['name', 'lon', 'lat']

# # data = []
# # for address in text_addresses:
# #     data.append([address['query']['text'], address['lon'], address['lat']])
# # print(data)

# with open("Baltimore_City_School_Lat_Lon.csv", 'w', newline='') as file:

#     csvwriter = csv.writer(file)
#     csvwriter.writerow(header)
#     csvwriter.writerows(data)

