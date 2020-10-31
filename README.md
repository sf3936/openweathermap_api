# openweathermap_api
A lightweight flask wrapper for openweathermap api.

I have build a user-friendly api to get real time weather data from

    openweathermap.com
    

The UI is pretty straight forward you type the name 
of a city and and the response is the current weather.
I have also added the option to use the mock server by checking a checkbox.

I have also configured each environment (i.e dev and prod)
to use their individual configurations : 

        1. production env. is using the real time api by default
        2. development env. is using the 'mock server' by default
        
P.S: The mock server returns a single result, 
the weather data of Petah Tikva.
If the 'Mock Server' checkbox is checked, the mockserver random result 
will be returned regardless of the search query

The App is running live on :
production env. is using the real time api by default

####    https://openweather-map-api.herokuapp.com/ 
