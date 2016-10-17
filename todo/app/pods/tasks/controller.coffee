`import Ember from 'ember';`

TaskController = Ember.Controller.extend

  currentFilter: 'all'

  newTaskName: undefined

  tasks: Ember.computed 'model', 'currentFilter', ->
    filter = @get('currentFilter')
    if filter == 'all'
      @get('model')
    else if filter == 'active'
      @get('model').filterBy('isComplete', false)
    else if filter == 'completed'
      @get('model').filterBy('isComplete', true)


  all: Ember.computed 'currentFilter', ->
    @get('currentFilter') == 'all'

  active: Ember.computed 'currentFilter', ->
    @get('currentFilter') == 'active'

  completed: Ember.computed 'currentFilter', ->
    @get('currentFilter') == 'completed'


  actions:
    filterClick: (btn) ->
      @set('currentFilter', btn)

    removeTask: (task) ->
      @set 'model', @get('model').filter (el) ->
        return el != task

    addTask: ->
      newTask = @store.createRecord 'task',
        name: @get('newTaskName')
        isComplete: false
      newTask.save()

      @get('model').pushObject(newTask)
      @set('newTaskName', undefined)
        

`export default TaskController;`
