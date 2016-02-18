angular.module("myapp", [])
.controller("myctrl", function($scope,$http){
	$scope.developer_team = [{"first_name": "Nikhil", "last_name": "Rane", "mobile_no": 9404505206, "email": "nikhilrane1992@gmail.com", "designation": "Software Developer and Trainer", "company_name": "Sahaj Academy Edutech LLP"},
				  {"first_name": "Kalyani","last_name":"Patil","mobile_no":8956515575,"email":"patilmadhukarkriti@gmail.com","designation":"Software Developer Intern", "company_name": "Sahaj Academy Edutech LLP"},
				  {"first_name": "Rahul","last_name":"Patil","mobile_no":9422979099,"email":"patil.rp@gmail.com","designation":"Software Developer and Trainer", "company_name": "Sahaj Academy Edutech LLP"}]
				  

				  // Simple GET request example:
	 var calllink = function(){
		$http({
			method: 'GET',
			url: 'http://www.makemycasa.com/misc/get/image/'
		}).then(function successCallback(response) {
		    // this callback will be called asynchronously
		    // when the response is available
		  }, function errorCallback(response) {
		    // called asynchronously if an error occurs
		    // or server returns response with an error status.
		  });
	}

			


		var init = function() {
		calllink();
	}
	init();
	
					

});