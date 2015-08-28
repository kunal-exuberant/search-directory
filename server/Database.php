<?php

class Database{

	$ip = 'localhost';
	$password = '';
	$db = '';
	$user = '';
	
	function __constructor(){
		$con = new mysqli($ip, $user, $password, $db);
	}

	function register_insert(){
		$con->query("insert into cook() values());
	}
}

?>