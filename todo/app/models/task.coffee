`import DS from 'ember-data';`

TaskModel = DS.Model.extend
  name: DS.attr('string')
  isCompleted: DS.attr('boolean')

`export default TaskModel;`
