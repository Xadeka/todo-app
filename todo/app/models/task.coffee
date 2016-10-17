`import DS from 'ember-data';`

TaskModel = DS.Model.extend
  name: DS.attr('string')
  isComplete: DS.attr('boolean')

`export default TaskModel;`
