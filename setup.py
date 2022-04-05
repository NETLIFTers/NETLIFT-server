
# {
#   "users" : [
#     {
#       "id": 1,
#       "username": "test_user",
#       "email": "test@gmail.com",
#       "password_digest": "sdkh4#%@^3wersd",
#       "active_program_id": 2,
#       "body_weight": 90,
#       "unit": "kg", // This can be changeable (weight unit
#       "smallest_increment": 1.25,
#       "programs": [
#       {
#         "id": 1,
#         "training_days": [1, 1, 0, 1, 1, 1, 0],
#         "workouts": [1, 2, 1, 5], // these are the workout ids
#       }
#       ],
#       "workouts": [
#       {
#         "id": 3,
#         "lifts": [1, 2, 4], // These are the lift ids
#         "completed": [1648727486], // These are time stamps when completed
#       },
#       ]
#     },
  # "lifts": [
  #   {
  #     "id": 3,
  #     "name": "squat",
  #     "reps": 5,
  #     "sets": 5,
  #     "exercise_id": 1
  #   },
#   ];
#   weights: [
#     {
#       user_id: 1,
#       lift_id: 3,
#       history: [60, 90, 80], // Always stored in kg
#     },
#   ];
#   ];

#   exercises:[
#     {
#       //info from exercise
#     }
#   ]
# }

# training_days=[0,1,3,5] = sunday, monday, wednesday, friday
