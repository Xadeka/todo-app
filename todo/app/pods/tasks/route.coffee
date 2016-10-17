`import Ember from 'ember';`

#@store.createRecord 'task',
#  name: 'Homework'
#  isComplete: false
#homework.save()

#@store.createRecord 'task',
#  name: "Make Dinner"
#  isComplete: false
#makeDinner.save()

#@store.createRecord 'task',
#  name: "Submit taxes"
#  isComplete: true
#taxes.save()

TaskRoute = Ember.Route.extend
  model: -> @store.findAll('task')

`export default TaskRoute;`
