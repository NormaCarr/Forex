### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  JS can be used frontend and is used for backend development as well (pretty efficiently). Python is used on the backend only, since browsers don't run it.
- Given a dictionary like ``{"a": 1, "b": 2}``: , list two    
  ways  you can try to get a missing key (like "c") *without* your programming crashing.
    1. importing "collections" for defaultdict
      import collections
    2. sets default value 'Key Not found' to absent keys
      collections.defaultdict(lambda : 'Key Not found')
- What is the role of web application framework, like Flask? 
  Frameworks automate the implementation of several tasks and give developers a structure for application development.
- What is a unit test?
- The unit test is implemented to test the functionality of an individual parts of the code.

- What is an integration test?
  In this step, the application components are tested to verify that they are working well together. 

- What is the role of web application framework, like Flask?
  To emulate the interaction between the server and client in the development process. 
- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  It depends on the purpose of the application. I will use the first to direct the user to the pretzel link; otherwise, I will use the second if there is a consult and it is necessary to have a value for the type

- How do you collect data from a URL placeholder parameter using Flask?
   By writing the name argument in the view function.
  

- How do you collect data from the query string using Flask?
   Using the keyword request.args.get('something')

- How do you collect data from the body of the request using Flask?
  using request.form.get('identifier')
  
- What is a cookie and what kinds of things are they commonly used for?
  A cookie is data stored in the web browser. These data are used to remember information about user web navigation, it can be username, preferences, interest, configurations. The Set-Cookie HTTP response header is used to send a cookie from the server to the user agent, so that the user agent can send it back to the server later
- What is the session object in Flask?
  It is a dictionary that contains a key-value and its value. You can use the Session object to store information needed for a particular user session. Variables stored in a Session object hold common information like name, id, and preferences about one single user, and are available to all pages in one application.
  
- What does Flask's `jsonify()` do?
  convert a dictionary in to JSON string
