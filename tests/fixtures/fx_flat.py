# Flat

valid_script = """
<script id="jsdata">
var data =
{
  "advert": {
    "id": 680044731,
    "map": {
      "lat": 43.260625,
      "lon": 76.962848
    },
    "photos": [
      {
        "src": "https://cf-kr.kcdn.online/webp/b7/1-full.jpg",
        "title": "Аренда квартир в Алматы: 1-комнатная "
      }
    ],
    "price": 300000,
    "rooms": 1,
    "square": 30
  },
  "adverts": [
    {
      "description": "Номер в Апарт-гостинице City Park!",
      "fullAddress": "Алматы, Наурызбайский р-н, Жунисова",
      "uuid": "b7331c3a-3219-410a-a04c-47043a354dc7"
    }
  ]
}
</script>
"""

expected_data = {
    "id": 680044731,
    "uuid": "b7331c3a-3219-410a-a04c-47043a354dc7",
    "url": "https://krisha.kz/a/show/680044731",
    "room": 1,
    "square": 30,
    "city": "Алматы",
    "lat": 43.260625,
    "lon": 76.962848,
    "description": "Номер в Апарт-гостинице City Park!",
    "photo": "https://cf-kr.kcdn.online/webp/b7/1-full.jpg",
    "price": 300000,
    "focus": None,
    "star": None,
}
