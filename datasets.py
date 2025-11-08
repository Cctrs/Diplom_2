creds_for_registration = {
    "email": "abragsmitmarker10000@gmail.com",
    "password": "pass123",
    "name": "CosmoCaactusBurger10000"
}

empty_required_params = [
    {
    "email": '',
    "password": "pass125",
    "name": "CosmoCaactusBurger10000"
    },
    {
    "email": "abragsmitmarker@gmail.com",
    "password": '',
    "name": "CosmoCaactusBurger10000"
    },
    {
    "email": "abragsmitmarker@gmail.com",
    "password": "pass125",
    "name": ""
    }
]

wrong_creds_for_login = [
    {"email": "abragsmitmarker10000@gmail.com",
    "password": "pass124"},
    {"email": "abragsmitmarker10000500@gmail.com",
    "password": "pass123"},
    {"email": "",
    "password": "pass123"},
    {"email": "abragsmitmarker10000@gmail.com",
    "password": ""}
]

update_user_info = [
    ({"email": "agrosmaker1000@gmail.com"},
    {
    "email": "agrosmaker1000@gmail.com",
    "name": "CosmoCaactusBurger10000"
    }),
    ({"pass": "password124"},
    {
    "email": "abragsmitmarker10000@gmail.com",
    "name": "CosmoCaactusBurger10000"
    }),
    ({"name": "Kaaaktus"},
    {
    "email": "abragsmitmarker10000@gmail.com",
    "name": "Kaaaktus"
    })
]

update_user_info_without_authorization = [
    {"email": "agrosmaker1000@gmail.com"},
    {"pass": "password124"},
    {"name": "Kaaaktus"}  
]

order_with_correct_ingredients = {
    "ingredients": [
                "61c0c5a71d1f82001bdaaa6d",
                "61c0c5a71d1f82001bdaaa72"
            ]
}

order_without_ingredients = {
    "ingredients": [
            ]
}

ingredients_with_wrong_hash = {
    "ingredients": [
                "61c0c5a7182001bdaaa6d",
                "61c0c5a71d1f820daaa72"
            ]
}

#error_messages
authorization_error_message = "You should be authorised"
wrong_creds_error_message = "email or password are incorrect"
wrong_ingredient_error_message = "Ingredient ids must be provided"
user_already_exists_message = "User already exists"
empty_required_fields_message = "Email, password and name are required fields"