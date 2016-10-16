`import Ember from 'ember';`

TaskController = Ember.Controller.extend
  tasks: Ember.computed.alias 'model'

`export default TaskController;`
