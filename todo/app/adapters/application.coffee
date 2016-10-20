`import DS from 'ember-data'`
`import ENV from 'todo/config/environment';`

ApplicationAdapter = DS.JSONAPIAdapter.extend
  host: ENV.apiHost

`export default ApplicationAdapter`
