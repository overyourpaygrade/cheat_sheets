######What is an object?

######Terminology
```
Class - a template - dog
Method or Message - a defined capability of a class - bark()
Field or attribute - a bit of data in a class - length
Object or instance - a particular instance of a class - Lassie
```
######Example:
```python
class PartyAnimal:

  x = 0
  
  def party(self):
    self.x = self.x + 1
    print "So far", self.x

an = PartyAnimal()

an.party()
```

###### Object Life Cycle

* Constructor
