Approach

Using django with restframework and django-filter.

With the spec'd endpoints I'm using restframework for its serialization and validation
plus the base views, rather than for any RESTful design or routing.
 
A faster approach to a microservice could be flask, or nameko perhaps.

I decided to use the built-in sqlite db.

The django-filter backend for djr is configured and so I've created filter sets for the views,
for automatic field filtering.
