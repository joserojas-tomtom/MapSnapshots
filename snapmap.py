import sys
import urllib.request
import json

# Code here!

# Fetch parameters from the command line
# make sure there are 4 ..only 4
# 5 because position 0 == the application name
if (len(sys.argv) != 5): 
  print ('I need 4 args!')
  quit()

#print ('Argument List:', str(sys.argv))

# Read the API KEY from the file somewhere
apiKey = sys.argv[4]
zoom = sys.argv[3]
city = sys.argv[2]
size = sys.argv[1]

# Get the center location of the city.
# use this URL : https://api.tomtom.com/search/2/search/cancun.json?idxSet=Geo&key=*****
#
# y4OUatPPGQgS71stpTvqD6n2iyteZrYD 
url = 'https://api.tomtom.com/search/2/search/'+city+'.json?idxSet=Geo&key='+apiKey
print ( url )

req = urllib.request.urlopen(url)
data = req.read().decode('utf-8')
#print(data)

# Convert data into JSON
obj = json.loads(data)

if (len(obj["results"]) == 0):
  print ('City not found')
  quit()

print('Found city center of '+city+' at '+ str(obj["results"][0]["position"]))
print("...\n\n\n\n\n\n\n")
lat = obj["results"][0]["position"]["lat"]
lon = obj["results"][0]["position"]["lon"]

translatedSize = ""

#converted switch case /new

if sys.argv[1]== 'small':
    translatedSize = small
    
elif sys.argv[1]== 'medium':
    translatedSize = medium
    
elif sys.argv[1]== 'large':
    translatedSize = large
    
    
# default:
#         print ('Choose between small, medium, or large for the size parameter');

#         break



# Create API CALL to 'static image'
# https://api.tomtom.com/map/1/staticimage?layer=basic&style=main&format=png&zoom=13&center=4.899886%2C%2052.379031&width=2048&height=2048&view=Unified&key=*****
urlStaticImage = "https://api.tomtom.com/map/1/staticimage?" \
                 "layer=basic&style=main&format=png&zoom="+zoom+"&" \
                 "center="+str(lon)+","+str(lat)+translatedSize+"&key="+apiKey#print(urlStaticImage)
# Save image to a file ..
imageRequest = urllib.request.urlopen(urlStaticImage)
imageBinary = imageRequest.read()
sys.stdout.buffer.write(imageBinary)

#small = 256x256
#medium = 512x512
#large= 1024x1024

# Check if image should be sent to email/attachment 
