  $(document).ready(function() {
   $('#addCarForm').submit(function(e) {
                e.preventDefault();
                
                // Validate dates
                const fromDate = new Date($('#fromDate').val());
                const toDate = new Date($('#toDate').val());
                
                if (fromDate > toDate) {
                    Swal.fire({
                        icon: 'error',
                        title: 'Invalid Dates',
                        text: 'From Date must be before To Date'
                    });
                    return;
                }
                
                // Prepare the data
                const carData = {
                    car_name: $('#carName').val(),
                    car_model: $('#carModel').val(),
                    car_color: $('#carColor').val(),
                    creator_code: $('#creatorCode').val(),
                    from_date: $('#fromDate').val(),
                    to_date: $('#toDate').val()
                };
                
                // Show loading indicator
                Swal.fire({
                    title: 'Processing...',
                    html: 'Please wait while we add the new car',
                    allowOutsideClick: false,
                    didOpen: () => {
                        Swal.showLoading();
                    }
                });
                
                // Make the AJAX POST request
                $.ajax({
                    url: 'http://localhost:8000/cars',
                    type: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify(carData),
                    dataType: 'json',
                    success: function(response) {
                        Swal.fire({
                            icon: 'success',
                            title: 'Success!',
                            text: 'Car added successfully',
                            confirmButtonText: 'OK'
                        }).then((result) => {
                            // Redirect to the main page after success
                            window.location.href = '/'; // Change to your main page URL
                        });
                    },
                    error: function(xhr, status, error) {
                        let errorMessage = 'An error occurred while adding the car';
                        if (xhr.responseJSON && xhr.responseJSON.message) {
                            errorMessage = xhr.responseJSON.message;
                        }
                        
                        Swal.fire({
                            icon: 'error',
                            title: 'Submission Failed',
                            text: errorMessage,
                            confirmButtonText: 'OK'
                        });
                    }
                });
            });
   });