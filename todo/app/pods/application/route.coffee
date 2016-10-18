`import Ember from 'ember';`

AppRoute = Ember.Route.extend
  beforeModel: ->
    @transitionTo('tasks')

`export default AppRoute;`
