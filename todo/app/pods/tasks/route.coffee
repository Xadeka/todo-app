`import Ember from 'ember';`

Task = Ember.Object.extend
  name: ''
  isComplete: false

homework = Task.create
  name: 'Homework'
  isComplete: false

makeDinner = Task.create
  name: "Make Dinner"
  isComplete: false

taxes = Task.create
  name: "Submit taxes"
  isComplete: true

TaskRoute = Ember.Route.extend
  model: -> [homework, makeDinner, taxes]

`export default TaskRoute;`
