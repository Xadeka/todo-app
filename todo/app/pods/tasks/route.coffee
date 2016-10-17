`import Ember from 'ember';`

TaskRoute = Ember.Route.extend
  model: -> @store.findAll('task')

`export default TaskRoute;`
