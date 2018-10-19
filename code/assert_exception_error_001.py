def kelvinToFahrenheit(Temperature):
    assert (Temperature>=0),"colder than aboslute zero!"
    res=((Temperature-273)*1.8)+32
    return res
print(kelvinToFahrenheit(273))
print(kelvinToFahrenheit(567.87))
print(kelvinToFahrenheit(-5))
