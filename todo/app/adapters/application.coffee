`import DS from 'ember-data'`

ApplicationAdapter = DS.JSONAPIAdapter.extend
  host: process.env.todoHost

`export default ApplicationAdapter`
