`import Ember from 'ember';`

TaskController = Ember.Controller.extend

  currentFilter: 'all'

  newTaskName: ''

  activeCount: Ember.computed 'model.@each.isComplete',  ->
    @get('model').filterBy('isComplete', false).length

  tasks: Ember.computed 'model', 'model.@each.isComplete', 'currentFilter', ->
    filter = @get('currentFilter')
    if filter == 'all'
      @get('model')
    else if filter == 'active'
      @get('model').filterBy('isComplete', false)
    else if filter == 'complete'
      @get('model').filterBy('isComplete', true)


  all: Ember.computed 'currentFilter', ->
    @get('currentFilter') == 'all'

  active: Ember.computed 'currentFilter', ->
    @get('currentFilter') == 'active'

  complete: Ember.computed 'currentFilter', ->
    @get('currentFilter') == 'complete'


  actions:
    filterClick: (btn) ->
      @set('currentFilter', btn)

    removeTask: (task) ->
      @store.findRecord('task', task.id, backgroundReload: false).then((t) ->
        t.destroyRecord()
      )

    addTask: ->
      newName = @get('newTaskName')
      if newName == ''
        return

      newTask = @store.createRecord 'task',
        name: @get('newTaskName')
        isComplete: false
      newTask.save()

      @set('newTaskName', '')

    toggleComplete: (task) ->
      @store.findRecord('task', task.id, backgroundReload: false).then((t) ->
        t.set('isComplete', !t.get('isComplete'))
        t.save()
      )

    removeComplete: () ->
      @get('model').forEach((task) ->
        if task.get('isComplete')
          task.destroyRecord()
      )


`export default TaskController;`
