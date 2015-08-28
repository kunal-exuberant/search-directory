class Help{
	
	function error_description($desc){
		case 'MISSING_API_PARAMETER':
			$error['message'] = "Missing some API parameters";
			break;
		default : 
			$error['message'] = "Some untracked error occured";
				
	}

}