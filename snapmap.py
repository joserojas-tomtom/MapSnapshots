import sys
# Code here!

# Fetch parameters from the command line
# make sure there are 3 ..only 3
# 4 because position 0 == the application name
if (len(sys.argv) != 4): 
  print ('I need 3 args!')
  quit()

#print ('Argument List:', str(sys.argv))

# Read the API KEY from the file somewhere
apiKey = sys.argv[3]
zoom = sys.argv[2]
city = sys.argv[1]

# Get the center location of the city.
# use this URL : https://api.tomtom.com/search/2/search/cancun.json?idxSet=Geo&key=*****
url = 'https://api.tomtom.com/search/2/search/'+city+'.json?idxSet=Geo&key='+apiKey
print ( url )

req = urllib.request.urlopen(url)
data = req.read().decode('utf-8')
print(data)

# Create API CALL to 'static image'

# Save image to a file ..

# Check if image should be sent to email/attachment 
