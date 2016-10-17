`import DS from 'ember-data'`

ApplicationAdapter = DS.JSONAPIAdapter.extend
  host: 'http://127.0.0.1:5000/api/v1'

`export default ApplicationAdapter`
