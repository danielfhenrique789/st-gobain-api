
def get_routes(Resource, parser):
    TODOS = {
        'todo1': {'task': 'build an API'},
        'todo2': {'task': '?????'},
        'todo3': {'task': 'profit!'},
    }

    def abort_if_todo_doesnt_exist(todo_id):
        if todo_id not in TODOS:
            abort(404, message="Todo {} doesn't exist".format(todo_id))


    # TodoList
    # shows a list of all todos, and lets you POST to add new tasks
    class TodoList(Resource):
        def get(self):
            return TODOS

        def post(self):
            args = parser.parse_args()
            todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
            todo_id = 'todo%i' % todo_id
            TODOS[todo_id] = {'task': args['task']}
            return TODOS[todo_id], 201

    return [{"class":TodoList,"endpoint":"/todos"}, {"class":Todo,"endpoint":"/todos/<todo_id>"}]