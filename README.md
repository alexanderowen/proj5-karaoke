# proj5-karaoke
CIS 399 Winter 2016  

Author: Alexander Owen  
URL: http://ix.cs.uoregon.edu/~aowen/htbin/cis399/proj5-karaoke/  
http://ix.cs.uoregon.edu:7957/    

A simple map of Eugene, with markers on points of interest.    

Places a marker with a popup of the address when the user clicks on the map.  
Also determines user location (with permission, of course) and places a marker on the map.  
Uses the Mapquest geocoding API to determine street address.  


# A bit on future features  
Coloring the map markers differently if they are POI markers, user location, so on. (Requires more work than 
seems necessary. The markers are stored as images. Storing different markers may require including some
extra files/importing a marker library like MakiMarker or AwesomeMarkers)

