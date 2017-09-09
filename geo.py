#coding=utf-8
import googlemaps

#change this param to your own—apply on google map api platform, you may use vpn for need.
API_KEY = ''

def is_number(s):
	'''
	judge if a string is an float or integer 
	'''
	try:
		float(s)
		return True
	except ValueError:
		pass

	try:
		import unicodedata
		unicodedata.numeric(s)
		return True
	except (TypeError, ValueError):
		pass

	return False


def read_file(file_name):
	'''
	read file and get addresses into list
	'''
	with open(file_name, 'r') as file:
		addresses = []
		for line in file:
			addresses.append(line.strip())
		#addresses = list(set(addresses))
		return addresses
		file.close()

def translate_addr(addr):
	'''
	translate address name into 'format name ' and latitude, longtitude
	'''

	with open('team_location_info11.txt','a+') as file:
		gmaps = googlemaps.Client(key=API_KEY)
		for address in addr:
			
			geo_result = gmaps.geocode(address, language='zh-CN')
			if (len(geo_result)<=0):
				continue
			addr_name = geo_result[0]['formatted_address']
			addr_laitude = geo_result[0]['geometry']['location']['lat']
			addr_longtitude = geo_result[0]['geometry']['location']['lng']	
			file.write('%s,%s,%f,%f\n' % (address, addr_name.encode('utf-8'), addr_laitude, addr_longtitude))
		file.close()
	print 'write file finished......'

# addresses = read_file('team-location.txt')
addresses = read_file('team-location.txt')
print 'read address file finished....'
print 'total address is :', len(addresses)
print 'translate begin'
translate_addr(addresses)