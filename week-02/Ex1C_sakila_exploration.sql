/*
a) The actor table includes columns for actor_id, first_name, last_name, and last_update
b) The film table includes film_id, title, description, release_year, language_id, original_language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features, and last_update
c) The film_actor table contains both the actor_id and film_id columns on the schema navigator
d) The rental table includes: rental_id, rental_date, inventory_id, customer_id, return_date, staff_id, and last_update. It is hard to read because the data uses ID numbers instead of actual names, so you can't tell who rented what without looking at other tables. The results also showed NULL rows making it even harder to interpret directly
e) The inventory table includes: inventory_id, film_id, store_id, and last_update
f) To find the names of films rented on a specfic date we need the rental, inventory, and film tables. They are related through a chain of IDs: the rental table links to inventory via inventory_id, and the inventory table links to film via film_id. By following this path, you can connect a specific rental date to a movie title.
*/

SELECT rental_id, rental_date, inventory_id FROM rental;
SELECT inventory_id, film_id FROM inventory;
SELECT film_id, title FROM film;