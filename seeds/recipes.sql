-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

-- Then, we recreate them
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    name text,
    cooking_time int,
    rating numeric(2,1)
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Chicken Curry', 90, 6.0);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Roast chicken', 125, 8);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Chips', 15, 7);
