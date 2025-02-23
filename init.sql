CREATE TABLE IF NOT EXISTS items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    description TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

INSERT INTO items (name, description, created_at) VALUES
    ('Luke Skywalker', 'Jedi Knight from Star Wars', NOW()),
    ('Darth Vader', 'Sith Lord and father of Luke Skywalker', NOW()),
    ('Princess Leia', 'Leader of the Rebel Alliance', NOW()),
    ('Han Solo', 'Smuggler turned Rebel hero', NOW()),
    ('Yoda', 'Wise Jedi Master', NOW()),
    ('Frodo Baggins', 'Hobbit and Ring-bearer from Lord of the Rings', NOW()),
    ('Gandalf', 'Powerful wizard and member of the Istari', NOW()),
    ('Aragorn', 'Ranger of the North and heir to the throne of Gondor', NOW()),
    ('Legolas', 'Elven prince and skilled archer', NOW()),
    ('Gimli', 'Dwarf warrior and son of Glóin', NOW());
