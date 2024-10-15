Superhero API:
    This is a Flask-based API for managing superheroes and their powers. The API supports the following models and relationships:
         Hero: Represents a superhero.
         Power: Represents a special ability or power.
         HeroPower: Represents the association between a Hero and their Power, including the strength of that power.

To connect to postgresSQL database, this command is used ('psql -U ben -h localhost -d superheroes')

The DB name is superheroes with below tables and their relations

                 List of relations
 Schema |      Name       | Type  | Owner 
--------+-----------------+-------+-------
 public | alembic_version | table | ben
 public | hero_powers     | table | ben
 public | heroes          | table | ben
 public | powers          | table | ben
(4 rows)

To initialize the database, the below commands are followed
     flask db init
     flask db migrate -m "Initial migration."
     flask db upgrade
