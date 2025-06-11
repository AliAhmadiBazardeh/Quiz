 $(document).ready(function() {
           all_cars = []         
            
              // Fetch cars from API
            function fetchCars() {
            all_cars = []  
                 $.ajax({
                    url: 'http://localhost:8000/cars',
                    type: 'GET',
                    dataType: 'json',
                    beforeSend: function() {
                        $('#carList').html(`
                            <div class="spinner-container">
                                <div class="spinner-border text-primary" role="status">
                                    <span class="visually-hidden">Loading...</span>
                                </div>
                            </div>
                        `);
                    },
                    success: function(cars) {
                        console.log('carsss')
                        console.log(cars)

                        if (cars && cars.length > 0) {
                            all_cars = cars
                            loadCars(cars);
                            updateColorFilterOptions(cars);
                        } else {
                           // showNoCarsMessage();
                             $('#carList').html(`
                            <div class="col-12 text-center my-5">
                                <i class="fas fa-exclamation-triangle fa-3x text-warning mb-3"></i>
                                <h4>No Cars Found</h4>
                                <p>Unable to find car data. Register new car.</p>
                                <a href="/register" class="btn btn-success" id="register">Register</a>
                                <p>or</p>                                
                                <button class="btn btn-primary" onclick="fetchCars()">Reload</button>                            
                            </div>
                        `);
                        }
                    },
                    error: function(xhr, status, error) {
                        console.error('Error fetching cars:', error);
                        $('#carList').html(`
                            <div class="col-12 text-center my-5">
                                <i class="fas fa-exclamation-triangle fa-3x text-danger mb-3"></i>
                                <h4>Error Loading Cars</h4>
                                <p>Failed to load car data. Please try again later.</p>
                                <button class="btn btn-primary" onclick="fetchCars()">Retry</button>
                            </div>
                        `);
                    }
                });
            }

            // Load cars into the page
            function loadCars(filteredCars = cars) {
                $('#carList').empty();
                
                if (filteredCars.length === 0) {
                    $('#carList').html(`
                        <div class="col-12 text-center my-5">
                            <i class="fas fa-car-crash fa-3x text-muted mb-3"></i>
                            <h4>No cars found</h4>
                            <p>Try adjusting your search filters</p>
                        </div>
                    `);
                    return;
                }
                
                filteredCars.forEach(car => {
                    const availabilityClass = car.status === 'available' ? 'bg-success' : 
                                            car.status === 'rented' ? 'bg-danger' : 'bg-warning';
                    const statusText = car.status === 'available' ? 'Available' : 
                                     car.status === 'rented' ? 'Rented' : 'In Maintenance';
                    
                    $('#carList').append(`
                        <div class="col-md-4 mb-4">
                            <div class="card h-100">
                                
                                <div class="card-body">
                                    <h5 class="card-title">${car.car_name}</h5>
                                    <p class="card-text">
                                        <span class="d-block mt-2"><strong>Color:</strong> ${car.car_color}</span>
                                        
                                        <span class="d-block"><strong>Available:</strong> ${car.from_date} to ${car.to_date}</span>
                                    </p>
                                </div>
                                <div class="card-footer bg-transparent">
                                    <button class="btn btn-sm btn-outline-primary view-details" data-car-id="${car.slug}">
                                        <i class="fas fa-info-circle"></i> Details
                                    </button>
                                   
                                </div>
                            </div>
                        </div>
                    `);
                });
                
                // Add event listeners to the new buttons
                $('.view-details').click(function() {
                    const carId = $(this).data('car-id');
                    showCarDetails(carId);
                });
                
                $('.rent-car').click(function() {
                    const carId = $(this).data('car-id');
                    rentCar(carId);
                });
            }
            
            // Show car details in modal
            function showCarDetails(carId) {
                const car =  all_cars.find(c => c.slug == carId);
                if (!car) return;
                
                const availabilityClass = car.status === 'available' ? 'text-success' : 
                                        car.status === 'rented' ? 'text-danger' : 'text-warning';
                const statusText = car.status === 'available' ? 'Available' : 
                                 car.status === 'rented' ? 'Rented' : 'In Maintenance';
                
                $('#carModalTitle').text(car.car_name);
                $('#carModalBody').html(`
                    <div class="row">
                        <div class="col-md-6">
                            <table class="table table-bordered">
                                <tr>
                                    <th>Model</th>
                                    <td>${car.car_model}</td>
                                </tr>
                                <tr>
                                    <th>Color</th>
                                    <td>${car.car_color}</td>
                                </tr>
                             
                                <tr>
                                    <th>Reserve date</th>
                                    <td>${car.from_date} to ${car.to_date}</td>
                                </tr>
                            </table>
                        </div>
                        <div class="col-md-6">
                            
                            <h5>Description</h5>
                            <p>This ${car.car_name} ${car.car_color} ${car.car_model}. It's reserved between ${car.from_date} and ${car.to_date} .</p>
                        </div>
                    </div>
                `);
                
                const modal = new bootstrap.Modal(document.getElementById('carDetailsModal'));
                modal.show();
            }                               
            
            // Filter cars based on search and filters
            function filterCars() {
                const searchText = $('#searchInput').val().toLowerCase();
                const statusFilter = $('#filterStatus').val();
                const dateFilter = $('#filterDate').val();
                
                let filtered = cars;
                
                // Apply status filter
                if (statusFilter !== 'all') {
                    filtered = filtered.filter(car => car.status === statusFilter);
                }
                
                // Apply search text
                if (searchText) {
                    filtered = filtered.filter(car => 
                        car.car_model.toLowerCase().includes(searchText) || 
                        car.car_name.toLowerCase().includes(searchText) || 
                        car.car_color.toLowerCase().includes(searchText)
                    );
                }
                
                // Apply date filter
                if (dateFilter) {
                    filtered = filtered.filter(car => 
                        new Date(car.from_date) <= new Date(dateFilter) && 
                        new Date(car.to_date) >= new Date(dateFilter)
                    );
                }
                
                loadCars(filtered);
            }
            
            // Event listeners for filtering
            $('#searchInput, #filterStatus, #filterDate').change(filterCars);
            $('#searchBtn').click(filterCars);
            $('#searchInput').keypress(function(e) {
                if (e.which === 13) filterCars();
            });
            
            // Initial load
            fetchCars();            
        });