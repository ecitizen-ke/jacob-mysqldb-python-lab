from flask import Blueprint,  jsonify, request
from app.models import State

states_bp = Blueprint("states_bp", __name__)


@states_bp.route("/states", methods=["GET"])
def get_states():
    #initialize the state object 
    # states = 
    
    return jsonify({"states":State().get_states(), "code": 200})
 
 
@states_bp.route("/states/filter", methods=["GET"])
def filter_by_starting_letter():
    states = State().filter()
    return jsonify({"states": states, "code": 200})


@states_bp.route("/states/create", methods=["POST"])
def create_state(): 
     # create new instance of `State` class and assign it to variable `state`
    state = State()

    # Get data from the request object
    data = request.get_json()
    
    name = data.get("name")
    abbreviation = data.get("abbreviation")
    population = data.get("population")
    year_admitted = data.get("year_admitted")

    # invoke create state method
    outcome=state.create_state(name, abbreviation, population, year_admitted)
    if outcome == False:
        return jsonify({"message": "State already exists in the database.", "status": 200})
    return jsonify({"message": "State created successfully", "status": 201})

    


@states_bp.route("/states/update", methods=["PATCH"])
def update_population():
    
    state=State()
    data=request.get_json()
    
    id=data.get("id")
    population=data.get("population")
    
    state.update_population(id,population)
    return jsonify({"message":"Population updated successfully", "code":200})


@states_bp.route("/states/delete", methods=["DELETE"])
def delete_state():
    
    state=State()
    data=request.get_json()
    
    id=data.get("id")
    
    delete=state.delete_state(id)
    if delete:
        return jsonify({"message": "State deleted successfully", "status": 200})
    else:
        return jsonify({"message": "Error deleting from the database", "status": 404})
   

@states_bp.route("/states/search", methods=["GET"])
def search_state():
    
    state=State()
    data=request.get_json
    
    name=data.get("name")
    
    states=state.search_state(name)
    return jsonify({"states": states, "code": 200})


@states_bp.route("/states/list", methods=["GET"])
def list_state_names():
    states = State().list_state_names([])
    return jsonify({"state": states, "code": 200})


@states_bp.route("/states/populous", methods=["GET"])
def most_populous():
    states = State().most_populous([])
    return jsonify({"states": states, "code": 200})


@states_bp.route("/states/average", methods=["GET"])
def average_population():
    states = State().average_population([])
    return jsonify({"average_population": states, "code": 200})


@states_bp.route("/states/after_year", methods=["GET"])
def states_after_year():
    states = State().states_after_year([],[])
    return jsonify({"states": states, "code": 200})


@states_bp.route("/states/count", methods=["GET"])
def count_population_range():
    states = State().count_population_range([])
    return jsonify({"Population Range": states, "code": 200})


@states_bp.route("/states/join", methods=["GET"])
def join_states_capitals():
    states = State().join_states_capitals()
    return jsonify({"states": states, "code": 200})