APIs to test:

auth:
    POST: /auth/users/              # Register a new user
    POST: /auth/token/login/        # Obtain auth token
    POST: /auth/token/logout/       # Logout (invalidate token)
booking:
    GET: /restaurant/bookings/      # List all bookings
    POST: /restaurant/bookings/     # Create a new booking
    GET: /restaurant/bookings/<id>/ # Retrieve a single booking
    PUT: /restaurant/bookings/<id>/ # Update a booking
    PATCH: /restaurant/bookings/<id>/ # Partially update a booking
    DELETE: /restaurant/bookings/<id>/ # Delete a booking
menu:
    GET: /restaurant/menu/          # List all menu items
    POST: /restaurant/menu/         # Create a new menu item
    GET: /restaurant/menu/<id>/     # Retrieve a single menu item
    PUT: /restaurant/menu/<id>/     # Update a menu item
    PATCH: /restaurant/menu/<id>/   # Partially update a menu item
    DELETE: /restaurant/menu/<id>/  # Delete a menu item


# create new user:
curl --request POST \
  --url http://127.0.0.1:8000/auth/users/ \
  --header 'Content-Type: application/json' \
  --data '{"username": "newuser1", "password": "securepassword", "re_password": "securepassword"}'

# get token: 
curl --request POST \
  --url http://localhost:8000/auth/token/login \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/11.0.0' \
  --data '{
    "username": "newuser1",
    "password": "securepassword"
}'


# menu list (use your token from prev request above ^):
curl --request GET \
  --url http://127.0.0.1:8000/restaurant/menu \
  --header 'Authorization: Token 51a55364b370f1a0829dbd86a6d47b64627d25b2'

# get by id (use your token from prev request above ^):
curl --request GET \
  --url http://127.0.0.1:8000/restaurant/menu/1 \
  --header 'Authorization: Token 51a55364b370f1a0829dbd86a6d47b64627d25b2'

# create new booking (use your token from prev request above ^):
curl --request POST \
  --url http://127.0.0.1:8000/restaurant/bookings/ \
  --header 'Authorization: Token 51a55364b370f1a0829dbd86a6d47b64627d25b2' \
  --header 'Content-Type: application/json' \
  --data '{"name": "John Doe","no_of_guests": 4,"booking_date": "2025-03-20T19:00:00Z"}'

# delete booking by id:
curl -X DELETE http://127.0.0.1:8000/restaurant/bookings/1/ \
    --header 'Authorization: Token 51a55364b370f1a0829dbd86a6d47b64627d25b2'

# post menu
curl --request POST \
  --url http://127.0.0.1:8000/restaurant/menu/ \
  --header 'Authorization: Token 51a55364b370f1a0829dbd86a6d47b64627d25b2' \
  --header 'Content-Type: application/json' \
  --data '{
           "title": "Pasta",
           "price": 12,
           "inventory": 50
         }'

# get menu :
curl --request GET \
  --url http://127.0.0.1:8000/restaurant/menu \
  --header 'Authorization: Token 51a55364b370f1a0829dbd86a6d47b64627d25b2'
