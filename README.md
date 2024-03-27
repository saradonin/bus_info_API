# Bus Info API

API aimed at ensuring compliance with legal regulations by providing a comprehensive passenger information system.

## Features
- ser Authentication: Secure token-based authentication system using JWT tokens.
- User Registration: Simple user registration process to create new accounts.
- Organizer Management: CRUD operations for managing organizers.
- Carrier Management: CRUD operations for managing carriers.
- Bus Line Management: Create, retrieve, update, and delete bus lines with ease.
- Territorial Unit Management: View a list of administrative division units of the country.
- Location Management: Browse locations and their details


## Endpoints

#### Authentication endpoints:
- `/login/`: Endpoint for obtaining JWT tokens for authentication.
- `/login/refresh/`: Endpoint for refreshing JWT tokens.
- `/register/`: Endpoint for user registration.


#### Territorial units and location endpoints:
- `/territory/`: Endpoint for listing territorial units.
- `/locations/`: Endpoint for listing locations.

#### Organizer endpoints:
- `/organizers/`: Endpoint for listing and creating organizers.
- `/organizer/<int:pk>/`: Endpoint for retrieving, updating, or deleting a specific organizer by its primary key.

#### Carrier endpoints:
- /`carriers/`: Endpoint for listing and creating carriers.
- `/carrier/<int:pk>/`: Endpoint for retrieving, updating, or deleting a specific carrier by its primary key.

#### Line endpoints:
- `/lines/`: Endpoint for listing and creating lines.
- `/lines/by-organizer/<int:organizer_id>/`: Endpoint for listing lines by a specific organizer.
- `/lines/by-carrier/<int:carrier_id>/`: Endpoint for listing lines by a specific carrier.
- `/line/<int:pk>/`: Endpoint for retrieving, updating, or deleting a specific line by its primary key.
