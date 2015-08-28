<?php
class Api{

	if(isset($_POST['mobile']) && isset($_POST['firstname']) && isset($_POST['lastname']) && isset($_POST['service_area']) && isset($_POST['food_type']) && isset($_POST['food_variety']) && isset($_POST['language_known']) && isset($_POST['min_charge_people']) && isset($_POST['max_charge_people']) && isset($_POST['verification']) && isset($_POST['available_timing'])){

		$database = new Database();
		$database->register();


	}
	else{
		$help->error_description("MISSING_API_PARAMETER");
	}
	?>

}



{
    "mobile": 89345345345,
    "firstname": "kunal",
    "lastname": "singh",
    "service_area": [
        "hoodi",
        "itpl",
        "btm layout 1"
    ],
    "food_type": 0,
    "food_variety": 1,
    "language_known": 0,
    "min_charge_people": {
        "total_charge": 2000,
        "people": 2
    },
    "max_charge_people": {
        "total_charge": 6000,
        "people": 8
    },
    "verification": 1,
    "available_timing": [
        {
            "startTime": "6000",
            "endTime": "7000"
        },
        {
            "startTime": "8000",
            "endTime": "9000"
        }
    ]
}
