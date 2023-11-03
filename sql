SELECT users.name
from users
inner join permissions
on projects.id = permissions.project_id

inner join users
on permissions.user_id = users.id

where project.name = "Next-Gen Polymer"



SELECT projects.name
from projects

inner join permissions
on projects.id = permissions.project_id

inner join users
on permissions.user_group_id = users.user_group_id
or on permissions.user_id = users.id

where users.email = 'ceo@acme.co'


