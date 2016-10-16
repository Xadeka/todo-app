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

TaskCollection = Ember.Object.extend
  content: []
  contentCompleted: (completed) ->
    @get('content').filterBy('isComplete', completed)

tasks = TaskCollection.create()
tasks.get('content').pushObject(homework)
tasks.get('content').pushObject(makeDinner)
tasks.get('content').pushObject(taxes)

TaskRoute = Ember.Route.extend
  model: ->
    tasks.contentCompleted(false)

`export default TaskRoute;`
