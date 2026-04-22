USE lana_dog_walking;

-- INSERT records for: owners

INSERT INTO owners (first_name, last_name, phone_number, address) VALUES
('Sarah',   'Johnson',  '302-555-1001', 'Wilmington, DE'),
('David',   'Kim',      '302-555-1002', 'Newark, DE'),
('Emily',   'Nguyen',   '302-555-1003', 'Dover, DE'),
('Carlos',  'Rivera',   '302-555-1004', 'Philadelphia, PA'),
('Jessica', 'Patel',    '302-555-1005', 'Hockessin, DE'),
('Brian',   'Thompson', '302-555-1006', 'Middletown, DE'),
('Amanda',  'Wilson',   '302-555-1007', 'Dover, DE'),
('James',   'Martinez', '302-555-1008', 'Middletown, DE'),
('Rachel',  'Chen',     '302-555-1009', 'Newark, DE'),
('Tyler',   'Adams',    '302-555-1010', 'Wilmington, DE');

-- INSERT records for: walkers

INSERT INTO walkers (walker_name, phone_emergency) VALUES
('Mike Torres',   '302-555-9911'),
('Lana Brooks',   '302-555-9912'),
('Jordan Hayes',  '302-555-9913'),
('Taylor Morgan', '302-555-9914'),
('Alexis Reed',   '302-555-9915'),
('Devin Price',   '302-555-9916'),
('Morgan Scott',  '302-555-9917'),
('Casey Flores',  '302-555-9918'),
('Jamie Collins', '302-555-9919'),
('Sam Bell',      '302-555-9920');

-- INSERT records for: dogs

INSERT INTO dogs (owner_id, dog_name, breed, age, weight_size, health_concerns, photo_url) VALUES
(1,  'Buddy',   'Labrador Retriever',  3, 'Large',  'None',           'https://photos.com/buddy.jpg'),
(2,  'Daisy',   'Golden Retriever',    5, 'Large',  'Hip dysplasia',  'https://photos.com/daisy.jpg'),
(3,  'Max',     'German Shepherd',     2, 'Large',  'None',           'https://photos.com/max.jpg'),
(4,  'Bella',   'French Bulldog',      4, 'Small',  'Brachycephalic', 'https://photos.com/bella.jpg'),
(5,  'Cooper',  'Beagle',              6, 'Medium', 'None',           'https://photos.com/cooper.jpg'),
(6,  'Luna',    'Poodle',              1, 'Medium', 'None',           'https://photos.com/luna.jpg'),
(7,  'Charlie', 'Border Collie',       3, 'Medium', 'None',           'https://photos.com/charlie.jpg'),
(8,  'Molly',   'Dachshund',           7, 'Small',  'Back problems',  'https://photos.com/molly.jpg'),
(9,  'Rocky',   'Boxer',               4, 'Large',  'None',           'https://photos.com/rocky.jpg'),
(10, 'Sadie',   'Australian Shepherd', 2, 'Medium', 'None',           'https://photos.com/sadie.jpg');

-- INSERT records for: walks

INSERT INTO walks (walker_id, dog_id, walk_date, start_time, duration_minutes, gps_tracking) VALUES
(1,  1, '2024-01-10', '08:00:00', 30, 'Active'),
(2,  2, '2024-01-10', '09:00:00', 45, 'Active'),
(3,  3, '2024-01-11', '07:30:00', 60, 'Active'),
(1,  4, '2024-01-11', '10:00:00', 20, 'Inactive'),
(4,  5, '2024-01-12', '08:15:00', 30, 'Active'),
(2,  6, '2024-01-12', '11:00:00', 45, 'Active'),
(5,  7, '2024-01-13', '07:00:00', 40, 'Active'),
(3,  8, '2024-01-13', '09:30:00', 25, 'Inactive'),
(6,  9, '2024-01-14', '08:45:00', 35, 'Active'),
(4, 10, '2024-01-14', '10:30:00', 50, 'Active');

-- INSERT records for: payments

INSERT INTO payments (owner_id, walk_id, amount, payment_date, payment_method) VALUES
(1,  1, 18.50, '2024-01-10', 'Credit Card'),
(2,  2, 22.50, '2024-01-10', 'Apple Pay'),
(3,  3, 30.00, '2024-01-11', 'Cash'),
(4,  4, 12.00, '2024-01-11', 'Credit Card'),
(5,  5, 18.50, '2024-01-12', 'Zelle'),
(6,  6, 22.50, '2024-01-12', 'Credit Card'),
(7,  7, 20.00, '2024-01-13', 'Venmo'),
(8,  8, 15.00, '2024-01-13', 'Cash'),
(9,  9, 19.25, '2024-01-14', 'Credit Card'),
(10,10, 27.50, '2024-01-14', 'Zelle');

SELECT * FROM owners;
SELECT * FROM walkers;
SELECT * FROM dogs;
SELECT * FROM walks;
SELECT * FROM payments;
