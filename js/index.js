$('.form').find('input, textarea').on('keyup blur focus', function (e) {
  
  var $this = $(this),
      label = $this.prev('label');

	  if (e.type === 'keyup') {
			if ($this.val() === '') {
          label.removeClass('active highlight');
        } else {
          label.addClass('active highlight');
        }
    } else if (e.type === 'blur') {
    	if( $this.val() === '' ) {
    		label.removeClass('active highlight'); 
			} else {
		    label.removeClass('highlight');   
			}   
    } else if (e.type === 'focus') {
      
      if( $this.val() === '' ) {
    		label.removeClass('highlight'); 
			} 
      else if( $this.val() !== '' ) {
		    label.addClass('highlight');
			}
    }

});

$('.tab a').on('click', function (e) {
  
  e.preventDefault();
  
  $(this).parent().addClass('active');
  $(this).parent().siblings().removeClass('active');
  
  target = $(this).attr('href');

  $('.tab-content > div').not(target).hide();
  
  $(target).fadeIn(600);
  
});


$('#submit_cook_information').click(function(){

  console.log("sending cook information");

  $.ajax({

    url: "/register",
    method: "POST",
    dataType: "JSON",
    data : {

              "mobile": $('#cook_mobile').val(),
              "firstname": $('#cook_firstname').val(),
              "lastname": $('#cook_secondname').val(),
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
            },

    success: function(data){
      console.log("cook regiter success");
      console.log(data);

    },

    error: function(data){

      console.log("cook register failure");
      console.log(data);

    }

  });

  return false;

});


