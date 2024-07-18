from app.db import Connection
from flask import jsonify


class State:
    """This is a model of a state"""

    states = []
    capitals=[]

    def __init__(self):
        self.db = Connection()

    def get_states(self):
        """Get all states"""

        query = "SELECT * FROM states"
        self.db.cursor.execute(query)
        rows = self.db.cursor.fetchall()
        if rows:
            for row in rows:

                state = {
                    "id": row[0],
                    "name": row[1],
                    "abbreviation": row[2],
                    "population": row[3],
                    "year_admitted": row[4],
                }
                self.states.append(state)
            return self.states
        else:
            return jsonify({"message": "Table is empty","status":404})

    def filter(self):
        """Filter states by first letter"""

        query = "SELECT * FROM states WHERE name LIKE 'W%'"
        self.db.cursor.execute(query)
        rows = self.db.cursor.fetchall()
        if rows:
            for row in rows:
                print(row)

                state = {
                    "id": row[0],
                    "name": row[1],
                    "abbreviation": row[2],
                    "population": row[3],
                    "year_admitted": row[4]
                }
                self.states.append(state)
            return self.states
        else:
            return "State not found"

    def create_state(self, name, abbreviation, population, year_admitted):
        """Create state method"""

        self.name = name
        self.abbreviation = abbreviation
        self.population = population
        self.year_admitted = year_admitted

        state = (self.name, self.abbreviation, self.population, self.year_admitted)

        query = "INSERT INTO states(name, abbreviation, population, year_admitted) VALUES(%s,%s,%s,%s)"

        result=self.db.cursor.execute(query, state)

        # If query execution is successful
        if result:
            self.db.conn.commit()
        self.db.cursor.close()
        self.db.conn.close()    
        
            
    
    def update_population(self, id, population):
        """update population of state"""
        
        self.population = population
        self.id = id
        
        state = (self.population, self.id) 
        
        query="UPDATE states SET population = %s WHERE id = %s"
        
        self.db.cursor.execute(query, state)

        # If query execution is successful
        # if self.db.cursor.rowcount:
        #     # Commit data to the database
        #     self.db.conn.commit()
        #     return "Updated Successfully"
        # else:
        #     return "Error updating the database"
            # return {
            #     "name": self.name,
            #     "abbreviation": self.abbreviation,
            #     "capital": self.capital,
            #     "population": self.population,
            #     "year_admitted": self.year_admitted
            # }
            
    def delete_state(self, id):
       
        self.id = id
        
        state = (self.id) 
   
        query="DELETE FROM states WHERE id = %d"
        
        self.db.cursor.execute(query, state)

        # If query execution is successful
        self.db.cursor.rowcount
            # Commit data to the database
        self.db.conn.commit()
            
    def search_state(self, name):
        """search state"""
       
        self.name = name
        
        state = (self.name) 
        
        query="SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
        
        self.db.cursor.execute(query, state)

        rows = self.db.cursor.fetchall()
        if rows:
            for row in rows:

                state = {
                    "id": row[0],
                    "name": row[1],
                    "abbreviation": row[2],                   
                    "population": row[3],
                    "year_admitted": row[4],
                }
                self.states.append(state)
            return self.states
        else:
            return "State does not exist"
        
    def list_state_names(self, name):
        """list state names"""
       
        self.name = name
        
        state = (self.name) 
        
        query="SELECT name FROM states ORDER BY states.name ASC"
        
        self.db.cursor.execute(query, state)

        rows = self.db.cursor.fetchall()
        if rows:
            for row in rows:

                state = {
                    "State Name": row[0],
                    
                }
                self.states.append(state)
            return self.states
        
        
    def most_populous(self, population):
        """most populated state"""
       
        self.population = population
        
        state = (self.population) 
        
        query="SELECT name, population FROM states ORDER BY population DESC LIMIT 2"
        
        self.db.cursor.execute(query, state)

        rows = self.db.cursor.fetchall()
        if rows:
            for row in rows:

                state = {
                    "name": row[0],
                    "population": row[1]
                    
                }
                self.states.append(state)
            return self.states
        
    
    def states_after_year(self, name, year_admitted):
        """states after year"""
        self.name = name
        self.year_admitted = year_admitted
        
        state = (self.name, self.year_admitted)
        
        query = """
        SELECT name, year_admitted
        FROM states
        WHERE year_admitted BETWEEN 1750 AND 1950 
        ORDER BY year_admitted ASC
        """
        self.db.cursor.execute(state,query)
        
        rows = self.db.cursor.fetchall()
        
        if rows:
            for row in rows:

                state = {
                    "name": row[0],
                    "year_admitted": row[1]
                }
        
        return row
    
        
    def average_population(self,population):
        """average population"""
        self.population = population
        
        query="SELECT AVG(population) FROM states"
        
        self.db.cursor.execute(query)

        rows = self.db.cursor.fetchone()
    
        return rows
    
     
    def count_population_range(self, population):
        """count population range"""
        self.population = population
        
        query = """
        SELECT COUNT(*)
        FROM states
        WHERE population BETWEEN 1000000 AND 5000000
        """
        self.db.cursor.execute(query)
        
        rows = self.db.cursor.fetchall()
        
        return rows
                
    
    def join_states_capitals(self):
        """join states to capitals"""
        
        query = """
        SELECT states.name, capitals.capital_name
        FROM states
        JOIN capitals ON states.id = capitals.state_id
        ORDER BY states.id ASC
        """
        self.db.cursor.execute(query)
        
        rows = self.db.cursor.fetchall()
        if rows:
            for row in rows:

                state = {
                    "name": row[0],
                    "capital": row[1]
                    
                }
                self.states.append(state)
            return self.states