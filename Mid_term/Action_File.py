# fleet_management.action

# Define the goal
int32 fleet_size
---
# Define the result
string[] vehicle_routes
---
# Define the feedback
float32 completion_percentage


#in this action definition:

#fleet_size is an integer field in the Action Goal representing the desired fleet size.
#vehicle_routes is an array of strings in the Action Result representing the routes of the vehicles.
#completion_percentage is a float in the Action Feedback representing the percentage of completion of the action.
