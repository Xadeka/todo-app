`import Ember from 'ember';`

TaskController = Ember.Controller.extend
  tasks: Ember.computed.alias 'model'
  
  displayedTasks: []

  all: false
  active: false
  completed: false

  actions:
    filterClick: (btn) ->
      @set('all', false)
      @set('active', false)
      @set('completed', false)

      if btn == 'all'
        @set('all', true)
        @set('displayedTasks', @get('tasks'))
        console.log(@get('displayedTasks'))
      else if btn == 'active'
        @set('active', true)
        @set('displayedTasks', @get('tasks').filterBy('isComplete', false))
        console.log(@get('displayedTasks'))
      else if btn == 'completed'
        @set('completed', true)
        @set('displayedTasks', @get('tasks').filterBy('isComplete', true))
        console.log(@get('displayedTasks'))


      return
      

`export default TaskController;`
