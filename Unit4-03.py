# Created by: Scarlett Gao
# Created on: Oct 2017
# Created for: ICS3U

import ui

def postal_address(street_address,city,postal_code,province,apartment_number = None):
	
    if(apt_number == None):
        print (street_address+' ' +city+' ' +postal_code+' ' +province)
  
    else:
        print (street_address+' ' +city+' ' +postal_code+' ' +province+' ' +apartment_number)
  
user_street_address = raw_input("Enter your address ",)
user_city = raw_input("Enter your city name ",)
user_postal_code = raw_input("Enter your postal code",)
user_province = raw_input("Enter your province ",)
user_apartment_number = raw_input("Enter your appartment number ",) 
postal_address(user_street_address, user_city, user_postal_code, user_province, user_apartment_number ) 
		
view = ui.load_view()
view.present('full_screen')
